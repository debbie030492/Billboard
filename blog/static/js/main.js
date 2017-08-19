

$('document').ready(function(){
   $('.form').hide();
   $('.checking').hide();

    $(".plus").click(function(){
    $('.adding').hide();
    $('.form').show();
    $('.checking').show();
    //$('.post-new-cont').show();
    });

    $(".sign1") .click(function(){
        //$('.post-new-cont').hide();
        $('.form').hide();
        $('.checking').hide();
        $('.adding').show();
    });


});