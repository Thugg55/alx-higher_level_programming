#!/usr/bin/node
/* Script display the Status code of a GET request
 * first argument is URL to request(GET)
 * printed in this form "code: <status code>
 */

const rq = require('request')
const url = process.argv(2)

rq(url, (err, response, data) => {
	if (err) {
		console.log(err);
		return;
	}
	console.log(`code: ${response.statusCode}`);
});
