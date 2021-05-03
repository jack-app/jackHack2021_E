let startTime;
let nowTime;
let addTime = 0;
let millisec = 0;
let sec100 = 0;
let sec = 0;
let min = 0;
let timerId;
let stopFlg = false;

$(function(){
    addTime = 0;
    millisec = 0;
    sec100 = 0;
    sec = 0;
    min = 0;
    stopFlg = false;

    console.log("Ho");
    timerId = setTimeout(countUp, 10);
    startTime = new Date().getTime();
    addTime = min*60*1000 + sec*1000 + millisec;
    startTime -= addTime;
    console.log("Hey")
});

    function drawTime(){
        let strTime = "";
        let strSec100, strSec, strMin;
        
        strSec100 = "" + sec100;
        if(strSec100.length < 2){
            strSec100 = "0" + strSec100;
        }
        strSec = "" + sec;
        if(strSec.length < 2){
            strSec = "0" + strSec;
        }
        strMin = "" + min;
        if(strMin.length < 2){
            strMin = "0" + strMin;
        }

        strTime = strMin + ":" + strSec + ":" + strSec100;

        if(stopFlg){
            return strTime;
        }

        $("#timer").html(strTime);
    }

    function countUp(){
        nowTime = new Date().getTime();
        diff = new Date(nowTime - startTime);
        millisec = diff.getMilliseconds();
        sec100 = Math.floor(millisec/10);
        sec = diff.getSeconds();
        min = diff.getMinutes();

        drawTime();
        timerId = setTimeout(countUp, 10);
    }

const stopTimer = function(){
    clearTimeout(timerId);
    stopFlg = true;
    return drawTime();
}