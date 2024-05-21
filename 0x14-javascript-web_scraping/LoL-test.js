#!/usr/bin/node

const request = require('request');
const gameName = process.argv[2];
const id = process.argv[3];
const url = `/riot/account/v1/accounts/by-riot-id/${gameName}/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content)
    const characters = content.characters;
    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error)
        {
          console.log(error);
        } 
        else 
        {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
