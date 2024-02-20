#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const parse = JSON.parse(body);
  const filmTitle = parse.title;
  console.log(filmTitle);
});
