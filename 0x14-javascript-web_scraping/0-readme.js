#!/usr/bin/node

#!/usr/bin/env node

const fs = require('fs');
const process = require('process');

// Retrieve the file path from the command line arguments
const filePath = process.argv[2];

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        // Print the error object if an error occurred
        console.error(err);
    } else {
        // Print the content of the file
        console.log(data);
    }
});
