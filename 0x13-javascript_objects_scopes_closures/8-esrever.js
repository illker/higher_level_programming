#!/usr/bin/node
exports.esrever = function (list) {
  const bacon = [];
  for (let burger = list.length - 1; burger >= 0; burger--) {
    bacon.push(list[burger]);
  }
  return bacon;
};
