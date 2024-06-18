#!/usr/bin/node

const fs = require('fs');
const path = require('path');

// Function to read contents of a file
function readFile (filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

// Command line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read contents of fileA and fileB
const contentA = readFile(fileA);
const contentB = readFile(fileB);

// Concatenate contents of fileA and fileB
// const concatenatedContent = contentA + contentB;
const concatenatedContent = contentA.trim() + '\n' + contentB.trim() + '\n';

// Write concatenated content to fileC
fs.writeFileSync(fileC, concatenatedContent);

// console.log(`Concatenation successful. Output written to ${fileC}`);
