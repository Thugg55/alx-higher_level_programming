#!/usr/bin/node
/*
 * Script prints the tiltle of a Star Wars movie 
 * first argument is the movie ID
 */
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
