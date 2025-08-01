def create_board():
    """Create a 10x10 battleship board"""
    board = []
    for row in range(10):
        board.append(['.'] * 10)
    return board

def display_board(board):
    """Display the board with coordinates"""
    print("   A B C D E F G H I J")
    print("  " + "-" * 21)
    
    for row in range(10):
        row_num = str(row + 1).rjust(2)
        print(f"{row_num} ", end="")
        
        for col in range(10):
            print(f"{board[row][col]} ", end="")
        print()

board = create_board()
print("🚢 BATTLESHIP BOARD")
print("=" * 25)
display_board(board)

ships = {
    'Carrier': {'size': 5, 'symbol': 'C'},
    'Battleship': {'size': 4, 'symbol': 'B'},
    'Cruiser': {'size': 3, 'symbol': 'R'},
    'Submarine': {'size': 3, 'symbol': 'S'},
    'Destroyer': {'size': 2, 'symbol': 'D'}
}

def place_ship(board, ship_name, ship_data, start_row, start_col, direction):
    """Place a ship on the board - H for horizontal, V for vertical"""
    size = ship_data['size']
    symbol = ship_data['symbol']
    
    if direction == 'H':
        if start_col + size > 10:
            print(f"❌ {ship_name} doesn't fit horizontally!")
            return False
        for col in range(start_col, start_col + size):
            if board[start_row][col] != '.':
                print(f"❌ Space occupied at {start_row+1},{chr(65+col)}!")
                return False
        for col in range(start_col, start_col + size):
            board[start_row][col] = symbol
    else:
        if start_row + size > 10:
            print(f"❌ {ship_name} doesn't fit vertically!")
            return False
        for row in range(start_row, start_row + size):
            if board[row][start_col] != '.':
                print(f"❌ Space occupied at {row+1},{chr(65+start_col)}!")
                return False
        for row in range(start_row, start_row + size):
            board[row][start_col] = symbol
    
    print(f"✅ {ship_name} placed successfully!")
    return True

place_ship(board, 'Carrier', ships['Carrier'], 0, 0, 'H')
place_ship(board, 'Battleship', ships['Battleship'], 2, 2, 'V')
place_ship(board, 'Destroyer', ships['Destroyer'], 5, 5, 'H')

print("\n🚢 BOARD WITH SHIPS")
print("=" * 25)
display_board(board)

def get_player_guess():
    """Get and validate player input"""
    while True:
        try:
            guess = input("Enter your guess (e.g., A5): ").upper().strip()
            
            if len(guess) < 2:
                print("❌ Please enter both column and row (e.g., A5)")
                continue
            
            col_letter = guess[0]
            row_str = guess[1:]
            
            if col_letter not in 'ABCDEFGHIJ':
                print("❌ Column must be A-J")
                continue
            
            row_num = int(row_str)
            if row_num < 1 or row_num > 10:
                print("❌ Row must be 1-10")
                continue
            
            col = ord(col_letter) - ord('A')
            row = row_num - 1
            
            return row, col
            
        except ValueError:
            print("❌ Invalid input. Please enter like 'A5'")
        except Exception as e:
            print(f"❌ Error: {e}")

def check_guess(board, row, col):
    """Check if guess is a hit or miss"""
    if board[row][col] == '.':
        board[row][col] = 'O'
        return False, "Miss! 💧"
    elif board[row][col] in 'CBRDS':
        ship_symbol = board[row][col]
        board[row][col] = 'X'
        return True, f"Hit! 🎯 You hit a {get_ship_name(ship_symbol)}!"
    else:
        return None, "You already guessed that spot!"

def get_ship_name(symbol):
    """Convert ship symbol to name"""
    ship_names = {
        'C': 'Carrier',
        'B': 'Battleship', 
        'R': 'Cruiser',
        'S': 'Submarine',
        'D': 'Destroyer'
    }
    return ship_names.get(symbol, 'Unknown Ship')

def play_game(board):
    """Main game loop"""
    hits = 0
    misses = 0
    total_ships = 17
    
    print("\n🎮 GAME START!")
    print("=" * 30)
    
    while hits < total_ships:
        print(f"\nHits: {hits} | Misses: {misses}")
        display_board(board)
        
        row, col = get_player_guess()
        is_hit, message = check_guess(board, row, col)
        
        if is_hit is None:
            print(message)
            continue
        elif is_hit:
            hits += 1
            print(f"✅ {message}")
        else:
            misses += 1
            print(f"❌ {message}")
        
        print(f"Progress: {hits}/{total_ships} ships hit")
    
    print("\n🎉 CONGRATULATIONS! You sunk all ships!")
    print(f"Final Score: {hits} hits, {misses} misses")

if __name__ == "__main__":
    print("\n🚢 BATTLESHIP GAME")
    print("=" * 30)
    play_game(board)
