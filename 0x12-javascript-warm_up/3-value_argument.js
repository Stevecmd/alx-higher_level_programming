#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2); // Exclude 'node' and script path

// Check if any arguments were passed
if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
