
var startTime;

function showClickMe(){
  $("p").show();
  startTime = new Date();
}

function showReactionTime(){
  var endTime = new Date();
  window.alert(
    "It took you "+ ((endTime.getTime() - startTime.getTime())/1000)
     + "seconds to click")
}

function setup(){
  $("p").hide();
  setTimeout(
    showClickMe,
    (Math.random()*9+1)*1000);
  $("p").on("click",
    showReactionTime);
}

$(document).ready(setup);
