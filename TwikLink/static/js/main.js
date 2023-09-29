gsap.registerPlugin(ScrollTrigger);


let likeNav = document.querySelector(".likeNav")
let backgroundShare =  document.querySelector(".background-share")
let BoxShare = document.querySelector(".Box-share")
let buttonDots =  document.getElementById("buttonDots")
let buttonClose = document.querySelector(".btn-close")
let section = document.getElementById("section")
buttonClose.addEventListener("click",() => {
    gsap.to(backgroundShare,.2,{
        opacity:0,display:"none",ease:"back.out(1.7)",
    })
    gsap.to(BoxShare,.2,{
        opacity:0,ease:"back.out(1.7)",display:"none"
        
    })
})
buttonDots.addEventListener("click",() => {
    gsap.to(backgroundShare,.2,{
        display:"flex",opacity:1,ease:"back.out(1.7)"
    })
    gsap.to(BoxShare,.2,{
        display:"flex",opacity:1,ease:"back.out(1.7)",
        
    })
})
backgroundShare.addEventListener("click",() => {
    gsap.to(backgroundShare,.2,{
        opacity:0,display:"none",ease:"back.out(1.7)",
    })
    gsap.to(BoxShare,.2,{
        opacity:0,ease:"back.out(1.7)",display:"none"
        
    })
    
})
window.addEventListener("scroll", () => {
    if (window.scrollY <= 100) {
        gsap.to(likeNav,.8,{scrollTrigger:{
            trigger: "#section", 
            // scrub: .5, 
            start: "+=200 +=100",
            end:"+=300 +=100 "  
        },backgroundColor:"rgba( 255, 255, 255, 0.5 )",backdropFilter:"blur(4px)",ease:"back.out(1.7)"})
        gsap.to(".likeNav > img",.8,{scrollTrigger:{
            trigger: "#section", 
            // scrub: .5, 
            start: "+=200 +=100",
            end:"+=300 +=100 " 
        },opacity: 1,ease:"back.out(1.7)"
        })
        gsap.to(".likeNav > h3",.8,{scrollTrigger:{
            trigger: "#section",
            // scrub: .5,
            start: "+=200 +=100",
            end:"+=300 +=100 "
        },opacity: 1,ease:"back.out(1.7)"
        })

    }else if(window.screenY == 0){
        gsap.set(likeNav,.8,{scrollTrigger:{
            trigger: "#section", 
            // scrub: .5, 
            start: "+=200 +=100",
            end:"+=300 +=100 "  
        },backgroundColor:"rgba( 255, 255, 255, 0 )",backdropFilter:"blur(0px)",ease:"back.out(1.7)"})
        gsap.set(".likeNav > img",.8,{scrollTrigger:{
            trigger: "#section", 
            // scrub: .5, 
            start: "+=200 +=100",
            end:"+=300 +=100 " 
        },opacity: 0,ease:"back.out(1.7)"
        })
        gsap.set(".likeNav > h3",.8,{scrollTrigger:{
            trigger: "#section",
            // scrub: .5,
            start: "+=200 +=100",
            end:"+=300 +=100 "
        },opacity: 0,ease:"back.out(1.7)"
        })
    }
    gsap.to(backgroundShare,.2,{
        opacity:0,display:"none",ease:"back.out(1.7)",
    })
    gsap.to(BoxShare,.2,{
        opacity:0,ease:"back.out(1.7)",display:"none"
        
    })
})

let one = new ClipboardJS('.btn-copy');

let two = new ClipboardJS('.Box-Copy',{
    text: function () {
        document.querySelector(".btn-copy").textContent = "Copied!"
        document.querySelector(".btn-copy").style.color = "#5cb571"
        setTimeout(()=> {
            document.querySelector(".btn-copy").textContent = "Copy!"
            document.querySelector(".btn-copy").style.color = "#000000"
        },1000)
        return document.querySelector(".btn-copy").getAttribute("data-clipboard-text");
    },
});


let three = new ClipboardJS('#btn-getlink',{
    text: (e) => {
        return e.previousElementSibling.getAttribute("href")
    }
});
