#!/usr/bin/node
/* Script gets the contents of a webpage and store it in a file */
const fs = require('fs');
const request = require('request');

function saveWebPage(url, filePath) {
    request(url, (error, response, body) => {
        if (error) {
            console.error("Error:", error);
            return;
        }
        if (response.statusCode !== 200) {
            console.error(`Error: HTTP status code ${response.statusCode}`);
            return;
        }
        fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
            if (err) {
                console.error("Error writing file:", err);
            } else {
                console.log(`Webpage content saved to ${filePath}`);
            }
        });
    });
}

if (process.argv.length !== 4) {
    console.error("Usage: node script.js <URL> <file_path>");
    process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];
saveWebPage(url, filePath);

