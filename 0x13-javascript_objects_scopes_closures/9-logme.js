#!/usr/bin/node

let ArgNum = 0;
exports.logMe = function (item) {
  ArgNum++;
  console.log(ArgNum - 1 + ': ' + item);
};
