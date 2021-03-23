#!/usr/bin/node
const one = process.argv[2];
const two = process.argv[3];
const res = add(one, two);

function add (a, b) {
  return a + b;
}

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  console.log(res);
}
