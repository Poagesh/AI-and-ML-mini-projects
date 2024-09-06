# Tic-Tac-Toe Game with AI

## Overview
This project is a Python-based implementation of a Tic-Tac-Toe game where a human player competes against an AI. The AI uses the Minimax algorithm with alpha-beta pruning to make optimal moves, ensuring it never loses. The human player plays as 'X', while the AI plays as 'O'.

## Features
- **Human vs AI**: The human player inputs moves, while the AI uses the Minimax algorithm to respond.
- **Minimax Algorithm**: AI is designed to play optimally using this algorithm with alpha-beta pruning.
- **Dynamic Board Display**: The game board is displayed after each move.
- **Random First Move for AI**: The AI selects its first move randomly to add variety to the game.

## How to Play
1. At the start of the game, the board is shown with numbers (0-8) indicating available positions.
2. The human player selects a move by inputting a number corresponding to an empty position on the board.
3. The AI responds with its move using the Minimax algorithm.
4. The game alternates between the human and AI until either:
   - One player wins.
   - The game ends in a tie.

## Classes
- **`tictactoe`**: Handles the game board, checking available moves, and determining the winner.
- **`HumanPlayer`**: Allows the human player to input their move.
- **`AIPlayer`**: Implements the AI logic with Minimax for the optimal move.
  
## Dependencies
- **Python 3.x**: Ensure you have Python installed.
  
## How to Run
1. Clone or download the repository.
2. Run the game by executing the Python script:
   ```bash
   python tictactoe.py
   ```
3. Follow the on-screen prompts to play against the AI.

## Example Gameplay
```
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
X's turn. Input move (0-8): 0
X makes a move to square 0
| X |   |   |
|   |   |   |
|   |   |   |
...
```


Enjoy playing Tic-Tac-Toe against an unbeatable AI!!!!!
