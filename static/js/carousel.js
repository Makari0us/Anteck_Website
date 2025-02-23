document.addEventListener('DOMContentLoaded', function() {
    // Initialize the carousel with a 3-second interval
    const carousel = new bootstrap.Carousel(document.getElementById('homeCarousel'), {
        interval: 3000,
        ride: 'carousel',
        pause: false
    });
});
