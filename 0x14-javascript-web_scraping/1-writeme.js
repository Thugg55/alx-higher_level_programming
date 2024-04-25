#!/usr/bin/node
/* Script writes a string to a file */

const fs = require('fs');

function writeToFileSync(filePath, content) {
    try {
        fs.writeFileSync(filePath, content, 'utf-8');
        console.log("Content successfully written to", filePath);
    } catch (error) {
        console.error("An error occurred while writing to the file:", error);
    }
}

// Check if the correct number of arguments are provided
if (process.argv.length !== 4) {
    console.log("Usage: node script.js <file_path> <string_to_write>");
    process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

writeToFileSync(filePath, content);

