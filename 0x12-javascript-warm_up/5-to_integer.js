#!/usr/bin/node
const numb = process.argv[2];

if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (process.argv[2] % 1 !== 0) {
  console.log('Not a number');
} else if (process.argv[2] % 1 === 0) {
  console.log('My number: ' + numb);
}
