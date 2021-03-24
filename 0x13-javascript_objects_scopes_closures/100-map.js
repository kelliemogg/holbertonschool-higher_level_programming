#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);

const newList = list;
console.log(newList.map(function (currentVal, idx, arr) {
  return (currentVal * idx);
}));
