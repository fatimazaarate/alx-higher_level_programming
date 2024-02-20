#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (error, response) => {
  console.log('code: ', response.statusCode);
}).on('error', (error) => {
  console.error(error.message);
});
