#!/usr/bin/node
/* Script writes a string to a file */

const fs = require('fs');
const argument = process.argv.slice(2);

fs.writeFile(argument[0], argument[1], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
