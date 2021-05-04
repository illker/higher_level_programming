#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv.slice(2);

fs.writeFile(myArgs[0], myArgs[1], 'utf-8', err => {
  if (err) {
    return console.error(err);
  }
});
