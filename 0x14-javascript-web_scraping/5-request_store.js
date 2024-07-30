#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Get URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both arguments are provided
if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch ${url}. Status code: ${response.statusCode}`);
    return;
  }

  // Write the response body to the file with UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(`Error writing to file: ${err.message}`);
      return;
    }
    console.log(`Content saved to ${filePath}`);
  });
});
