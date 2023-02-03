(function() {
    'use strict';

    /*Carousel function*/
    function animateLoadingBar(animatedElem, transform, opacity) {
        animatedElem.css({
            "opacity": opacity,
            "transform": "translate3d(" + transform + "%,0,0)",
            "-webkit-transform": "translate3d(" + transform + "%,0,0)"
        })
    }


    if ($(".carousel").length) {
        $(".carousel").each(function() {
            var thisCarousel = $(this);

            var loadingBar = '<div class="loading-bar-wrapper">';
            loadingBar += '<div class="loading-bar-animate">';
            loadingBar += '</div>';
            loadingBar += '</div>';

            thisCarousel.find(".carousel-item").append(loadingBar);

            thisCarousel.find(".carousel-item").each(function() {
                var dataInterval = $(this).data("interval");

                $(this).find(".loading-bar-animate").css({
                    "transition-duration": dataInterval + "ms",
                    "-webkit-transition-duration": dataInterval + "ms"
                });
            });

            $(window).on("load", function() {
                var firstInterval = thisCarousel.find(".carousel-item.active").data("interval");
                animateLoadingBar(thisCarousel.find(".carousel-item.active").find(".loading-bar-animate"), 0, 1)

                thisCarousel.carousel({
                    ride: "autoplay",
                    interval: firstInterval
                })
            });
            thisCarousel.on("slid.bs.carousel", function(e) {
                animateLoadingBar($(this).find(".carousel-item").find(".loading-bar-animate"), -100, 0);
                animateLoadingBar($(e.relatedTarget).find(".loading-bar-animate"), 0, 1);
            });

        });
    }



    /*Portfolio gallery filter and Lightbox*/


    $('.list').click(function() {

        const value = $(this).attr('data-filter');
        // ^ this ties the '.list' class to a data-filter, ("data-filter", "value of list") 
        //   based on its value 
        if (value == 'all') {
            $('.imageBox').show('1000');
        } else {
            $('.imageBox').not('.' + value).hide('1000');
            //$('.mySlides').not('.' + value).removeClass('active');
            $('.imageBox').filter('.' + value).show('1000');
            // $('.mySlides').not('.' + value).addClass('active');
        }

    });


    $('.list').click(function() {
        $(this).addClass('active').siblings().removeClass('active')
    });


    // define all UI variable
    const navToggler = document.querySelector('.nav-toggler');
    const navMenu = document.querySelector('.site-navbar ul');
    const navLinks = document.querySelectorAll('.site-navbar a');

    // load all event listners
    allEventListners();

    // functions of all event listners
    function allEventListners() {
        // toggler icon click event
        navToggler.addEventListener('click', togglerClick);
        // nav links click event
        navLinks.forEach(elem => elem.addEventListener('click', navLinkClick));
    }

    // togglerClick function
    function togglerClick() {
        navToggler.classList.toggle('toggler-open');
        navMenu.classList.toggle('open');
    }

    // navLinkClick function
    function navLinkClick() {
        if (navMenu.classList.contains('open')) {
            navToggler.click();
        }
    }



})(jQuery);