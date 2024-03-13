#!/usr/bin/node
// a script that imports an array, computes new array

const { list } = require('./100-data');

const newL = list.map((value, index) => value * index);

console.log(list);
console.log(newL);
