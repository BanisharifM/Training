"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString
    .replace(/\s*$/, "")
    .split("\n")
    .map((str) => str.replace(/\s*$/, ""));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

// Complete the reverseArray function below.
function reverseArray(a) {
  n = a.length();
  let res = [];
  for (i = n - 1; i >= 0; i--) {
    res = a[i];
  }
  return res;
}

function main() {
  console.log("sd");
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const arrCount = parseInt(readLine(), 10);

  ws.write(arrCount);

  const arr = readLine()
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

//   const res = reverseArray(arr);

  ws.write(res.join(" ") + "\n");

  ws.end();
}
