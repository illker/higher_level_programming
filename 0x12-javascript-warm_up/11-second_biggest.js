#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const burger = process.argv.slice(2);
  burger.sort();
  burger.reverse();
  console.log(burger[1]);
}
