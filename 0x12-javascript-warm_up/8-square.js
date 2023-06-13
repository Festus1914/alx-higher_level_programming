#!/usr/bin/node
function printSquare(size) {
  const squareSize = parseInt(size);
  
  if (isNaN(squareSize)) {
    console.log("Missing size");
    return;
  }
  
  for (let i = 0; i < squareSize; i++) {
    let row = "";
    for (let j = 0; j < squareSize; j++) {
      row += "X";
    }
    console.log(row);
  }
}

const squareSize = process.argv[2];
printSquare(squareSize);
