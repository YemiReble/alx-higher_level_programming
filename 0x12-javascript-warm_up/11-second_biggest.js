#!/usr/bin/node

const arg = process.argv.slice(2).map(Number);
arg.sort((a, b) => a - b);
console.log(arg[arg.length - 2] || 0);
