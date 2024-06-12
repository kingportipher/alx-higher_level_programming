// Fetch the translation using jQuery's get method

let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data, stat) {
  $('DIV#character').text(data.name);
});
