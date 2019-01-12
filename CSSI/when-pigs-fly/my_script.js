function showWhenClicked() {
    $("#pig").show();
  }

function hideWhenClicked() {
    $("#pig").hide();
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
}
function fly(){
  $("div").animate({
        left: '650px',
        height: '+=450px',
        width: '+=750px',
        top: "750px"
    });



}
$(document).ready(setup);
