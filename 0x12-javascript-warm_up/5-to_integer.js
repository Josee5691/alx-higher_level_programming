#!/usr/bin/node
const statement = "Not a number";

const argument = parseInt(process.argv[2]);

if (isNaN(argument)){
	console.log("Not a number");
}
else
	console.log("My number: " + argument);
