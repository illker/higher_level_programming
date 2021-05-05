#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const url = myArgs[0];
const wedge = '/18/';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let j = 0;
    const burger = JSON.parse(body);
    for (const bu of burger.results) {
      for (const character of bu.characters) {
        if (character.includes(wedge)) {
          j++;
        }
      }
    }
    console.log(j);
  }
});
