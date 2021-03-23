#!/usr/bin/node
const list = require('./100-data');

let i;
const newList = list.map(x => list[x] * i);

console.log(list);
console.log(newList);
