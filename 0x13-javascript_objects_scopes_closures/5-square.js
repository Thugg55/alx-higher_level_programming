#!/usr/bin/node
// a class Square that extends from a rectangle class

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
	constructor (size) {
		super(size, size);
	}
}

module.exports = Square;
