#!/usr/bin/node

// Importing the dictionary from 101-data.js
const { dict } = require('./101-data');

// Creating a new dictionary to store user ids by occurrence
const sortedDict = {};

// Iterating over the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // If the occurrence count is already a key in sortedDict, push userId to its array
  if (sortedDict[occurrence]) {
    sortedDict[occurrence].push(userId.toString()); // Ensure userId is converted to string
  } else {
    // Otherwise, create a new array with userId as the first element
    sortedDict[occurrence] = [userId.toString()]; // Ensure userId is converted to string
  }
}

// Printing the sorted dictionary
console.log(sortedDict);
