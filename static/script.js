$( document ).ready(function() {
  function move() {
    $('#courrier').css("left", pos);
    right = parseInt( $("#courrier").css("left") );
    console.log( right );
    if( pos === 0 ) {
      pos = 10;
      timeout = 500;
    }
    else if( pos < endRoute ) {
      if( right < farm1 ) {
        pos = parseInt( $('#courrier').css("left") ) + step;
        timeout = 100;
      } else if( right < (farm1 + 150) ) {
        pos = parseInt( $('#courrier').css("left") ) + 180;
        setTimeout( function() {
          $('#courrier').attr("src", "static/img/bikecourrier1.gif");
        }, 250);
        timeout = 500;
      } else {
        if( right < farm2 ) {
          pos = parseInt( $('#courrier').css("left") ) + step;
          timeout = 100;
        } else if( right < (farm2 + 150) ) {
          pos = parseInt( $('#courrier').css("left") ) + 180;
          setTimeout( function() {
            $('#courrier').attr("src", "static/img/bikecourrier2.gif");
          }, 250);
          timeout = 500;
        } else {
          pos = parseInt( $('#courrier').css("left") ) + step;
          timeout = 100;
        }
      }
	  } else {
      pos = 0
      setTimeout( function() {
        $('#courrier').attr("src", "static/img/bikecourrier0.gif");
      }, 500);
      timeout = 1000;
    }
    setTimeout( move, timeout);
  }
  var step = 10;
  var pos = 0;
  var farm1 = parseInt( $("#farm1").css("left") ) - parseInt( $("#courrier").width() );
  var farm2 = parseInt( $("#farm2").css("left") );
  var endRoute = parseInt( $("#woman").css("left") ) + parseInt( $("#courrier").width() );
  var timeout = 100;
  move();
});
