#!/usr/bin/node

const request = require('request');
const gameName = process.argv[2];
const id = process.argv[3];
const apiKey = 'RGAPI-4f4bd076-2cda-4018-99f6-b4958deb6cd3';  // Replace with your actual API key
const url = `https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/${gameName}/${id}?api_key=RGAPI-4f4bd076-2cda-4018-99f6-b4958deb6cd3`;


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
