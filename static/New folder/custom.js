
  $(function () {

    // MENU
    $('.navbar-collapse a').on('click',function(){
      $(".navbar-collapse").collapse('hide');
    });

    // AOS ANIMATION
    AOS.init({
      disable: 'mobile',
      duration: 800,
      anchorPlacement: 'center-bottom'
    });


      $(document).ready(function(){
        $('.content').click(function(){
          $('.content').toggleClass("heart-active")
          $('.text').toggleClass("heart-active")
          $('.numb').toggleClass("heart-active")
          $('.heart').toggleClass("heart-active")
        });
      });
      $(document).ready(function(){
        $('.con').click(function(){
          $('.con').toggleClass("hear-active")
          $('.tex').toggleClass("hear-active")
          $('.num').toggleClass("hear-active")
          $('.hear').toggleClass("hear-active")
        });
      });
      
      $(document).ready(function(){
        $('.co').click(function(){
          $('.co').toggleClass("hea-active")
          $('.te').toggleClass("hea-active")
          $('.nu').toggleClass("hea-active")
          $('.hea').toggleClass("hea-active")
        });
      });
    
    // SMOOTHSCROLL NAVBAR
    $(function() {
      $('.navbar a, .hero-text a').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 49
        }, 1000);
        event.preventDefault();
      });
    });    
  });

  
