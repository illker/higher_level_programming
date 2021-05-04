#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);

request.get(myArgs[0]).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});
