/* Day 1: Sonar Sweep */
const { read } = require("../utils/input.js");
const input = read(1).map(line => parseInt(line));

let increases = 0;
let windows = 0;

/* input.reduce((previous, measurement) => {
  if (!previous) return measurement;
  if (measurement > previous) increases++;
  return measurement;
}, 0);*/

for (let i = 0; i < input.length; i++) {
  if (input[i] > input[i - 1]) increases++;
}

for (let i = 0; i < input.length; i++) {
  if (input[i] > input[i - 3]) windows++; 
}

console.log(`Part 1: ${increases}\nPart 2: ${windows}`);
