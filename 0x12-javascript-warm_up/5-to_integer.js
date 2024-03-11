#!/usr/bin/node
// Script prints my number

const mynum = Math.floor(Number(process.argv[2]));
console.log(isNaN(mynum) ? 'Not a number' : 'My number: ${mynum}');
