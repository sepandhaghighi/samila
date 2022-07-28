function ready(callback) {
    if (document.readyState != 'loading') callback();
    else if (document.addEventListener) document.addEventListener('DOMContentLoaded', callback);
    else document.attachEvent('onreadystatechange', function() {
        if (document.readyState == 'complete') callback();
    });
}

function ipfs_link(input_id) {
    return "https://ipfs.io/ipfs/" + input_id
}

var mydata = JSON.parse(data);

var template = `
<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="{{link}}">
      <img src="{{link}}" alt="{{number1}}" width="300" height="300">
    </a>
    <div class="desc">{{number1}}</div>
  </div>
</div>
`

function fill_template(img_number, img_link) {
    var temp = template;
    for (let i = 0; i < 2; i++) {
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