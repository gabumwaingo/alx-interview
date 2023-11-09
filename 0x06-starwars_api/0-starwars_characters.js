#!/usr/bin/node
//fetching data frok the star wars api


const request = require('request');
const filmurl = 'https://swapi-api.alx-tools.com/api/films/${process.argv[2]}';

request(filmurl, (error, response, body) => {
	if (error) 
		console.log(error);
	else {
		console.log(body);
		try {
			const filmData = JSON.parse(body);
			const characters = filmData.characters;

			characters.forEach(characterurl => {
				request(characterUrl, (error, response, characterBody) => {
					if (!error && response.statusCode == 200){
						const characterData = JSON.parse(characterBody);
						console.log(characterData.name);
					} else {
						console.log('Error fetching the characters: ${error}');
				}
			});
		});
		} catch (ParseError) {
			console.log('Error parsing filmData: ${parseError}');
		}
	}

});
