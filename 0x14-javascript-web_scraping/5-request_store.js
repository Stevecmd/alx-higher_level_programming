#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const fs = require('fs');
const filePath = process.argv[3];

request(url).pipe(fs.createWriteStream(filePath, { encoding: 'utf8' }))
  .on('close', () => {
    console.log(`Content saved to ${filePath}`);
  })
  .on('error', (error) => {
    console.error(`Error: ${error.message}`);
  });
