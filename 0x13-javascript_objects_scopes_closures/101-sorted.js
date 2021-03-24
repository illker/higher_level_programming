#!/usr/bin/node
const burger = require('./101-data.js').dict;
const bacon = {};
for (const i in burger) {
  if (bacon[burger[i]] === undefined) {
    bacon[burger[i]] = [];
  }
  bacon[burger[i]].push(i);
}
console.log(bacon);
