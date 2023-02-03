var imageBox = document.querySelectorAll('.imageBox');
var modalSlide = document.querySelectorAll('.modal-slide');



//Automaically generate modal content
var modal = document.querySelector('.modal-content');

function createSlideItem(text) {
    var slide_item = document.createElement('div');
    slide_item.className = "mySlides";
    slide_item.innerHTML = text;
    return slide_item;
}

var items = []

for (i = 0; i < modalSlide.length; i++) {
    items.push(createSlideItem(modalSlide[i].innerHTML))
    var anchor = imageBox[i];
}

items.forEach(function(slide_item) {
    modal.appendChild(slide_item)
})


// Open the Modal
function openModal() {
    document.getElementById("myModal").style.display = "block";


}


// Close the Modal
function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);




// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);

}

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    var i;
    var slides = document.querySelectorAll(".mySlides");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideIndex - 1].style.display = "block";
}