<h1>Fast Style Transfer using <a href="https://github.com/keras-team/keras">Keras</a></h1>
<p>
Rendering the semantic content of an image in different styles is a difficult image processing task. A task which a human would take days or months to complete is done within seconds using neural networks. We used pretrained models VGG-16 and VGG-19 using image and video as inputs to compare their quality of style transfer and performance. We also experimented by adding texture upon style on the content image.
</p>

<div class="row">
  <h3>Content Image + Style Image = Stylized Image</h3>
  <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/images/content/tandon_image.jpg">
      <img src="/images/content/tandon_image.jpg" style="max-width:100%;">
    </a>
  </div>
  <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/images/style/wave_crop.jpg"> 
      <img src="/images/style/wave_crop.jpg" style="max-width:100%;">
    </a>
  </div>
  <div class="column" style="float: left;width: 33.33%; padding: 5px;">
   `<a href="/results/vgg16_image_transform/tandon_wavercrop_output.png"> 
      <img src="/results/vgg16_image_transform/tandon_wavercrop_output.png" style="max-width:100%;">
    </a>
  </div>
</div>

<h2>Results</h2>
<p>Image Style Transfer using VGG-16 and VGG-19</p>

 <div>
  <div class="row">
   <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/images/content/tandon.jpg">
     <img src="/images/content/tandon.jpg" style="max-width:100%;">
    </a>
   </div>
   <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/images/style/wave_crop.jpg"> 
      <img src="/images/style/la_muse.jpg" style="max-width:100%;">
    </a>
   </div> 
  </div>
  <div class="row">
   <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/results/vgg16_image_transform/tandon_wavercrop_output.png">
     <img src="/results/vgg16_image_transform/tandon_wavercrop_output.png" style="max-width:100%;">
    </a>
   </div>
   <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/results/vgg19_image_transform/tandon_la_muse_output.jpg"> 
      <img src="/results/vgg19_image_transform/tandon_la_muse_output.jpg" style="max-width:100%;">
    </a>
   </div> 
  </div>
 </div>
 
<p>The outcome of texture and style addition on content image using VGG-16</p>

 <div>
  <div class="row">
   <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/images/content/101.jpg">
     <img src="/images/content/101.jpg" style="max-width:100%;">
    </a>
   </div>
   <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/results/Texture_transform/wave_crop.jpg"> 
      <img src="/results/Texture_transform/wave_crop.jpg" style="max-width:100%;">
    </a>
   </div> 
  </div>
  <div class="row">
   <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/results/Texture_transform/texture.jpg">
     <img src="/results/Texture_transform/texture.jpg" style="max-width:100%;">
    </a>
   </div>
   <div class="column" style="float: left;width: 33.33%; padding: 5px;">
    <a href="/results/Texture_transform/texture_wavecrop_output.png"> 
      <img src="/results/Texture_transform/texture_wavecrop_output.png" style="max-width:100%;">
    </a>
   </div> 
  </div>
 </div>

<p>Video Style Transfer using VGG-19</p>
<p>Content Video</p>
 <div align="center">
    <a href="https://www.youtube.com/watch?v=xVJwwWQlQ1o">
       <img src="/results/Video_Transform/video_input_gif.gif" alt="Content Video" width="800px" height="400px" style="max-width:100%;">
     </a>
</div>
<p>Stylized Video</p>
<div align="center">
    <a href="https://www.youtube.com/watch?v=xVJwwWQlQ1o">
       <img src="/results/Video_Transform/video_output_gif.gif" alt="Content Video" width="800px" height="400px" style="max-width:100%;">
     </a>
</div>

 
  
  
 
