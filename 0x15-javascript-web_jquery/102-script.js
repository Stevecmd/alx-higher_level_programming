/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
