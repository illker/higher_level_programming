#!/usr/bin/node
burger = process.argv.length;
if (burger < 3) {
  console.log('No argument');
} else if (burger === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
