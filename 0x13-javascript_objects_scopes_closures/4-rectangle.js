#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const x = 'X';
    for (let i = 1; i <= this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }

  rotate () {
    const wide = this.width;
    const tall = this.height;
    this.width = tall;
    this.height = wide;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
