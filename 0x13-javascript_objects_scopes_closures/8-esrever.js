#!/usr/bin/node

exports.esrever = function (list) {
  const RevList = [];
  let i = 0;

  for (i = list.length - 1; i >= 0; i--) {
    RevList.push(list[i]);
  }
  return RevList;
};
