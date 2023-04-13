#!/usr/bin/node

const content = process.argv[2];
let i;
let j = 0;
let square = '';

for (i = 0; i < content; i++) {
  // for (j = 0; j < content; j++) {
  while (j < content) {
    square = square + 'X';
    j++;
  }
  console.log(square);
}
if (!parseInt(content)) {
  console.log('Missing size');
}
