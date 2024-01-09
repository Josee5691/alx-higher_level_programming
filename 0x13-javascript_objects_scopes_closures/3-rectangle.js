#!/usr/bin/node
module.exports = class Rectangle {
  costructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height) {
      console.log('X'.repeat(this.width));
    }
  }
};
