// new Splide( '.splide' ).mount( window.splide.Extensions )
// const splide = new Splide( '.splide', {
//     type   : 'loop',
//     drag   : 'free',
//     focus  : 'center',
//     perPage: 3,
//     autoScroll: {
//         speed: 1,
//     },
// } );

// splide.mount();
// console.log(splide)

const splide = new Splide( '.splide', {
    type   : 'loop',
    drag   : false,
    focus  : 'center',
    perPage: 5,
    height: '100%',
    // width:'100%',
    direction   : 'ttb',
    transition: 'fade',
    gap:'15px',
    // lazyLoad:'sequential',
    arrows: false,
    pagination: false,
    autoScroll: {
        speed: 1,
        pauseOnHover:false,
    },
    breakpoints:{
        1150:{
            direction   : 'ltr',
            height:'auto',
            width:'100%',
        },
        938:{
            perPage: 4,
            height:'auto',
            width:'100%',
        },
        743:{
            perPage: 3,
            height:'auto',
            width:'100%',

        },
        563:{
            perPage: 2,
            height:'auto',
            width:'100%',
        },
        380:{
            perPage: 1,
            height:'auto',
            width:'100%',
        }
    }
} );

const splidex = new Splide( '.splide.two', {
    type   : 'loop',
    drag   : false,
    focus  : 'center',
    perPage: 5,
    direction   : 'ttb',
    height: '100%',
    gap:'15px',
    transition: 'fade',
    // lazyLoad:'sequential',
    pagination: false,
    arrows: false,
    autoScroll: {
        speed: -1,
        pauseOnHover:false,
    },
    breakpoints:{
        1150:{
            direction   : 'ltr',
            height:'auto',
            width:'100%',
        },
        938:{
            perPage: 4,
            height:'auto',
            width:'100%',
        },
        743:{
            perPage: 3,
            height:'auto',
            width:'100%',
        },
        563:{
            perPage: 2,
            height:'auto',
            width:'100%',
        },
        380:{
            perPage: 1,
            height:'auto',
            width:'100%',
        }
    }
} );

document.addEventListener( 'DOMContentLoaded',() => {
    splide.mount(window.splide.Extensions);
    splidex.mount(window.splide.Extensions);
})
