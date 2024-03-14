#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};
for (const id in dict) {
	  console.log(id);
	  if (newDict[dict[id]]) {
		      newDict[dict[id]].push(id);
		    } else {
			        newDict[dict[id]] = [id];
			      }
}
console.log(newDict);
