$( document ).ready(function() {
  var leftPos = 0;
  var move = function() {
    $("div.courrier img").css("left", leftPos+'px');
    leftPos += $("div.courrier img").width() + 1;
    if( leftPos > $( document).width() - $("div.courrier img").width() ) {
      leftPos = 0;
    }
    setTimeout( move, 1000);
  }
  move();
});
