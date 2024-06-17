#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Define variables to hold the arguments
const arg1 = args[0] || 'undefined';
const arg2 = args[1] || 'undefined';

// Print the formatted output
console.log(`${arg1} is ${arg2}`);
