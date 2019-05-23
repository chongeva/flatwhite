$(document).ready(function(){
    // When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        console.log();
        if ($(document).scrollTop() > 80) {
            $(".navbar").addClass('navbar-shrink');
            $(".navbar").addClass('bg-dark');
        } else {
            $(".navbar").removeClass('navbar-shrink');
            $(".navbar").removeClass('bg-dark');
        }
    }

    scrollFunction();

    $(".responsive-embed").each(function(){
        $(this).fitVids();
    });

    $(document).on('click', '[data-toggle="lightbox"]', function(event) {
        event.preventDefault();
        $(this).ekkoLightbox();
    });
});
