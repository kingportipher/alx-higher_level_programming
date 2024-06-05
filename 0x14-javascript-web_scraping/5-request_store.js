#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const process = require('process');

// Retrieve the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the URL and store the response body in the specified file
request(url)
    .on('error', (err) => {
        console.error('Error making request:', err);
    })
    .pipe(fs.createWriteStream(filePath, { encoding: 'utf8' }))
    .on('error', (err) => {
        console.error('Error writing to file:', err);
    })
    .on('finish', () => {
        console.log(`Successfully saved the content to ${filePath}`);
    });

