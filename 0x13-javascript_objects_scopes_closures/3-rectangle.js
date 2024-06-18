#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      // Create an empty object if w or h is not a positive integer
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
