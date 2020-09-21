//highlight active sidenav item
$("#sideLinks div a").click(function() {
    $(this).children().addClass('active').parent().parent().siblings().children().children().removeClass('active');
    $("html, body").animate({ scrollTop: 0 }, 50);
    $(this).children().css({"background-color":"white","color":"black"});
    $(this).children().children().css({"background-color":"white","color":"black"});
});