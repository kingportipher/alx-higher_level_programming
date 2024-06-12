$(document).ready(function() {
  // When the user clicks on the DIV with id "DIV#red_header"
  $('DIV#red_header').click(function() {
    // Update the text color of the <header> element to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});
