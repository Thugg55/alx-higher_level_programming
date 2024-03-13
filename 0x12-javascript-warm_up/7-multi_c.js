#!/usr/bin/node
// Script prints x times "C is fun"

let i = 0;
const { argv } = require('process');

if (argv[2] === undefined) { console.log('Missing number of occurrences'); } else {
  for (i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}
