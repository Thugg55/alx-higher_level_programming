#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

const valueA = fs.readFileSync(`./${argv[2]}`);
const valueB = fs.readFileSync(`./${argv[3]}`);
fs.writeFileSync(`./${argv[4]}`, `${valueA}${valueB}`);
