#!/usr/bin/node

// Define a recursive function to compute factorial
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0) {
    return 1;
  }

  // Recursive case: factorial of n is n times factorial of (n-1)
  return n * factorial(n - 1);
}

// Get the first argument passed to the script and convert to integer
const arg = parseInt(process.argv[2]);

// Compute factorial using the factorial function
const result = factorial(arg);

// Print the result using console.log
console.log(result);
