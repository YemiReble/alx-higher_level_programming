// Using the JQuery API to colour the header tag

$(document).ready(function () {
  $('#red_header').on('click', function () {
    $('header').css('color', 'red');
  });
});
