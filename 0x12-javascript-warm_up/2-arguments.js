#!/usr/bin/node
// prints a message based on the number of arguments

let myVar;
for (myVar in process.argv) {
}
myVar--;
if (myVar === 0)
	console.log('No argument');
if (myVar === 1)
	console.log('Argument found');
if (myVar > 1)
	console.log('Arguments found');
