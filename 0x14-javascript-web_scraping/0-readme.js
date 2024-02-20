#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
