const { join } = require("path");
const { readFileSync } = require("fs");

const pad = (day) => `day${day.toString().padStart(2, "0")}.txt`;

module.exports.read = (day) => readFileSync(join(__dirname, "..", "inputs", pad(day)))
  .toString()
  .trim()
  .split("\n");
