const fs = require('fs');
const path = require('path');

const myLogger = async function (req, res, next) {
	let jsonPath = path.join(__dirname, 'requestCount.log');
	console.log(jsonPath);
	let requestCount;
	let requestCountString;
	fs.readFile(jsonPath, 'utf8', (err, data) => {
		if (err) {
			// console.log('Error', err);
		} else {
			// console.log('Data', data);
			requestCount = Number(data);
			// console.log('RequestCount int type =', typeof requestCount);
			// console.log('RequestCount int =', requestCount);
			requestCountString = ++requestCount;
			// console.log('RequestCountString type =', typeof requestCountString);
			// console.log('RequestCountString = ', requestCountString);
		}

		fs.writeFile(jsonPath, String(requestCountString), (err) => {
			// console.log(err);
		});
	});

	next();
};

module.exports = myLogger;
