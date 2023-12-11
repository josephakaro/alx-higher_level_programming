#!/usr/bin/node
const { argv } = require("node:process");

if (argv) {
  if (argv.length >= 3) {
    console.log("Argument found");
  } else if (argv.length <= 3) {
    console.log("No argument");
  }
}
