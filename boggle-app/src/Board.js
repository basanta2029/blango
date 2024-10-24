import React from 'react';
import './Board.css';

function Board({ grid }) {
  return (
    <div className="Board">
      {grid.map((row, rowIndex) => (
        <div key={rowIndex} className="Board-row">
          {row.map((letter, colIndex) => (
            <div key={colIndex} className="Board-tile">
              {letter}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default Board;