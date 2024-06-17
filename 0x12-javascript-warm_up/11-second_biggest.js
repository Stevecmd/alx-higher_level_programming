#!/usr/bin/node

// Get all arguments passed to the script,
// excluding 'node' and script path
const args = process.argv.slice(2);

// Convert arguments to integers
const numbers = args.map(arg => parseInt(arg));

// Sort numbers in descending order
numbers.sort((a, b) => b - a);

// If there are no arguments or only one argument, print 0
if (numbers.length < 2) {
  console.log(0);
} else {
  // Find and print the second largest number
  console.log(numbers[1]);
}
