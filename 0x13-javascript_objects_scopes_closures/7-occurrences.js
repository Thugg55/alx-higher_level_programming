#!/usr/bin/node
// function returns the number of occurences in a list.

exports.nbOccurences = function (list, searchElement) {
	const x;
	let occ = 0;
	for (x of list) {
		if (x === searchElement) {
			occ++;
		}
	}
	return occ;
};
