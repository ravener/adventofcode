/* Day 1: Sonar Sweep */
const { readNumbers } = require("../utils/input.js");
const input = readNumbers(1);

let increases = 0;
let windows = 0;

for (let i = 0; i < input.length; i++) {
  if (input[i] > input[i - 1]) increases++;
}

for (let i = 0; i < input.length; i++) {
  if (input[i] > input[i - 3]) windows++; 
}

console.log(`Part 1: ${increases}\nPart 2: ${windows}`);
