$(document).ready(function(){
    console.log('*'.repeat(25) + ' Welcome To Auth0n ' + '*'.repeat(25))
    setTimeout(function(){
        $("#messages div").each(function(){
            $(this).removeClass("show")
        })
    }, 2000)
});