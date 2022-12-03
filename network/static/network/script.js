// GLOBAL ELEMENTS
const imageInput = document.querySelector("#id_image");
const imageLabel = document.querySelector("#image-label");
const imageContainer = document.querySelector("#image-container");
let userImage;

// GLOABAL FUNCTIONS 

function imagePreview() {
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            let image = reader.result;
            let imgElem = document.createElement("img");
            imgElem.src = image;
            imgElem.setAttribute("id", "selected-image");
            imageContainer.insertBefore(imgElem, imageLabel);

        }
    } else {
        return;
    }

}



document.addEventListener('DOMContentLoaded', function() {
    imageInput.addEventListener("change", imagePreview);
    document.querySelector('#newPostButton').addEventListener('mouseover', () => {
        document.querySelector('#newPostSvg').setAttribute("animation", "tada"); 
    });
    document.querySelector('#newPostButton').addEventListener('mouseout', () => {
        document.querySelector('#newPostSvg').setAttribute("animation", "none"); 
    });
    })