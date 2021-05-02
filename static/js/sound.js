const soundJudge=function(val){
    if(val){
        document.getElementById('sound-file1').play();
    }else{
        document.getElementById('sound-file2').play();
    }
}