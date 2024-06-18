#!/usr/bin/node

const fs = require('fs');

// Function to read contents of a file
function readFile (filePath) {
  return fs.readFileSync(filePath, 'utf8').trim(); // Trim to remove any trailing newline
}

// Command line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read contents of fileA and fileB
const contentA = readFile(fileA);
const contentB = readFile(fileB);

// Concatenate contents of fileA and fileB with a newline in between
const concatenatedContent = `${contentA}\n${contentB}\n`;

// Write concatenated content to fileC
fs.writeFileSync(fileC, concatenatedContent);
