# Image Carousel Components

This directory contains reusable carousel implementations that can be used across project pages.

## Option 1: JavaScript Component (Recommended)

Use the `carousel.js` component for full programmatic control:

```html
<div id="my-carousel"></div>

<script src="/assets/js/carousel.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
  const images = [
    { src: '/assets/images/projects/my-project/image1.jpg', alt: 'Description 1' },
    { src: '/assets/images/projects/my-project/image2.jpg', alt: 'Description 2' },
    { src: '/assets/images/projects/my-project/image3.jpg', alt: 'Description 3' }
  ];
  
  new ImageCarousel('my-carousel', images, {
    width: '800px',
    height: '600px',
    caption: 'My project images',
    autoPlay: false
  });
});
</script>
```

## Option 2: Copy-Paste Template

For quick implementation, copy the template below and customize:

```html
<!-- Carousel Container -->
<div class="image-carousel" style="position: relative; width: 800px; height: 800px; margin: 2rem auto; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <div class="carousel-container" style="position: relative; width: 100%; height: 100%; overflow: hidden;">
    <!-- Slide 1 -->
    <div class="carousel-slide active" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 1; transition: opacity 0.5s ease-in-out;">
      <img src="IMAGE_1_PATH" alt="IMAGE_1_ALT" style="width: 100%; height: 100%; object-fit: contain; background: #f8f9fa;">
    </div>
    <!-- Slide 2 -->
    <div class="carousel-slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; transition: opacity 0.5s ease-in-out;">
      <img src="IMAGE_2_PATH" alt="IMAGE_2_ALT" style="width: 100%; height: 100%; object-fit: contain; background: #f8f9fa;">
    </div>
    <!-- Add more slides as needed -->
  </div>

  <!-- Navigation arrows -->
  <button class="carousel-prev" onclick="changeSlide(-1)" style="position: absolute; top: 50%; left: 15px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer; font-size: 18px; transition: background 0.3s; z-index: 10;">‹</button>
  <button class="carousel-next" onclick="changeSlide(1)" style="position: absolute; top: 50%; right: 15px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer; font-size: 18px; transition: background 0.3s; z-index: 10;">›</button>

  <!-- Dots indicator -->
  <div class="carousel-dots" style="position: absolute; bottom: 15px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; z-index: 10;">
    <span class="dot active" onclick="currentSlide(1)" style="width: 12px; height: 12px; border-radius: 50%; background: rgba(255,255,255,0.8); cursor: pointer; transition: background 0.3s;"></span>
    <span class="dot" onclick="currentSlide(2)" style="width: 12px; height: 12px; border-radius: 50%; background: rgba(255,255,255,0.4); cursor: pointer; transition: background 0.3s;"></span>
    <!-- Add more dots as needed -->
  </div>
</div>

<figcaption style="text-align: center; margin-top: 0.5rem; font-style: italic; color: #666; font-size: 0.9em;">YOUR_CAPTION_HERE</figcaption>

<!-- JavaScript -->
<script>
let slideIndex = 1;

function changeSlide(n) {
  showSlide(slideIndex += n);
}

function currentSlide(n) {
  showSlide(slideIndex = n);
}

function showSlide(n) {
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.dot');

  if (n > slides.length) { slideIndex = 1; }
  if (n < 1) { slideIndex = slides.length; }

  slides.forEach(slide => slide.style.opacity = '0');
  dots.forEach(dot => dot.classList.remove('active'));

  if (slides[slideIndex - 1]) {
    slides[slideIndex - 1].style.opacity = '1';
  }
  if (dots[slideIndex - 1]) {
    dots[slideIndex - 1].style.background = 'rgba(255,255,255,0.8)';
    dots[slideIndex - 1].classList.add('active');
  }

  dots.forEach((dot, index) => {
    if (index !== slideIndex - 1) {
      dot.style.background = 'rgba(255,255,255,0.4)';
      dot.classList.remove('active');
    }
  });
}

// Hover effects
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.carousel-prev, .carousel-next').forEach(btn => {
    btn.addEventListener('mouseenter', () => btn.style.background = 'rgba(0,0,0,0.7)');
    btn.addEventListener('mouseleave', () => btn.style.background = 'rgba(0,0,0,0.5)');
  });

  document.querySelectorAll('.dot').forEach(dot => {
    dot.addEventListener('mouseenter', () => {
      if (!dot.classList.contains('active')) {
        dot.style.background = 'rgba(255,255,255,0.6)';
      }
    });
    dot.addEventListener('mouseleave', () => {
      if (!dot.classList.contains('active')) {
        dot.style.background = 'rgba(255,255,255,0.4)';
      }
    });
  });
});
</script>
```

## Usage Tips

1. **JavaScript Component**: Best for complex carousels with dynamic content
2. **Copy-Paste Template**: Quick solution for static carousels
3. **Remember to update**:
   - Image paths and alt text
   - Number of dots to match number of images
   - Caption text
   - Carousel dimensions if needed