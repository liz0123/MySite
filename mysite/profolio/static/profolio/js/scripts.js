$(window).on("load",function(){
    $(".loader-wrapper").fadeOut("slow");
  });

const about_observer = new IntersectionObserver(entries => {
    entries.forEach(entry =>{
        if(entry.isIntersecting){
            document.querySelectorAll(".about")[0].classList.add('fadeInLeft');
            document.querySelectorAll(".about_img")[0].classList.add('fadeInRight');
        }
    })
})

about_observer.observe(document.querySelector(".about-wrapper"));

const project_observer = new IntersectionObserver(entries => {
    entries.forEach(entry =>{
        if(entry.isIntersecting){
            document.querySelectorAll(".section")[0].classList.add('fadeInLeft');
            document.querySelectorAll(".card")[0].classList.add('fadeInDown');
            document.querySelectorAll(".card")[1].classList.add('fadeInDown');
        }
    })
})

project_observer.observe(document.querySelector(".projects-wrapper"));