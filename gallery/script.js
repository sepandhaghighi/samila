const image_error_url = '../images/image_error.png';
var mydata = JSON.parse(data);

function ready(callback) {
    if (document.readyState != 'loading') callback();
    else if (document.addEventListener) document.addEventListener('DOMContentLoaded', callback);
    else document.attachEvent('onreadystatechange', function() {
        if (document.readyState == 'complete') callback();
    });
}

function image_error(obj, id_number){
    obj.src = image_error_url;
    let desc = document.getElementById(`desc${id_number}`)
    desc.innerHTML = `<i class="fa fa-refresh fa-lg refresh" aria-hidden="true" onclick="refresh(${id_number});"></i>`;
}

function ipfs_link(ipfs_id) {
    return "https://ipfs.io/ipfs/" + ipfs_id
}

function refresh(id_number) {
    let img = document.getElementById(`img${id_number}`)
    img.src = ipfs_link(mydata[mydata.length - id_number]["link"])
    let desc = document.getElementById(`desc${id_number}`)
    desc.innerHTML = id_number;
}


var template = `
<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="{{link}}">
      <img id="img{{number1}}" src="{{link}}" alt="{{number1}}" width="300" height="300" loading="lazy" onerror="image_error(this, {{number1}});">
    </a>
    <div class="desc" id="desc{{number1}}">{{number1}}</div>
  </div>
</div>
`

function fill_template(img_number, img_link) {
    var temp = template;
    for (let i = 0; i < 6; i++) {
        temp = temp.replace("{{number1}}", img_number).replace("{{link}}", img_link)
    }
    return temp
}

function run() {
    for (let i = 0; i < mydata.length; i++) {
        document.body.innerHTML += fill_template(parseInt(mydata[i]["number"]), ipfs_link(mydata[i]["link"]))

    }

}
ready(function() {
    run();
});