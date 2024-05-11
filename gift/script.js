
document.addEventListener("DOMContentLoaded", function(event) {
    var query_string = window.location.search;
    var url_params = new URLSearchParams(query_string);
    var code = url_params.get('code');
    var gift_box = document.getElementById("gift_box");

    function redirect(){
        window.location.href = "https://www.samila.site"
    }
    
    function ipfs_url(cid){
        return "https://cloudflare-ipfs.com/ipfs/" + cid;
    }

    if (samila_gift_data.hasOwnProperty(code)){
        document.getElementById("gift_code").innerHTML = 1000 + parseInt(code);
        document.getElementById("gift_owner").innerHTML = samila_gift_data[code]["owner"];
        document.getElementById("gift_date").innerHTML = samila_gift_data[code]["date"];
        document.getElementById("gift_version").innerHTML = samila_gift_data[code]["version"];
        document.getElementById("gift_image_link").href = ipfs_url(samila_gift_data[code]["image_cid"]);
        document.getElementById("gift_config_link").href = ipfs_url(samila_gift_data[code]["config_cid"]);
        gift_box.style.display = "inline-block";
        document.getElementById("gift_image").src = ipfs_url(samila_gift_data[code]["image_cid"]);
    }
    else{
        gift_box.innerHTML = "Wrong code!<br/><br/>&nbsp;Redirecting ...";
        gift_box.style.display = "inline-block";
        setTimeout(redirect, 4500);
    }
});

