#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
