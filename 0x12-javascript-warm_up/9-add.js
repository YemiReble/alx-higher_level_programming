#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const val = process.argv;

console.log(add(parseInt(val[2]), parseInt(val[3])));
