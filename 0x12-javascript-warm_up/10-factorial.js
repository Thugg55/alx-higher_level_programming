#!/usr/bin/node
// Script computes and prints a factorial

function factorial (num) {
  return num === 0 || isNaN(num) ? 1 : num * factorial(num - 1);
}

const x = process.argv[2] / 1;
isNaN(x) ? console.log('1') : console.log(factorial(x));
