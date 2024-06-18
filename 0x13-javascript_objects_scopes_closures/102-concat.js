#!/usr/bin/node

// Import the 'fs' module for file system operations.
const fs = require('fs');

// Read the content of the file specified by the first command-line argument,
// and convert it to a string using the 'toString' method.
const fArg = fs.readFileSync(process.argv[2]).toString();

// Read the content of the file specified by the second command-line argument,
// and convert it to a string using the 'toString' method.
const sArg = fs.readFileSync(process.argv[3]).toString();

// Write the concatenated content of the two input files to
// the file specified by the third command-line argument.
fs.writeFileSync(process.argv[4], fArg + sArg);
