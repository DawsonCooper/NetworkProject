// GLOBAL ELEMENTS
    const imageInput = document.querySelector("#id_image");
    const imageLabel = document.querySelector("#image-label");
    const imageContainer = document.querySelector("#image-container");
    const likeButton = document.querySelectorAll(".like");
    const dislikeButton = document.querySelectorAll(".dislike");
    const commentButton = document.querySelectorAll(".comment");

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
function interactButtonHover(button){
    for(let i=0; i < button.length; i++){
        
        button[i].addEventListener('mouseover', () =>{
           button[i].childNodes[0].setAttribute("type", "solid");
        });
        button[i].addEventListener('mouseout', () => {
            if(button[i].childNodes[0]._state.color === "red"){
                button[i].childNodes[0].setAttribute("type", "solid");  
            }else{
                button[i].childNodes[0].setAttribute("type", "regular");
            }
        })
       
            button[i].addEventListener('click', (e) =>{
                e.preventDefault();
                let postId = button[i].name;
                if (button != commentButton){
                    if (button[i].childNodes[0]._state.color != "red"){
                        button[i].childNodes[0].setAttribute("type", "solid");
                        button[i].childNodes[0].setAttribute("color", "red");
                    }else{
                        button[i].childNodes[0].setAttribute("color", 'white');
                        button[i].childNodes[0].setAttribute("type", 'solid');
                    }
                }
                fetch(`/like/${postId}`, {
                    method: 'POST',
                }).then(response => response.json())
                .then(result => console.log(result))
                .catch(error => console.log(error));
            })
        }}





document.addEventListener('DOMContentLoaded', function() {
    interactButtonHover(likeButton)
    interactButtonHover(dislikeButton)
    interactButtonHover(commentButton)
    if (imageInput){
        imageInput.addEventListener("change", imagePreview);
    }
    document.querySelector('#newPostButton').addEventListener('mouseover', () => {
    document.querySelector('#newPostSvg').setAttribute("animation", "tada"); 
    });
    document.querySelector('#newPostButton').addEventListener('mouseout', () => {
        document.querySelector('#newPostSvg').setAttribute("animation", "none"); 
    });

    })