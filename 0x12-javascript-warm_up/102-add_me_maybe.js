#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const n = number++;
  theFunction(n);
};
