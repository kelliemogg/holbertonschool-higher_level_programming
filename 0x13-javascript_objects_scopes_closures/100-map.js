#!/usr/bin/node
const list = require('./100-data');

// pass a function to map
let i;
const newList = list.map(x => list[x] * i);
console.log(newList);
