gsap.registerPlugin(ScrollTrigger);


let menu = document.querySelector(".menu")
let nav = document.querySelector(".nav")
let Logo = document.querySelector(".Logo")
let NavItem = document.querySelector(".NavItem")
let Navlist = document.querySelector(".Navlist")
let loginas = document.querySelector(".loginas")
let logout = document.querySelector(".btn-logout")
let tl = gsap.timeline({duration:.5});
menu.addEventListener("click", ()=> {
    nav.classList.toggle("active")
    Logo.classList.toggle("active")
    NavItem.classList.toggle("active")
    Navlist.classList.toggle("active")
    logout.classList.toggle("active")
    loginas.classList.toggle("active")
    tl.set(Logo,{
        x:0,
        opacity:1,
    })
    if (nav.classList.contains("active")) {
        tl.to(nav,.8,{
            minHeight:'350px',
            ease:"expo.out"
        })
        tl.from(Logo,.4,{
            x: -150,
            opacity:0,
            ease:"expo.out"
        })        
    }else if(!nav.classList.contains("active")){
        
        tl.to(nav,{
            minHeight:'60px',
            ease:"expo.out"
        })
        tl.from(Logo,.2,{
            x: 100,
            opacity:0,
            ease:"expo.out"
        }) 
    }
    
})
window.addEventListener("resize", () => {
    if(window.innerWidth > 1180){
        gsap.to(nav,{
            minHeight:'60px',
            ease:"expo.out"
        })
        nav.classList.remove("active")
        Logo.classList.remove("active")
        NavItem.classList.remove("active")
        Navlist.classList.remove("active")
        logout.classList.remove("active")
        loginas.classList.remove("active")
    }
})

let likeone = document.getElementById("likeone")
let descriptionColor = document.querySelector(".textarea-des")
likeone.addEventListener("input",(e) => {
    descriptionColor.style.color = `${e.target.value}`
})
// let UserColor = document.getElementById("UserColor")
// let username = document.getElementById("input-username")
// username.style.color = `${UserColor.value}`
// UserColor.addEventListener("input",(e) => {
//     username.style.color = `${e.target.value}`
// })

const gradientBox = document.querySelector(".gradient-box");
const selectMenu = document.querySelector(".select-box select");
const colorInputs = document.querySelectorAll(".colors input");
const refreshBtn = document.querySelector(".refresh");

const getRandomColor = () => {
    const randomHex = Math.floor(Math.random() * 0xffffff).toString(16);
    return `#${randomHex}`;
}

const generateGradient = (isRandom) => {
    if(isRandom) {
        colorInputs[0].value = getRandomColor();
        colorInputs[1].value = getRandomColor();
    }
    const gradient = `linear-gradient(${selectMenu.value}, ${colorInputs[0].value}, ${colorInputs[1].value})`;
    gradientBox.style.background = gradient;
}



colorInputs.forEach(input => {
    input.addEventListener("input", () => generateGradient(false));
});

selectMenu.addEventListener("change", () => generateGradient(false));
refreshBtn.addEventListener("click", () => generateGradient(true));






document.addEventListener( 'DOMContentLoaded',() => {
    
    let file_input = document.getElementById("file-input")
    let PhotoProfile = document.getElementById("PhotoProfile")
    let backgroundTest = document.getElementById("backgroundTest")
    let backgroundProfile = document.querySelector(".input-backgroundProfile")

    let inputItem = document.getElementById("additem")
    let PhotoItem = document.getElementById("PhotoItem")

    inputItem.addEventListener('change', function(){
        //this refers to file
        const choosedFile = this.files[0];

        if (choosedFile) {

            const reader = new FileReader();
            reader.addEventListener('load', function(){
                PhotoItem.setAttribute('src', reader.result);
            });

            reader.readAsDataURL(choosedFile)
        }
    });
    file_input.addEventListener('change', function(){
        //this refers to file
        const choosedFile = this.files[0];

        if (choosedFile) {

            const reader = new FileReader();
            console.log(reader.result)
            reader.addEventListener('load', function(){
                PhotoProfile.setAttribute('src', reader.result);
            });

            reader.readAsDataURL(choosedFile)
            console.log()
        }
    });
    backgroundProfile.addEventListener('change', function(){
        //this refers to file
        const choosedFile = this.files[0];

        if (choosedFile) {

            const reader = new FileReader();
            reader.addEventListener('load', function(){
                backgroundTest.setAttribute('src', reader.result);
            });

            reader.readAsDataURL(choosedFile)
        }
    });
})

// let file_input = document.getElementById("file-input")
// let PhotoProfile = document.getElementById("PhotoProfile")
// let backgroundTest = document.getElementById("backgroundTest")
// let backgroundProfile = document.querySelector(".input-backgroundProfile")


// file_input.addEventListener('change', function(){
//     //this refers to file
//     const choosedFile = this.files[0];

//     if (choosedFile) {

//         const reader = new FileReader();
//         reader.addEventListener('load', function(){
//             PhotoProfile.setAttribute('src', reader.result);
//         });

//         reader.readAsDataURL(choosedFile)
//         console.log()
//     }
// });
// backgroundProfile.addEventListener('change', function(){
//     //this refers to file
//     const choosedFile = this.files[0];

//     if (choosedFile) {

//         const reader = new FileReader();
//         reader.addEventListener('load', function(){
//             backgroundTest.setAttribute('src', reader.result);
//         });

//         reader.readAsDataURL(choosedFile)
//     }
// });