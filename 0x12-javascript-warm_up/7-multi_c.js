#!/usr/bin/node

const content = process.argv[2];
// let word = "C is fun"
let i;

for (i = 0; i < content; i++) {
  console.log('C is fun');
}
if (!parseInt(content)) {
  console.log('Missing number of occurrences');
}
