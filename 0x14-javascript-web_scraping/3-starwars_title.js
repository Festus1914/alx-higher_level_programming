#!/usr/bin/node
const request = require('request');

// Function to fetch the movie details from the Star Wars API
function fetchMovieDetails(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode !== 200) {
        console.error('API returned non-200 status:', response.statusCode);
      } else {
        const movieData = JSON.parse(body);
        const movieTitle = movieData.title;
        console.log(`Star Wars Episode ${movieData.episode_id}: ${movieTitle}`);
      }
    }
  });
}

// Check if a valid movie ID was provided as an argument
const args = process.argv.slice(2);
if (args.length !== 1 || isNaN(args[0])) {
  console.error('Please provide a valid movie ID (episode number).');
  process.exit(1);
}

const movieId = parseInt(args[0]);

// Fetch the movie details and print the title
fetchMovieDetails(movieId);
