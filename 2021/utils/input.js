const { join } = require("path");
const { readFileSync } = require("fs");

const pad = (day) => `day${day.toString().padStart(2, "0")}.txt`;

const read = (day) => readFileSync(join(__dirname, "..", "inputs", pad(day)))
  .toString()
  .trim()
  .split("\n");

const readNumbers = (day) => read(day).map(line => parseInt(line));

module.exports = { read, readNumbers };
