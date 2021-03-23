#!/usr/bin/node
const one = process.argv[2];
const two = process.argv[3];

function add (one, two) {
  return parseInt(one) + parseInt(two);
}

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  const res = add(one, two);
  console.log(res);
}
