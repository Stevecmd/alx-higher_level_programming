#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  if (characters.length === 0) {
    console.log('No characters found.');
    return;
  }
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}
