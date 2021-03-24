#!/usr/bin/node
const fs = require('fs');
const burger = fs.readFilesSync(process.argv[2], 'utf8');
const bacon = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], burger + bacon);
