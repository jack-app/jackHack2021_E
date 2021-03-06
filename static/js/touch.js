$(function(){
    let cancelFlg = true;

    const areaWidth = $("#hideImage").width();
    $(".main-modal-mask").width(areaWidth);
    const areaHeight = $("#hideImage").height();
    $(".main-modal-mask").height(areaHeight);

    const areaOffsetTop = $("#hideImage").offset().top;
    const areaOffsetLeft = $("#hideImage").offset().left;
    $(".main-modal-mask").offset({ top: areaOffsetTop, left: areaOffsetLeft });

    $("#hideImage").on('click', function(e) {
        console.log("座標" + e.offsetX + "," + e.offsetY);
        console.log("答え" + answer_area_x + "," + answer_area_y);

        if(cancelFlg){
            cancelFlg = false;
            let minX = answer_area_x[0];
            let maxX = answer_area_x[1];
            let minY = answer_area_y[0];
            let maxY = answer_area_y[1];

            if(e.offsetX < minX || e.offsetX > maxX){
                soundJudge(false);
                $(".main-modal-mask").show();
                // 3秒間入力不可
                setTimeout(()=>{
                    cancelFlg = true;
                    $(".main-modal-mask").hide();
                }, 2500);
                return
            }

            if(e.offsetY < minY || e.offsetY > maxY){
                soundJudge(false);
                $(".main-modal-mask").show();
                // 3秒間入力不可
                setTimeout(()=>{
                    cancelFlg = true;
                    $(".main-modal-mask").hide();
                }, 2500);
                return
            }

            const timeResult = stopTimer();
            console.log("result=>"+timeResult);
            soundJudge(true);
            setTimeout(()=>{
                window.location.href = '/result?time_result='+timeResult;
                // $.ajax({
                //     url: '/result?time_result='+timeResult,
                //     type: 'POST',
                //     // data: {time_result: timeResult}
                // });
            }, 1500);
        }
    });
});

    //     if 'file' not in request.files:
    //         flash('ファイルがありません')
    //         return redirect(request.url)
        
    //     if file.filename == '':
    //         flash('ファイルがありません')
    //         return redirect(request.url)

