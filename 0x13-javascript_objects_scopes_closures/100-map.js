#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const burger = list.map((bacon, index) => bacon * index);
console.log(burger);
