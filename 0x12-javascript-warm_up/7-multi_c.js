#!/usr/bin/node
let burger = parseInt(process.argv[2])
if (isNaN(burger)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < burger; i++) {
    console.log('C is fun');
  }
}
