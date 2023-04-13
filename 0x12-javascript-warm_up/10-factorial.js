#!/usr/bin/node

function factorial (a) {
  // for (let i = 0; i < a; i++) { b *= i; } Doesn't work :(
  return (a === 0 || isNaN(a) ? 1 : a * factorial(a - 1));
}

console.log(factorial(parseInt(process.argv[2])));
