#!/usr/bin/node

let i = 2;

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  for (; process.argv[i] !== undefined; i++) {
    console.log(process.argv[i]);
  }
}
