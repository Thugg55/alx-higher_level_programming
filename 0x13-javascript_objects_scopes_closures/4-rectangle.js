#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      object.create(null);
    }
  }

  // print(), a method that prints in form of X
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // rotate (), a method that exchanges the width and the height
  rotate () {
    const rot = this.width;
    this.width = this.height;
    thi.height = rot;
  }

  // double (), a method that multiples the widthe and height by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
