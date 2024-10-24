import React, { useState } from 'react';
import './GuessInput.css';

function GuessInput({ allSolutions, foundSolutions, correctAnswerCallback }) {
  const [input, setInput] = useState('');
  const [message, setMessage] = useState('Make your first guess!');

  const handleGuess = () => {
    if (foundSolutions.includes(input)) {
      setMessage(`${input} has already been found!`);
    } else if (allSolutions.includes(input)) {
      correctAnswerCallback(input);
      setMessage(`${input} is correct!`);
    } else {
      setMessage(`${input} is incorrect!`);
    }
    setInput('');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleGuess();
    }
  };

  return (
    <div className="GuessInput">
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder="Enter a word"
      />
      <p>{message}</p>
    </div>
  );
}

export default GuessInput;