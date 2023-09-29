function submitForm() {
    const emailInput = document.querySelector(".input-Email").value;


    const xhr = new XMLHttpRequest();
    const formData = new FormData();

    formData.append("email", emailInput);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            console.log(xhr.status)
            if (xhr.status === 200) {
                backblur.classList.add("active")
                boxmessage.classList.add("active")
            } else {
                console.error("Form submission failed.");
            }
        }
    };

    xhr.open("GET", "https://www.google.com/");
    xhr.send('null');
}
