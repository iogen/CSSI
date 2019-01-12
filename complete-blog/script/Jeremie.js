window.alert ("Welcome to Jeremie's Life");

function showWhenClicked() {
    $(".flag").show();
  }

  function hideWhenClicked() {
    $(".flag").hide();
}

function setup() {
    $("#showflag").click(showWhenClicked);
    $("#hideflag").click(hideWhenClicked);

$(document).ready(setup);
