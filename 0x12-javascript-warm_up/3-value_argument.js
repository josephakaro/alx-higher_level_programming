#!/usr/bin/node
const { argv } = require("node:process");

if (argv) {
  if (argv.length >= 3) {
    for (i = 2; i < argv.length; i++) {
      if (argv[i] <= 3) break;
      console.log(argv[i]);
    }
  } else if (argv.length <= 3) {
    console.log("No argument");
  }
}