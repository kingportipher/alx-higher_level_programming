#!/usr/bin/node
const fs = require('fs');

function writeToFile(filePath, content) {
  fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
      console.error("Error writing to file:", err);
    } else {
      console.log("File written successfully!");
    }
  });
}

// Example usage (assuming Node.js environment)
if (process.argv.length !== 3) {
  console.error("Usage: node writeToFile.js <filepath> <string>");
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

writeToFile(filePath, content);
