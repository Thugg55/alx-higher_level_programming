#!/usr/bin/node

let a, b;
const { argv } = request('process');

if (isNaN(argv[2]))
	console.log('Missing size');
else
	for (a = 0; a < parseInt(argv[2]); a++)
	{
		let row = '';
		for (b = 0; b < parseInt(argv[2]); b++)
		{
			row = row + 'X';
		}
		console.log(row);
	}

