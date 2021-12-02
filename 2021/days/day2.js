/* Day 2: Dive! */
const { read } = require("../utils/input.js");
const input = read(2);

function partOne() {
  let position = 0;
  let depth = 0;

  for (const command of input) {
    const [cmd, arg] = command.split(" ");

    switch (cmd) {
      case "up":
        depth -= parseInt(arg);
        break;
      case "down":
        depth += parseInt(arg);
        break;
      case "forward":
        position += parseInt(arg);
        break;
    }
  }

  console.log(`Part 1: ${position * depth}`);
}

function partTwo() {
  let position = 0;
  let depth = 0;
  let aim = 0;

  for (const command of input) {
    const [cmd, arg] = command.split(" ");

    switch (cmd) {
      case "down":
        aim += parseInt(arg);
        break;
      case "up":
        aim -= parseInt(arg);
        break;
      case "forward":
        position += parseInt(arg);
        depth += (aim * parseInt(arg));
        break;
    }
  }

  console.log(`Part 2: ${position * depth}`);
}

partOne();
partTwo();
