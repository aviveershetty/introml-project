from keras.layers import Input, merge
from keras.models import Model,Sequential
from layers import VGGNormalize,ReflectionPadding2D,Denormalize,conv_bn_relu,res_conv,dconv_bn_nolinear
from loss import dummy_loss,StyleReconstructionRegularizer,FeatureReconstructionRegularizer,TVRegularizer
from keras.optimizers import Adam, SGD,Nadam,Adadelta
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from scipy.misc import imsave, imshow
import time
import numpy as np 
import argparse
import h5py
import tensorflow as tf
import cv2


from skimage import color, exposure, transform
from scipy import ndimage
from scipy.ndimage.filters import median_filter
from img_util import preprocess_image, preprocess_image_for_generating, preprocess_reflect_image, crop_image, preprocess_reflect_video

#uncomment this while running VGG-19 architecture
#import nets_vgg19 as nets

#comment this while running Vgg-19 architecture
import nets

count = 1


#out1 = cv2.VideoWriter('output_in.avi',fourcc, 20.0, (frame_width,frame_height))

# from 6o6o's fork. https://github.com/6o6o/chainer-fast-neuralstyle/blob/master/generate.py
def original_colors(original, stylized,original_color):
    # Histogram normalization in v channel
    ratio=1. - original_color 

    hsv = color.rgb2hsv(original/255)
    hsv_s = color.rgb2hsv(stylized/255)

    hsv_s[:,:,2] = (ratio* hsv_s[:,:,2]) + (1-ratio)*hsv [:,:,2]
    img = color.hsv2rgb(hsv_s)    
    return img

def blend(original, stylized, alpha):
    return alpha * original + (1 - alpha) * stylized



def median_filter_all_colours(im_small, window_size):
    """
    Applies a median filer to all colour channels
    """
    ims = []
    for d in range(3):
        im_conv_d = median_filter(im_small[:,:,d], size=(window_size,window_size))
        ims.append(im_conv_d)

    im_conv = np.stack(ims, axis=2).astype("uint8")
    
    return im_conv

def load_weights(model,file_path):
    f = h5py.File(file_path)

    layer_names = [name for name in f.attrs['layer_names']]

    for i, layer in enumerate(model.layers[:31]):
        g = f[layer_names[i]]
        weights = [g[name] for name in g.attrs['weight_names']]
        layer.set_weigh
        ts(weights)

    f.close()
    
    print('Pretrained Model weights loaded.')



#class to derive inference on videos 
class video_predictor:
    #init function to load parameters
    def __init__(self, image, media_filter, blend_alpha, original_color, style, output_file):
        aspect_ratio, x = preprocess_reflect_video(image, size_multiple=4)
        img_width= img_height = x.shape[1]
        print("img_width = ", img_width)
        self.net = nets.image_transform_net(img_width,img_height)
        self.model = nets.loss_net(self.net.output,self.net.input,img_width,img_height,"",0,0)


        self.model.compile(Adam(),  dummy_loss)  # Dummy loss since we are learning from regularizes

        self.model.load_weights(style,by_name=False)

    #predictor function for each frame
    def pred(self, image, media_filter, blend_alpha, original_color, style, output_file):
        aspect_ratio, x = preprocess_reflect_video(image, size_multiple=4)
        t1 = time.time()
        y = self.net.predict(x)[0] 
        y = crop_image(y, aspect_ratio)

        print("process: %s" % (time.time() -t1))

        ox = crop_image(x[0], aspect_ratio)

        y =  median_filter_all_colours(y, media_filter)

        if blend_alpha > 0:
            y = blend(ox,y,blend_alpha)


        if original_color > 0:
            y = original_colors(ox,y,original_color )


        #imsave('%s_output.png' % output_file, y)
        #imshow(y)
        return y



def main(args):
    count = 1
    style= args.style
    
    output_file =args.output
    input_file = args.input
    original_color = args.original_color
    blend_alpha = args.blend
    media_filter = args.media_filter


    cap = cv2.VideoCapture(input_file)
    frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("frame_width = ", frame_width)
    frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
    print("frame_height = ", frame_height)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(input_file + '_output.mp4',fourcc, 20.0, (frame_width,frame_height))
    
    #read video frame by fame and process
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == 1:
            print("image read successful")

        #change color format for processing
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        
        if count == 1:
            count += 1
            video_pred = video_predictor(image = image,media_filter = media_filter,blend_alpha = blend_alpha, 
                original_color = original_color,style = style, output_file = output_file )

        #call the transform function in video predictor class
        image = video_pred.pred(image = image,media_filter = media_filter,blend_alpha = blend_alpha, 
                original_color = original_color,style = style, output_file = output_file )

        #change the color format back for saving
        new_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Save the resulting frame as part of the video
        out.write(new_image)

        # Display the resulting frame
        #cv2.imshow('transformed video',new_image)
        cv2.waitKey(5)





    #release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    
    
        
 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Real-time style transfer')

    parser.add_argument('--style', '-s', type=str, required=True,
                        help='style model path')

    parser.add_argument('--input', '-i', type = str, required=True,
                        help='input file name')

    parser.add_argument('--output', '-o', default=None, required=True,type=str,
                        help='output file name without extension')

    parser.add_argument('--original_color', '-c', default=0, type=float,
                        help='0~1 for original color')

    parser.add_argument('--blend', '-b', default=0, type=float,
                        help='0~1 for blend with original image')

    parser.add_argument('--media_filter', '-f', default=3, type=int,
                        help='media_filter size')
    parser.add_argument('--image_size', default=256, type=int)

    args = parser.parse_args()
    main(args)
