#!/usr/bin/node

// Importing the list array from 100-data.js
const { list } = require('./100-data');

// Using map to create a new array where each element is multiplied by its index
const newList = list.map((value, index) => value * index);

// Printing the original list and the new list
console.log(list);
console.log(newList);
