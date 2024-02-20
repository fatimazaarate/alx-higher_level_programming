#!/usr/bin/node

const https = require('https');

if (process.argv.length < 3) {
  process.exit(1);
}

const url = process.argv[2];

https.get(url, response => {
  console.log('code: ', response.statusCode);
}).on('error', (myError) => {
  console.error(myError.message);
});
