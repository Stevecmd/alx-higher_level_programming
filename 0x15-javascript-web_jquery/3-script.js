/* global $ */
$('DIV#red_header').click(() => {
  const header = $('HEADER');
  if (header.css('color') === 'rgb(255, 0, 0)') { // red
    header.css('color', 'black');
  } else {
    header.css('color', '#FF0000'); // red
  }
});
