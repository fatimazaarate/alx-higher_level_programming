#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const parsedData = JSON.parse(body);

  const film = parsedData.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );
  if (film.length > 0) {
    console.log(film.length);
  }
  else {
    console.error(error);
  }
});
