#!/usr/bin/node
const sz = process.argv[2];
const x = 'X';
let i;

if (process.argv[2] % 1 !== 0) {
  console.log('Missing size');
} else {
  for (i = 0; i <= sz - 1; i++) {
    console.log(x.repeat(sz));
  }
}
