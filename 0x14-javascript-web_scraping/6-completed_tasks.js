#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const url = myArgs[0];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = {};
    const burger = JSON.parse(body);
    for (const bu of burger) {
      if (bu.completed === true) {
        if (tasks[bu.userId] === undefined) {
          tasks[bu.userId] = 1;
        } else {
          tasks[bu.userId] += 1;
        }
      }
    }
    console.log(tasks);
  }
});
