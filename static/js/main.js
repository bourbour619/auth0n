$(document).ready(function(){
    console.log('*'.repeat(25) + ' Welcome To Auth0n ' + '*'.repeat(25))
    withDelay(function(){
        $("#messages div").each(function(){
            $(this).removeClass("show")
        })
    }, 1000)
});

function withDelay(fn, delay){
    return setTimeout(fn, delay)
}