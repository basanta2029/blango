import React, { useState, useEffect } from 'react';
import Board from './Board';
import GuessInput from './GuessInput';
import FoundSolutions from './FoundSolutions';
import './App.css';

const GAME_STATE = {
  BEFORE: 'before',
  IN_PROGRESS: 'in_progress',
  ENDED: 'ended',
};

function App() {
  const [gameState, setGameState] = useState(GAME_STATE.BEFORE);
  const [grid, setGrid] = useState([]);
  const [foundSolutions, setFoundSolutions] = useState([]);
  const [allSolutions, setAllSolutions] = useState(['apple', 'bee', 'cat']); // Example solutions
  const [totalTime, setTotalTime] = useState(0);
  const [startTime, setStartTime] = useState(null);
  const [timer, setTimer] = useState(60); // Game lasts 60 seconds

  // Start the game
  const startGame = () => {
    setGameState(GAME_STATE.IN_PROGRESS);
    setStartTime(Date.now());
    setGrid(generateGrid()); // Random grid generation
    setFoundSolutions([]);
    setTimer(60); // Reset timer to 60 seconds
  };

  // End the game
  const endGame = () => {
    setGameState(GAME_STATE.ENDED);
    setTotalTime((Date.now() - startTime) / 1000);
  };

  // Generates a simple grid
  const generateGrid = () => {
    return [
      ['A', 'B', 'C'],
      ['D', 'E', 'F'],
      ['G', 'H', 'I'],
    ];
  };

  // Timer logic, decrease time every second
  useEffect(() => {
    let interval;
    if (gameState === GAME_STATE.IN_PROGRESS && timer > 0) {
      interval = setInterval(() => {
        setTimer((prevTimer) => prevTimer - 1);
      }, 1000);
    } else if (timer === 0) {
      endGame(); // Automatically end the game when the timer reaches 0
    }
    return () => clearInterval(interval);
  }, [gameState, timer]);

  // Adds a correct word to found solutions
  const correctAnswerFound = (answer) => {
    setFoundSolutions([...foundSolutions, answer]);
  };

  return (
    <div className="App">
      <h1>Boggle Solitaire</h1>

      {gameState === GAME_STATE.BEFORE && (
        <button onClick={startGame}>Start Game</button>
      )}

      {gameState === GAME_STATE.IN_PROGRESS && (
        <>
          <p>Time Remaining: {timer} seconds</p> {/* Display timer */}
          <Board grid={grid} />
          <GuessInput
            allSolutions={allSolutions}
            foundSolutions={foundSolutions}
            correctAnswerCallback={correctAnswerFound}
          />
          <button onClick={endGame}>Stop Game</button>
        </>
      )}

      {gameState === GAME_STATE.ENDED && (
        <>
          <h2>Game Over</h2>
          <p>Total Time: {totalTime} seconds</p>
          <FoundSolutions headerText="Solutions You've Found" words={foundSolutions} />
          <FoundSolutions headerText="Missed Words" words={allSolutions.filter(word => !foundSolutions.includes(word))} />
          <button onClick={startGame}>Start New Game</button>
        </>
      )}
    </div>
  );
}

export default App;