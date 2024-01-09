#!/usr/bin/node
const empty = 'undefined';
console.log((process.argv[2] || empty) + ' is ' + (process.argv[3] || empty));
