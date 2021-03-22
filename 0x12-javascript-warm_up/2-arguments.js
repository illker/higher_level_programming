#!/usr/bin/node
burger = process.argv.length
if (burger < 3) {
  console.log('No argument')
} else if (burger === 3) {
  console.log('Argument found')
} else if (burger > 3) {
  console.log('Arguments found')
}
