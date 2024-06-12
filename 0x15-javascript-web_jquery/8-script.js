$(document).ready(function() {
  // URL to fetch the list of movies
  let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Fetch the list of movies using jQuery's get method
  $.get(url, function(data, status) {
    // Loop through each movie in the results
    data.results.forEach(function(movie) {
      // Create a new list item with the movie title
      let listItem = '<li>' + movie.title + '</li>';
      // Append the list item to the UL with id "list_movies"
      $('UL#list_movies').append(listItem);
    });
  });
});

