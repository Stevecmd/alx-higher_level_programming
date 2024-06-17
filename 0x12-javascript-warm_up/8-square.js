#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2]; // Exclude 'node' and script path

// Convert the argument to an integer using parseInt
const size = parseInt(arg);

// Check if the argument can be converted to a valid integer
if (!isNaN(size)) {
  // Iterate through rows to print the square
  for (let i = 0; i < size; i++) {
    let row = '';
    // Iterate through columns to construct each row of the square
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
