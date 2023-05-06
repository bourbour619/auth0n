$(document).ready(function(){
    $("#profileNav a").each(function(){
        $(this).on("mouseenter", function(){
            $(this).addClass("text-bg-primary rounded-pill")
            $(this).removeClass("link-dark")
        })
        $(this).on("mouseleave", function(){
            $(this).removeClass("text-bg-primary rounded-pill")
            $(this).addClass("link-dark")
        })
    })
});