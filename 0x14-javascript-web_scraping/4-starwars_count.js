#!/usr/bin/node
/* Script print the number of movies where the character "Wedge Antiles" presen
 * first argument is the API URL of the Star wars API
 */
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const res in data) {
      const characters = data[res].characters;
      for (const id in characters) {
        if (characters[id].includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
