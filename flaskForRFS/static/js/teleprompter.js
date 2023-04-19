$(window).scrollTop(0);

var play = true;
var currentScroll = 0;
var duration
var speed = 80;

var scroller = setInterval(scroll, speed);

function scroll() {
  if(play == true) {
    currentScroll = $(window).scrollTop();
    if($(window).scrollTop() + $(window).height() == $(document).height()) {
      play = false
    } else {
      $(window).scrollTop(currentScroll+1);
      
    }
  }
}

function keyDownTextField(e) {
  var keyCode = e.keyCode;
  if(keyCode==192) {
    event.preventDefault();
    play = !play;
    return false;
  } 
}
document.addEventListener("keydown", keyDownTextField, false);
