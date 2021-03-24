#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else if (process.argv.length > 3) {
  const list = [];
  for (let i = 2; i < process.argv.length; i++) {
    list.push(process.argv[i]);
  }
  list.sort((a, b) => b - a);
  console.log(list[1]);
}
