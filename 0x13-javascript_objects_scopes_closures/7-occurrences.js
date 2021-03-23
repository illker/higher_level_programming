#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let burger = 0;
  for (const i in list) {
    if (searchElement === list[i]) {
      burger++;
    }
  }
  return burger;
};
