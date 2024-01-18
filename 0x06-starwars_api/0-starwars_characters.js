#!/usr/bin/node
// script to print file contents
const req = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

const getName = (charUrl) => {
  return new Promise((resolve, reject) => {
    req(charUrl, function (err, res, bdy) {
      if (err) {
        reject(err);
        return;
      }

      const character = JSON.parse(bdy);
      resolve(character.name);
    });
  });
};

req(url, async function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const names = [];
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    const charUrl = characters[i];

    const name = await getName(charUrl);

    names.push(name);
  }

  names.map((n) => console.log(n));
});
