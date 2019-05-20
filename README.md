<h1>Fast Style Transfer using <a href="https://github.com/keras-team/keras">Keras</a></h1>
<p>
Rendering the semantic content of an image in different styles is a difficult image processing task. A task which a human would take days or months to complete is done within seconds using neural networks. We used pretrained models VGG-16 and VGG-19 using image and video as inputs to compare their quality of style transfer and performance. We also experimented by adding texture upon style on the content image.
</p>

<h3>Content Image + Style Image = Stylized Image</h3>
    <div display="inline-block">
      <a href="/images/content/tandon_image.jpg">
        <img src="/images/content/tandon_image.jpg" height="246px" style="max-width:100%;">
      </a>  
      <a href="/images/style/wave_crop.jpg"> 
        <img src="/images/style/wave_crop.jpg" height="246px" style="max-width:100%;">
      </a>
      <a href="/results/vgg16_image_transform/tandon_wavercrop_output.png"> 
        <img src="/results/vgg16_image_transform/tandon_wavercrop_output.png" height="246px" style="max-width:100%;">
      </a>
    </div>
   </br>

<h2>Results</h2>
<h3>Image Style Transfer using VGG-16 and VGG-19</h3>

<p>Content and Style image</p>
   
   <div display="inline-block">
    <a href="/images/content/tandon_image.jpg">
     <img src="/images/content/tandon_image.jpg" height="246px" width="250px"">
    </a> 
    <a href="/images/style/wave_crop.jpg"> 
      <img src="/images/style/la_muse.jpg" height="246px" width="250px"">
    </a>
   </div> 

 <p>VGG16 and VGG19 output images</p> 
   <div display="inline-block">
    <a href="/results/vgg16_image_transform/tandon_la_muse_output.png">
     <img src="/results/vgg16_image_transform/tandon_la_muse_output.png" height="246px" width="250px"">
    </a>   
    <a href="/results/vgg19_image_transform/tandon_la_muse_output.jpg"> 
      <img src="/results/vgg19_image_transform/tandon_la_muse_output.jpg" height="246px" width="250px"">
    </a>
   </div> 

 
<h3>The outcome of texture and style addition on content image using VGG-16</h3>
<h4>Content Image + Style Image + Texture Image = Texture Style Output Image</h4>
<p>Content, Style and Texture Images</p>
   <div display="inline-block">
    <a href="/images/content/101.jpg">
     <img src="/images/content/101.jpg" height="246px" width="250px">
    </a>   
    <a href="/results/Texture_transform/wave_crop.jpg"> 
      <img src="/results/Texture_transform/wave_crop.jpg" height="246px" width="250px">
    </a>
    <a href="/results/Texture_transform/texture.jpg">
     <img src="/results/Texture_transform/texture.jpg" height="246px" width="250px">
    </a>
   </div>
 
 <p>Style Output without Textute and Style and Texture Output Image</p>
   <div display="inline-block">
    <a href="/images/generated/wave_crop_output.png"> 
      <img src="/images/generated/wave_crop_output.png" height="246px" width="250px"">
    </a>
    <a href="/results/Texture_transform/texture_wavecrop_output.png"> 
      <img src="/results/Texture_transform/texture_wavecrop_output.png" height="246px" width="250px"">
    </a>
   </div> 
 

<h3>Video Style Transfer using VGG-19</h3>
<p>Content Video</p>
 <div align="center">
    <a href="https://www.youtube.com/watch?v=3hoThry5WsY">
       <img src="/results/Video_Transform/video_input_gif.gif" alt="Content Video" width="800px" height="400px" style="max-width:100%;">
     </a>
</div>
<p>Stylized Video</p>
<div align="center">
    <a href="https://www.youtube.com/watch?v=3hoThry5WsY">
       <img src="/results/Video_Transform/video_output_gif.gif" alt="Stylized Video" width="800px" height="400px" style="max-width:100%;">
     </a>
</div>

<div>
<h2>Implementation</h2>
<p>We train with MS-COCO training set and prepare low-resolution inputs by blurring with a Gaussian kernel of width σ = 1.0 and down-sampling with bicubic interpolation. We resize each of the 80k training images to 256 × 256 and train with 2 epochs on the whole dataset. We use Adam with learning rate 1 × 10−3. The output images are regularized with total variation regularization with a strength of between 1 × 10−6 and 1×10−4, chosen via cross-validation per style target. For style transfer experiments, we compute feature reconstruction loss at layer ‘block3_conv3’ and style reconstruction loss at layers ‘block1_conv2’, ‘block2_conv2’, ‘block3_conv3’ and ‘block4_conv3’ of the VGG-16 loss network. For VGG-19, we compute feature reconstruction loss at layer ‘block4_conv2’ and style reconstruction loss at layers ‘block1_conv1’, ‘block2_conv1’, ‘block3_conv1’, ‘block4_conv1’ and ‘block5_conv1’ of the loss network. The code has been implemented in Keras using Tensorflow as the backend. Training takes roughly 4 hours on a single P40 GPU.</p>
</div>

<div>
   <h2>Usage</h2>
   <h3>1. Training models VGG-16 and VGG-19</h3>
     <p>python3 train.py --style <<path to style image>> --output <output file name without extension> </p>
     <p><b>Note:</b> Dataset should be kept in images/dataset location.</br>
      Uncomment line 17 and comment line 20 of train.py for training VGG-19.</p>
        
   <h3>2. Image Style transfer using VGG-16 and VGG-19 models</h3>   
      <p>python3 transform.py --style <path to style model> --input <path to content image></p>
      <p><b>Note:</b> Uncomment line 22 and comment line 25 of transform.py for VGG-19 model for Style transfer.</p>
   <h3>3. Texture and style addition to content image</h3>
      <p>python3 texture_trasform.py --texture <texture model file path> --style <style model file path> --input <input file path> --output <output filename with out extension></p>
   <h3>4. Video Style Transfer using VGG-16 model</h3>
      <p>python3 video_transform.py --input <path to input video> --style <style model path> --output <output filename without extension></p>
          </div>

<div>
    <h2>Acknowledgement</h2>
    <p>We would like to thank Prof. Sundeep Rangan for advising us for the project and providing Google Cloud Platform GPU credits. Also, we would like to thank Sam Lee and Logan Engstrom whose Style Transfer code open-sourced on GitHub has been used and modified in this project.</p>
</div>
 
  
  
 
