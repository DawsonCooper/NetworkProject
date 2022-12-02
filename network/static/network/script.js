function sendPost(caption = "", image = undefined) {
    fetch('/sendPost', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
        },
        body: JSON.stringify({
            caption: caption,
            image: image
        })
    }).catch(error => alert(error));
}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector("#post").addEventListener('submit', (e) => {
        e.preventDefault();
        text = document.querySelector("#caption").value;
        sendPost(text);
        // TODO: SETUP A SECOND FORM THAT WILL GET AN IMAGE FROM THE USER IF THEY WANT
    })
})