#!/usr/bin/node

const args1 = process.argv[2];
const args2 = process.argv[3];

if (args1 === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
