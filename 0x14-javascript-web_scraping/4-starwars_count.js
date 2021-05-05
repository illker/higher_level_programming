#!/usr/bin/node

const request = require('request');
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';

request(wedge, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const burger = JSON.parse(body).films;
    console.log(burger.length);
  }
});
