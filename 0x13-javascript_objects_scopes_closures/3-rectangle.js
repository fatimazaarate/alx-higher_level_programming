#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '' /* empty str */
      for (let j = 0; j < this.weight; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;
