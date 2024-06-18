#!/usr/bin/node
const fs = require('fs');

// Reading the contents of fileA and fileB
const contentA = fs.readFileSync(process.argv[2]).toString();
const contentB = fs.readFileSync(process.argv[3]).toString();

// Write concatenated content to fileC
fs.writeFileSync(process.argv[4], contentA + '\n' + contentB);
