// HEADER ANIMATION
window.onscroll = function() {scrollFunction()};
var element = document.getElementById("body");
function scrollFunction() {
  if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
      $(".navbar").addClass("fixed-top");
      element.classList.add("header-small");
      $("body").addClass("body-top-padding");

  } else {
      $(".navbar").removeClass("fixed-top");
      element.classList.remove("header-small");
      $("body").removeClass("body-top-padding");
  }
}

// OWL-CAROUSAL for Testimonial
$('.owl-carousel').owlCarousel({
    items: 3,
    loop:true,
    dot:true,
    autoplay: true,
    nav: true,
    navText: [`<img src="../../media_files/media/Vector (5).png">`, `<img  src="../../media_files/media/Vector (4).png">`],
    // navText: [`<img src="../../media_files/media/prev-arrow.png">`, `<img  src="../../media_files/media/next-arrow.png">`],
    slideTransition: 'linear',
    autoplayHoverPause: true,
    // reduce width of the cards
    responsive:{
      0:{
          items:1
      },
      500:{
          items:2
      },
      1300:{
          items:3
      }
  }
})





// active class
$('.owl-dot').click(function () {
  $('.owl-dot').removeClass('active');
  $(this).addClass('active');
});


// SCROLLSPY
$(document).ready(function() {
  $(".nav-link").click(function() {
      var t = $(this).attr("href");
      $("html, body").animate({
          scrollTop: $(t).offset().top - 75
      }, {
          duration: 1000,
      });
      $('body').scrollspy({ target: '.navbar',offset: $(t).offset().top });
      return false;
  });

});

// AOS
AOS.init({
    offset: 120, 
    delay: 0,
    duration: 1200, 
    easing: 'ease', 
    once: true, 
    mirror: false, 
    anchorPlacement: 'top-bottom', 
    disable: "mobile"
  });

//SIDEBAR-OPEN
  $('#navbarSupportedContent').on('hidden.bs.collapse', function () {
    $("body").removeClass("sidebar-open");
  })

  $('#navbarSupportedContent').on('shown.bs.collapse', function () {
    $("body").addClass("sidebar-open");
  })


  window.onresize = function() {
    var w = window.innerWidth;
    if(w>=992) {
      $('body').removeClass('sidebar-open');
      $('#navbarSupportedContent').removeClass('show');
    }
  }