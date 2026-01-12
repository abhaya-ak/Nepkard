document.addEventListener("DOMContentLoaded", () => {
    const slider = document.getElementById("centerSlider");
    const slides = Array.from(slider.children);
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");

    let currentIndex = 0;

    function updateSlider() {
    slides.forEach((slide, index) => {
        slide.classList.remove("active");
        if (index === currentIndex) {
            slide.classList.add("active");
        }
    });

    const sliderRect = slider.parentElement.getBoundingClientRect();
    const activeSlide = slides[currentIndex];
    const slideRect = activeSlide.getBoundingClientRect();

    const sliderCenter = sliderRect.width / 2;
    const slideCenter =
        activeSlide.offsetLeft + slideRect.width / 2;

    const translateX = slideCenter - sliderCenter;

    slider.style.transform = `translateX(${-translateX}px)`;
}

    nextBtn.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % slides.length;
        updateSlider();
    });

    prevBtn.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        updateSlider();
    });

    // Auto slide (like Slick autoplay)
    setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        updateSlider();
    }, 3500);

    updateSlider();
});
