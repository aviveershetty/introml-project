<h1>Fast Style Transfer using <a href="https://github.com/keras-team/keras">Keras</a></h1>
<p>
Rendering the semantic content of an image in different styles is a difficult image processing task. A task which a human would take days or months to complete is done within seconds using neural networks. We used pretrained models VGG-16 and VGG-19 using image and video as inputs to compare their quality of style transfer and performance. We also experimented by adding texture upon style on the content image.
</p>

  <h3>Content Image + Style Image = Stylized Image</h3>
  <div display="inline-block">
    <div>
      <a href="/images/content/tandon_image.jpg">
        <img src="/images/content/tandon_image.jpg" height="246px" style="max-width:100%;" align="left">
      </a>
    </div>
    <div>
      <a href="/images/style/wave_crop.jpg"> 
        <img src="/images/style/wave_crop.jpg" height="246px" style="max-width:100%;" align="middle">
      </a>
    </div>
    <div>
     `<a href="/results/vgg16_image_transform/tandon_wavercrop_output.png"> 
        <img src="/results/vgg16_image_transform/tandon_wavercrop_output.png" height="246px" style="max-width:100%;">
      </a>
    </div>
  </div>
  </br>

<h2>Results</h2>
<h3>Image Style Transfer using VGG-16 and VGG-19</h3>

   <div>
    <a href="/images/content/tandon_image.jpg">
     <img src="/images/content/tandon_image.jpg" height="246px" style="max-width:100%;">
    </a>
   </div>
   <div>
    <a href="/images/style/wave_crop.jpg"> 
      <img src="/images/style/la_muse.jpg" height="246px" style="max-width:100%;">
    </a>
   </div> 

  
   <div>
    <a href="/results/vgg16_image_transform/tandon_wavercrop_output.png">
     <img src="/results/vgg16_image_transform/tandon_wavercrop_output.png" height="246px" style="max-width:100%;">
    </a>
   </div>
   <div>
    <a href="/results/vgg19_image_transform/tandon_la_muse_output.jpg"> 
      <img src="/results/vgg19_image_transform/tandon_la_muse_output.jpg" height="246px" style="max-width:100%;">
    </a>
   </div> 

 
<h3>The outcome of texture and style addition on content image using VGG-16</h3>

   <div>
    <a href="/images/content/101.jpg">
     <img src="/images/content/101.jpg" height="246px" style="max-width:100%;">
    </a>
   </div>
   <div>
    <a href="/results/Texture_transform/wave_crop.jpg"> 
      <img src="/results/Texture_transform/wave_crop.jpg" height="246px" style="max-width:100%;">
    </a>
   </div> 


   <div>
    <a href="/results/Texture_transform/texture.jpg">
     <img src="/results/Texture_transform/texture.jpg" height="246px" style="max-width:100%;">
    </a>
   </div>
   <div>
    <a href="/results/Texture_transform/texture_wavecrop_output.png"> 
      <img src="/results/Texture_transform/texture_wavecrop_output.png" height="246px" style="max-width:100%;">
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

 
  
  
 
