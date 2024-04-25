#!/usr/bin/node
/* Script gets the contents of a webpage and store it in a file */
const request = require('request');
const args = process.argv.slice(2);
const fs = require('fs');
request(args[0], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    fs.writeFile(args[1], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
