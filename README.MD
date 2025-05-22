# Python Tic-Tac-Toe Game

This repository contains a simple implementation of the classic Tic-Tac-Toe game developed in Python. The game features both single-player mode against a computer opponent and a two-player mode for playing with friends.

## Game Features

- **Two Game Modes**:
  - Play against the computer
  - Play against another player
- **Interactive Command-Line Interface**
- **Player Customization**:
  - Choose player names
  - Select your preferred symbol (X or O)
- **Game Logic**:
  - Win detection (horizontal, vertical, and diagonal)
  - Draw detection
  - Input validation
  - Automatic board reset after game completion

## How to Play

1. Run the game using Python:

   ```bash
   python -m src
   ```

   or navigate to the src directory and run:

   ```bash
   python __main__.py
   ```

2. Choose your game mode:
   - Play against the computer (PC)
   - Play against another player (GIOCATORE)

3. Enter player name(s) and choose your symbol (X or O)

4. Make moves by entering row (0-2) and column (0-2) coordinates when prompted

5. The game will automatically detect wins, draws, and reset the board for a new game

## Game Controls

- **Row Input**: Enter a number between 0-2 to select the row
- **Column Input**: Enter a number between 0-2 to select the column
- The game validates all inputs and prevents illegal moves

## Code Structure

The game is organized in a single Python module with the following key functions:

- `print_board()`: Displays the current state of the game board
- `board_full()`: Checks if the board is full (draw condition)
- `reset_board()`: Resets the board for a new game
- `check_winner()`: Determines if the current player has won
- `make_move(x, y)`: Places a player's symbol on the board
- `computer_move()`: Handles the computer's turn (random move selection)
- `setup_game()`: Initializes the game with player information
- `main()`: Main game loop that handles player input and game flow

## Requirements

- Python 3.x

## Example Game Board

```
 X |   |   
-----------
   | O |   
-----------
   |   | X 
```

## Future Improvements

Potential enhancements for the game could include:
- Implementing a smarter AI for the computer player
- Adding a graphical user interface
- Keeping score across multiple games
- Adding difficulty levels for the computer opponent
- Implementing a replay feature

---

*This project was created as part of the educational journey at ITS Steve Jobs Academy.*