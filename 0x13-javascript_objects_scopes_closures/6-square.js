#!/usr/bin/node
// a class Square that inherits from 5-square.js

class Square extends require('./5-square.js') {
	charPrint(c) {
		if ( c === undefined) {
			this.print();
		}
		else {
			for (let x = 0; i < this.height; i++)
				console.log(c.repeat(this.width));
		}
	}
};
