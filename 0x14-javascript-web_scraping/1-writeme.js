#!/usr/bin/node
const fs = require('fs');

function writeStringToFile(filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log('String has been written to the file successfully!');
    }
  });
}

// Usage: node script.js <file_path> <string_to_write>
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

if (!filePath || !stringToWrite) {
  console.error('Please provide both the file path and the string to write.');
} else {
  writeStringToFile(filePath, stringToWrite);
}
