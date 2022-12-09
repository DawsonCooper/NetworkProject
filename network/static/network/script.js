// GLOBAL ELEMENTS
const imageInput = document.querySelector("#id_image");
const imageLabel = document.querySelector("#image-label");
const imageContainer = document.querySelector("#image-container");
const likeButton = document.querySelectorAll(".like");
const dislikeButton = document.querySelectorAll(".dislike");
const commentButton = document.querySelectorAll(".comment");    
const editButtonArr = document.querySelectorAll('#editPostButton');
const editForms = document.querySelectorAll('#editPostForm');
const editSubButtons = document.querySelectorAll('#edit-sub');
function sendInteraction(body, postId){
        fetch(`/like/${postId}`, {
            method: 'POST',
            body: JSON.stringify({
                body: body,
            })
            }).then(response => response.json())
            .then(result => console.log(result))
            .catch(error => alert(error));
            setTimeout(() => {
                update_interaction_count()
            }, 100);
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
                            dislikeButton[i].childNodes[0].setAttribute("type", "regular");
                            dislikeButton[i].childNodes[0].setAttribute("color", "white");
                            
                        }else{
                            sendInteraction('dislike', postId);
                            likeButton[i].childNodes[0].setAttribute("type", "regular");
                            likeButton[i].childNodes[0].setAttribute("color", "white");
                            
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
function get_post_data(postId,caption) {
    
    fetch(`/get_post_data/${postId}`, {
        method: 'GET'
    }).then(response => response.json())
    .then(result => caption.innerText = result.caption)
    .catch(error => alert(error));
}

function submit_post_modification(postId, caption) {
    fetch(`update_post/${postId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ body: caption })
    });
}
function update_interaction_count(){
    fetch(`/update_interaction_count`, {
        method: 'GET',
        })
        .then(response => response.json())
        .then((result) => {
            console.log(result);
            for (let i = 0; i < result.length; i++) {
                likeCount = document.querySelector(`#p-${result[i].id}`);
                console.log(likeCount);
                likeCount.innerText = result[i].totalLikes
            }
        })
        .catch(error => console.log(error));
    }
function get_user_interactions(){
    fetch(`/get_user_interactions`, {
        method: 'GET',
        })
        .then(response => response.json())
        .then((result) => {
            for (let i = 0; i < result.length; i++){

                let arrOfButtons = document.querySelectorAll(`[name="${result[i].post}"]`);

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
    }

document.addEventListener('DOMContentLoaded', function() {

    for(let i = 0; i < editButtonArr.length; i++){
        for (let j = 0; j < editForms.length; j++){

            editButtonArr[i].addEventListener('click', () => {
                get_post_data(editForms[i].lastElementChild.id, editForms[j].childNodes[3].childNodes[1])
            })
        }
    }

    editForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault()
            let id = form.lastElementChild.id;
            console.log('id: ' +id)
            let caption = form.childNodes[3].childNodes[1].value;
            submit_post_modification(id, caption);
        })
    });
    get_user_interactions();
    interactButtonHover(likeButton);
    interactButtonHover(dislikeButton);
    interactButtonHover(commentButton);
    let interactionsArr;

    if (imageInput){
        imageInput.addEventListener("change", imagePreview);
    }
    document.querySelector('#newPostButton').addEventListener('mouseover', () => {
    document.querySelector('#newPostSvg').setAttribute("animation", "tada"); 
    });
    document.querySelector('#newPostButton').addEventListener('mouseout', () => {
        document.querySelector('#newPostSvg').setAttribute("animation", "none"); 
    });
    const editButton = document.querySelectorAll('#editPostButton');
    editButton.forEach(button => {

        button.addEventListener('mouseover', () => {
            button.childNodes[0].nextSibling.setAttribute("animation", "tada"); 
    });
        button.addEventListener('mouseout', () => {
            button.childNodes[0].nextSibling.setAttribute("animation", "none"); 
        });
    })        
});
