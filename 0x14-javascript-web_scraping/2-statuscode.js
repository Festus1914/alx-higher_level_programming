#!/usr/bin/node
// Import the 'request' module
const request = require('request');

// Get the URL from the command line argument
const url = process.argv[2];

// Make the GET request
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    console.log('code:', response.statusCode);
  }
});
