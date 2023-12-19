const fs = require('fs');
const path = require('path');

// const myLogger = async function (req, res, next) {
// 	// for local
// 	// let jsonPath = path.join(__dirname, 'requestCount.log');

// 	// for server
// 	let jsonPath = path.join(__dirname, 'requestCount.log');

// 	console.log('reqCount Dir name', jsonPath);
// 	let requestCount;
// 	let requestCountString;
// 	fs.readFile(jsonPath, 'utf8', (err, data) => {
// 		if (err) {
// 			// console.log('Error', err);
// 		} else {
// 			// console.log('Data', data);
// 			requestCount = Number(data);
// 			// console.log('RequestCount int type =', typeof requestCount);
// 			// console.log('RequestCount int =', requestCount);
// 			requestCountString = ++requestCount;
// 			// console.log('RequestCountString type =', typeof requestCountString);
// 			// console.log('RequestCountString = ', requestCountString);
// 		}

// 		fs.writeFile(jsonPath, String(requestCountString), (err) => {
// 			// console.log(err);
// 		});
// 	});

// 	next();
// };

// TEXT GET REQUEST START
const myLogger = async function (req, res, next) {
	let filePath = path.join(__dirname, '../database', 'reqCount.txt');
	console.log('reqCount dir name = ', __dirname);
	console.log('reqCount file path = ', filePath);

	// Read the content of reqCount.txt with the callback style
	let fileDataNumber;
	let fileDataString;
	fs.readFile(filePath, 'utf-8', (err, fileContent) => {
		if (err) {
			console.error('Error reading reqCount.txt:', err);
			res.status(500).send('Internal Server Error');
		} else {
			fileDataNumber = Number(fileContent);
			fileDataString = ++fileDataNumber;

			console.log('request count =', fileDataNumber);
			console.log(req.protocol); // "https"
			console.log(req.hostname); // "example.com"
			console.log(req.path); // "/creatures"
			console.log(req.originalUrl); // "/creatures?filter=sharks"
			console.log(req.subdomains); // "['ocean']

			fs.writeFile(filePath, String(fileDataString), (err) => {
				// console.log(err);
			});

			//res.json({ RequestCount: fileContent });
		}
	});
	next();
};
// TEST GET REQUEST END

module.exports = myLogger;
