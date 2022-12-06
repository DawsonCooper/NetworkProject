// GLOBAL ELEMENTS
    const imageInput = document.querySelector("#id_image");
    const imageLabel = document.querySelector("#image-label");
    const imageContainer = document.querySelector("#image-container");
    const likeButton = document.querySelectorAll(".like");
    const dislikeButton = document.querySelectorAll(".dislike");
    const commentButton = document.querySelectorAll(".comment");
    function sendInteraction(body, postId){
        fetch(`/like/${postId}`, {
            method: 'POST',
            body: JSON.stringify({
                body: body,
            })
            }).then(response => response.json())
            .then(result => console.log(result))
            .catch(error => alert(error));
    }
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
            if(button[i].childNodes[0].attributes.color.nodeValue == "red"){
                button[i].childNodes[0].setAttribute("type", "solid");  
            }else{
                button[i].childNodes[0].setAttribute("type", "regular");
            }
        })
       
            button[i].addEventListener('click', (e) =>{
                e.preventDefault();
                postId = button[i].name;
                if (button != commentButton){
                    if (button[i].childNodes[0].attributes.color.nodeValue != "red"){
                        button[i].childNodes[0].setAttribute("type", "solid");
                        button[i].childNodes[0].setAttribute("color", "red");
                        if (button == likeButton){
                            sendInteraction('like', postId);
                            dislikeButton.childNodes[0].setAttribute("type", "regular");
                            dislikeButton.childNodes[0].setAttribute("color", "white");
                            
                        }else{
                            sendInteraction('dislike', postId);
                            likeButton.childNodes[0].setAttribute("type", "regular");
                            likeButton.childNodes[0].setAttribute("color", "white");
                            
                        }
                    }else{
                        sendInteraction('undo', postId);
                        button[i].childNodes[0].setAttribute("color", 'white');
                        button[i].childNodes[0].setAttribute("type", 'solid');
                    }
                }else{
                    // TODO: WE WILL WANT TO REPLACE COMMENT WITH THE BODY FROM SOME TEXT FIELD
                    sendInteraction('comment', postId);
                }
                
            })
        }}





document.addEventListener('DOMContentLoaded', function() {
    interactButtonHover(likeButton)
    interactButtonHover(dislikeButton)
    interactButtonHover(commentButton)
    let interactionsArr;
    fetch(`/get_user_interactions`, {
        method: 'GET',
        }).then(response => response.json())
        .then(result => {
            for (let i = 0; i < result.length; i++){
                console.log(result);
                let arrOfButtons = document.querySelectorAll(`[name="${result[i].post}"]`);
                console.log(arrOfButtons)
                if(result[i].status == 1){
                    arrOfButtons[0].childNodes[0].setAttribute('color', 'red');
                    arrOfButtons[0].childNodes[0].setAttribute('type', 'solid');
                }else if(result[i].status == -1){
                    arrOfButtons[1].childNodes[0].setAttribute('color', 'red');
                    arrOfButtons[1].childNodes[0].setAttribute('type', 'solid'); 
                }
            }
        })
        .catch(error => console.log(error));

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