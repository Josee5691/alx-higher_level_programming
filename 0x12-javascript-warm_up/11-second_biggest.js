#!/usr/bin/node
const arr = process.argv
const length = arr.length

function secondBiggest(arr){
	arr.sort((a, b) => (b - a))
	return arr[1];
}

if (length < 4)
	console.log(0);
else
	console.log(secondBiggest(arr.slice(2, length)));

