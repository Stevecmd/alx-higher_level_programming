#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }
  request.get(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(characters, index + 1);
    }
  });
}
