$(document).ready(function(){
    $("#profileNav > li > a").each(function(){
        $(this).on("mouseenter", function(){
            $(this).addClass("text-bg-primary")
            $(this).addClass("rounded")
            $(this).removeClass("link-dark")
        })
        $(this).on("mouseleave", function(){
            if(!$(this).hasClass('active')){
                $(this).removeClass("text-bg-primary")
                $(this).removeClass("rounded")
                $(this).addClass("link-dark")
            }
        })
    })
});