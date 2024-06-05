#!/usr/bin/node
const request = require('request');
const process = require('process');

// Retrieve the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the API URL with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
    if (error) {
        // Print the error object if an error occurred
        console.error('Error:', error);
        return;
    }

    // Check for successful response
    if (response.statusCode === 200) {
        // Parse the response body
        const movie = JSON.parse(body);
        // Print the title of the movie
        console.log(movie.title);
    } else {
        // Print an error message if the movie is not found
        console.error(`Failed to retrieve movie: ${response.statusCode}`);
    }
});
