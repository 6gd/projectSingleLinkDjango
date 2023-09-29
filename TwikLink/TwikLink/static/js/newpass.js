let inputpassword = document.querySelectorAll(".input-password")
let textPassword = document.getElementById("textPassword")
let btnReset = document.querySelector(".btn-reset")

function isPasswordStrong(password) {
    if (password.length < 8) {
        return false;
    }

    const hasUppercase = /[A-Z]/.test(password);
    const hasLowercase = /[a-z]/.test(password);
    const hasNumber = /\d/.test(password);
    const hasSpecialChar = /[!@#$%^&*()_+[\]{};':"\\|,.<>/?]/.test(password);

    return hasUppercase && hasLowercase && hasNumber && hasSpecialChar;
}



inputpassword[0].addEventListener("input", () => {
    if (isPasswordStrong(inputpassword[0].value)){
        textPassword.textContent = "Password is Strong"

        gsap.fromTo(textPassword,.3 ,{y:-20,opacity:0} ,{ opacity:1,y:0,color:"#47b425"})
        inputpassword[0].style.border = "1px solid #47b425"
        inputpassword[1].removeAttribute("disabled",'')
    }else{
        textPassword.textContent = "Password is weak"
        gsap.fromTo(textPassword,.3 ,{y:-20,opacity:0} ,{ opacity:1,y:0,color:"#b42525"})
        inputpassword[0].style.border = "1px solid #b42525"
        inputpassword[1].setAttribute('disabled', '');
    }
})
inputpassword[1].addEventListener("input", () => {

    if (inputpassword[0].value == inputpassword[1].value){
        inputpassword[1].style.border = "1px solid #47b425"
        textPassword.textContent = ""
        btnReset.removeAttribute('disabled', '');

    }else if (inputpassword[1].value == ""){
        inputpassword[1].style.border = "0px solid #b42525"
        btnReset.setAttribute('disabled', '');

    }else{
        btnReset.setAttribute('disabled', '');

        inputpassword[1].style.border = "1px solid #b42525"
    }
})


