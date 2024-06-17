#!/usr/bin/node

// Get the command line arguments excluding
// the first two elements (node and script path)
const args = process.argv.slice(2);

// Determine the message to print based on the number of arguments
let message;
if (args.length === 0) {
  message = 'No argument';
} else if (args.length === 1) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

// Print the message to the console
console.log(message);
