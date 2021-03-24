#!/usr/bin/node
let burger = 0;
exports.logMe = function (item) {
  console.log(`${burger}: ${item}`);
  burger++;
};
