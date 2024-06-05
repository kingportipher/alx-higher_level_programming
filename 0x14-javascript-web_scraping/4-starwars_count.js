#!/usr/bin/node
const request = require('request');
const process = require('process');

// Retrieve the API URL from the command line arguments
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve films: ${response.statusCode}`);
    return;
  }

  const results = JSON.parse(body).results;
  const count = results.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/')) ? count + 1 : count;
  }, 0);

  console.log(count);
});
