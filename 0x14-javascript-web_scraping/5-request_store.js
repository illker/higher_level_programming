#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const myArgs = process.argv.slice(2);

request(myArgs[0]).pipe(fs.createWriteStream(myArgs[1]));
