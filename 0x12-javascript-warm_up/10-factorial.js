#!/usr/bin/node
const num = process.argv[2];

function factorial (num) {
  let answer = 1;
  let i;

  if (num === 0 || num === 1) {
    return answer;
  } else {
    for (i = num; i >= 1; i--) {
      answer = answer * i;
    }
    return (answer);
  }
}

if (process.argv.length < 3) {
  console.log(1);
} else {
  const res = factorial(num);
  console.log(res);
}
