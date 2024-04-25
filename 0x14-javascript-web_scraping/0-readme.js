#!/usr/bin/node
/* Script reads and prints the content of a file */

const fs = require('fs');
const filePath = process.argv[2];

function readFile(filePath) {
    fs.readFile(filePath, 'utf-8', (err, data) => {
        if (err) {
            console.error("An error occurred while reading the file:");
            console.error(err);
            return;
        }
        console.log(data);
    });
}

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <file_path>");
} else {
    readFile(filePath);
}

