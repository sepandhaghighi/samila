
function range(size) {
    return [...Array(size).keys()].map(i => (i+1) + '.jpg');
}

function ready(callback){
    if (document.readyState!='loading') callback();
    else if (document.addEventListener) document.addEventListener('DOMContentLoaded', callback);
    else document.attachEvent('onreadystatechange', function(){
        if (document.readyState=='complete') callback();
    });
}

var backgrounds = range(15);

function redirect(flag){
    switch(flag){
        case 1:
            window.open("https://gitcoin.co/grants/3915/samila-generative-art-generator");
            break;
        case 2:
            window.open("https://www.samila.site/wallets.html");
            break;
        case 3:
            window.open("https://www.coffeete.ir/opensource");
            break;
        default:
            window.open("https://gitcoin.co/grants/3915/samila-generative-art-generator");
            
    }
    
}

function change_bg(){
    var random_index
    random_index = Math.floor(Math.random() * backgrounds.length)
    random_image = backgrounds[random_index]
    var s = document.getElementsByClassName('siteWrapper')
    s[0].style.background = `url('images/backgrounds/${random_image}') repeat center center`
}

ready(function(){
    change_bg();
});

