#!/usr/bin/node
const num = process.argv[2];

function factorial (num) {
  let answer = 1;

  if (num === 0 || num === 1 || isNaN(num) === true) {
    return answer;
  } else {
    answer = num * factorial(num - 1);
  }
  return (answer);
}

if (process.argv.length < 3) {
  console.log(1);
} else {
  const res = factorial(num);
  console.log(res);
}
