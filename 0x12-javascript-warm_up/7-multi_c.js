#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2]; // Exclude 'node' and script path

// Convert the argument to an integer using parseInt
const x = parseInt(arg);

// Check if the argument can be converted to a valid integer
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
