/**
 * Reusable Image Carousel Component
 * Usage: new ImageCarousel(containerId, images, options)
 */
class ImageCarousel {
  constructor(containerId, images, options = {}) {
    this.container = document.getElementById(containerId);
    this.images = images;
    this.options = {
      width: options.width || '800px',
      height: options.height || '800px',
      showDots: options.showDots !== false,
      showArrows: options.showArrows !== false,
      autoPlay: options.autoPlay || false,
      autoPlayInterval: options.autoPlayInterval || 3000,
      caption: options.caption || null,
      ...options
    };
    this.currentSlide = 0;
    
    this.init();
  }

  init() {
    if (!this.container) {
      console.error(`Carousel container with id "${this.containerId}" not found`);
      return;
    }

    this.render();
    this.bindEvents();
    
    if (this.options.autoPlay) {
      this.startAutoPlay();
    }
  }

  render() {
    // Create carousel HTML structure
    this.container.innerHTML = `
      <div class="image-carousel" style="position: relative; width: ${this.options.width}; height: ${this.options.height}; margin: 2rem auto; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <div class="carousel-container" style="position: relative; width: 100%; height: 100%; overflow: hidden;">
          ${this.images.map((img, index) => `
            <div class="carousel-slide ${index === 0 ? 'active' : ''}" 
                 style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: ${index === 0 ? '1' : '0'}; transition: opacity 0.5s ease-in-out;">
              <img src="${img.src}" alt="${img.alt || ''}" 
                   style="width: 100%; height: 100%; object-fit: contain; background: #f8f9fa;">
            </div>
          `).join('')}
        </div>

        ${this.options.showArrows ? `
          <button class="carousel-prev" style="position: absolute; top: 50%; left: 15px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer; font-size: 18px; transition: background 0.3s; z-index: 10;">‹</button>
          <button class="carousel-next" style="position: absolute; top: 50%; right: 15px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer; font-size: 18px; transition: background 0.3s; z-index: 10;">›</button>
        ` : ''}

        ${this.options.showDots ? `
          <div class="carousel-dots" style="position: absolute; bottom: 15px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; z-index: 10;">
            ${this.images.map((_, index) => `
              <span class="dot ${index === 0 ? 'active' : ''}" 
                    data-slide="${index}"
                    style="width: 12px; height: 12px; border-radius: 50%; background: rgba(255,255,255,${index === 0 ? '0.8' : '0.4'}); cursor: pointer; transition: background 0.3s;"></span>
            `).join('')}
          </div>
        ` : ''}
      </div>
      ${this.options.caption ? `<figcaption style="text-align: center; margin-top: 0.5rem; font-style: italic; color: #666; font-size: 0.9em;">${this.options.caption}</figcaption>` : ''}
    `;
  }

  bindEvents() {
    // Arrow navigation
    const prevBtn = this.container.querySelector('.carousel-prev');
    const nextBtn = this.container.querySelector('.carousel-next');
    
    if (prevBtn) prevBtn.addEventListener('click', () => this.changeSlide(-1));
    if (nextBtn) nextBtn.addEventListener('click', () => this.changeSlide(1));

    // Dot navigation
    const dots = this.container.querySelectorAll('.dot');
    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const slideIndex = parseInt(dot.dataset.slide);
        this.goToSlide(slideIndex);
      });
    });

    // Hover effects
    const arrows = this.container.querySelectorAll('.carousel-prev, .carousel-next');
    arrows.forEach(arrow => {
      arrow.addEventListener('mouseenter', () => {
        arrow.style.background = 'rgba(0,0,0,0.7)';
      });
      arrow.addEventListener('mouseleave', () => {
        arrow.style.background = 'rgba(0,0,0,0.5)';
      });
    });

    dots.forEach(dot => {
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
  }

  changeSlide(direction) {
    this.currentSlide += direction;
    
    if (this.currentSlide >= this.images.length) {
      this.currentSlide = 0;
    } else if (this.currentSlide < 0) {
      this.currentSlide = this.images.length - 1;
    }
    
    this.updateSlide();
  }

  goToSlide(index) {
    this.currentSlide = index;
    this.updateSlide();
  }

  updateSlide() {
    const slides = this.container.querySelectorAll('.carousel-slide');
    const dots = this.container.querySelectorAll('.dot');

    slides.forEach((slide, index) => {
      slide.style.opacity = index === this.currentSlide ? '1' : '0';
      slide.classList.toggle('active', index === this.currentSlide);
    });

    dots.forEach((dot, index) => {
      const isActive = index === this.currentSlide;
      dot.style.background = `rgba(255,255,255,${isActive ? '0.8' : '0.4'})`;
      dot.classList.toggle('active', isActive);
    });
  }

  startAutoPlay() {
    this.autoPlayTimer = setInterval(() => {
      this.changeSlide(1);
    }, this.options.autoPlayInterval);
  }

  stopAutoPlay() {
    if (this.autoPlayTimer) {
      clearInterval(this.autoPlayTimer);
    }
  }

  destroy() {
    this.stopAutoPlay();
    this.container.innerHTML = '';
  }
}

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = ImageCarousel;
}