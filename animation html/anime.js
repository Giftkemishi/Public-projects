document.addEventListener('DOMContentLoaded', function() {
    // Info boxes hover effect
    const boxes = document.querySelectorAll('.box');
    boxes.forEach(box => {
        box.addEventListener('mouseover', () => {
            boxes.forEach(b => {
                if (b !== box) {
                    b.style.transform = 'scale(0.9)';
                    b.style.opacity = '0.8';
                }
            });
        });
        
        box.addEventListener('mouseout', () => {
            boxes.forEach(b => {
                b.style.transform = 'scale(1)';
                b.style.opacity = '1';
            });
        });
    });

    // Image slider functionality
    const slider = document.querySelector('.product-slider');
    const slides = document.querySelectorAll('.slide');
    const texts = document.querySelectorAll('.text');
    let currentSlide = 0;
    let intervalId;

    function showSlide(index) {
        // Hide all slides and texts
        slides.forEach(slide => slide.classList.remove('active'));
        texts.forEach(text => text.classList.remove('active'));
        
        // Show current slide and text
        slides[index].classList.add('active');
        texts[index].classList.add('active');
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    // Start auto-sliding
    function startSlider() {
        intervalId = setInterval(nextSlide, 2000);
    }

    // Stop auto-sliding
    function stopSlider() {
        clearInterval(intervalId);
    }

    // Initialize slider
    showSlide(0);
    
    // Start auto-slide when mouse enters slider
    slider.addEventListener('mouseenter', () => {
        startSlider();
    });
    
    // Stop and reset when mouse leaves
    slider.addEventListener('mouseleave', () => {
        stopSlider();
        currentSlide = 0;
        showSlide(currentSlide);
    });
});