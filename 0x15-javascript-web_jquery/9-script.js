$(document).ready(function() {
  // URL to fetch the translation of "hello" in French
  let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Fetch the translation using jQuery's get method
  $.get(url, function(data) {
    // Update the text of the DIV with id "hello" with the fetched translation
    $('#hello').text(data.hello);
  });
});

