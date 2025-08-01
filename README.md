# �� Battleship Game

A classic Battleship game built with Python! Sink all the enemy ships by guessing their coordinates.

## 🎮 Features

- **10x10 Game Board** with coordinate system (A1-J10)
- **5 Different Ships**: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), Destroyer (2)
- **Hit/Miss Detection** with visual feedback (X for hits, O for misses)
- **Real-time Score Tracking** (hits/misses counter)
- **Win Condition** when all 17 ship spaces are hit
- **Interactive Command-line Interface**

## �� How to Play

1. **Run the game:**
   ```bash
   python battelship.py
   ```

2. **Enter coordinates** like "A1", "B3", "C5"
   - Column: A-J (left to right)
   - Row: 1-10 (top to bottom)

3. **Track your progress:**
   - Hit all 17 ship spaces to win
   - See your hits/misses in real-time

## 🧠 Learning Concepts

This game teaches:
- **2D Lists** - Game board representation
- **Nested Loops** - Board display and ship placement
- **String Manipulation** - Coordinate validation
- **User Input Processing** - Getting and validating guesses
- **Game State Management** - Tracking hits, misses, progress
- **Function Organization** - Modular code structure
- **Error Handling** - Input validation and edge cases

## 🚀 Code Structure

- `create_board()` - Initialize 10x10 game board
- `display_board()` - Show current game state
- `place_ship()` - Place ships with collision detection
- `get_player_guess()` - Get and validate player input
- `check_guess()` - Determine hit/miss and update board
- `play_game()` - Main game loop with win condition
