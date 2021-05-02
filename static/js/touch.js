$(function(){
    $("#imageArea").on('click', function(e) {
        console.log(point);
        console.log("座標" + e.offsetX + "," + e.offsetY);
    });
});
