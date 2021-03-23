#!/usr/bin/node
const first = process.argv[2];
const second = process.argv[3];

if (process.argv[2] === undefined) {
  console.log(undefined + ' is ' + undefined);
} else {
  console.log(first + ' is ' + second);
}
