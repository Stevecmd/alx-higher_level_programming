#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const { results } = JSON.parse(body);

    const count = results.reduce((count, film) => {
      const hasWedgeAntilles = film.characters.find((character) => character.endsWith(`/api/people/${wedgeAntillesId}/`));
      return hasWedgeAntilles ? count + 1 : count;
    }, 0);

    console.log(count);
  }
});
