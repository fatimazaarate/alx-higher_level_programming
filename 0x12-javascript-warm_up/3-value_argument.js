#!/usr/bin/node

let i = 2;

if (process.argv.length < 3) {
  console.log('No argument');
} else {
  while (i < process.argv.length) {
    console.log(process.argv[i]);
    i++;
  }
}
