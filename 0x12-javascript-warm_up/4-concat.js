#!/usr/bin/node

const arg = process.argv;
if (arg[2] && arg[3]) {
  console.log(arg[2] + ' is ' + arg[3]);
}
// if (arg[2] === undefined && arg[3] === undefined) {
// console.log(arg[2] + ' is ' + arg[3]);
// }
if (arg[2] === undefined || arg[3] === undefined) {
  console.log(arg[2] + ' is ' + arg[3]);
}
