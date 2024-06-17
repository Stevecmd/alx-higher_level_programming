#!/usr/bin/node

// Define the function add with parameters a and b
function add (a, b) {
  return a + b;
}

// Get the first and second arguments passed to the script
const arg1 = process.argv[2]; // First argument (excluding 'node' and script path)
const arg2 = process.argv[3]; // Second argument

// Convert arguments to integers using parseInt
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

// Check if both arguments can be converted to integers
if (!isNaN(num1) && !isNaN(num2)) {
  // Call the add function and print the result
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}
