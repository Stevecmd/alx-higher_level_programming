/* global $ */
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    const header = $('HEADER');
    if (header.css('color') === 'rgb(255, 0, 0)') {
      header.css('color', 'black');
    } else {
      header.css('color', '#FF0000');
    }
  });
});
