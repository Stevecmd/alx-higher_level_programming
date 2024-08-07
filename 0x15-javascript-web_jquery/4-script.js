/* global $ */
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    const header = $('HEADER');
    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else {
      header.removeClass('green').addClass('red');
    }
  });
});
