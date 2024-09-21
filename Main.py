# Create the Tic-Tac-Toe board
def create_board():
    return [' ' for _ in range(9)]  # A 3x3 board

# Display the board in CLI
def display_board(board):
    print("\n")
    for i in range(3):
        print(f"{board[3*i]} | {board[3*i+1]} | {board[3*i+2]}")
        if i < 2:
            print("--+---+--")
    print("\n")

# Check for a win
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]             # Diagonals
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_conditions)

# Check if the game is a tie
def is_tie(board):
    return ' ' not in board

# Human player makes a move
def player_move(board, player):
    move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = player
    else:
        print("Invalid move. Try again.")
        player_move(board, player)

# Game loop
def game():
    board = create_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        
        if current_player == 'X':  # Human player's turn
            player_move(board, current_player)
        else:  # AI player's turn
            move = minimax(board, current_player)['position']
            board[move] = current_player
            print(f"AI chose position {move + 1}")
        
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'  # Switch turns

        # Minimax algorithm
def minimax(board, player):
    opponent = 'X' if player == 'O' else 'O'
    
    # Base case: Check for a terminal state
    if check_winner(board, 'O'):
        return {'score': 1}
    elif check_winner(board, 'X'):
        return {'score': -1}
    elif is_tie(board):
        return {'score': 0}

    # Recursive case: Evaluate all possible moves
    moves = []
    for i in range(9):
        if board[i] == ' ':
            # Simulate the move
            board[i] = player
            result = minimax(board, opponent)
            moves.append({'position': i, 'score': result['score']})
            board[i] = ' '  # Undo the move

    # Choose the best move for AI (maximizing player O)
    if player == 'O':
        best_move = max(moves, key=lambda x: x['score'])
    else:
        best_move = min(moves, key=lambda x: x['score'])

    return best_move



def main():
    game()

if __name__ == "__main__":
    main()
