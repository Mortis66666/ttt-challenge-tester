import json
import random

def generate_test_case():
    # Initialize an empty board
    board = ['-' for _ in range(9)]
    # Initialize the player as X
    player = 'X'
    
    inputs = []
    outputs = []
    
    while '-' in board and not check_winner(board):
        # Generate a random move
        move = random.randint(0, 8)
        # Check if the move is legal
        if board[move] == '-':
            # Place the move on the board
            board[move] = player
            # Add the move to the inputs
            inputs.append(str(move))
            # Add the current state of the board to the outputs
            outputs.append(' '.join(board))
            # Switch players
            player = 'O' if player == 'X' else 'X'
    
    # Check the game outcome
    outcome = check_winner(board)
    if outcome:
        outputs.append(outcome)
    else:
        outputs.append("Tie")
    
    return inputs, "\n".join(outputs)

def check_winner(board):
    # Define winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '-':
            return board[combo[0]] + " win"
    
    return None

# Generate 10,000 test cases
test_cases = [[], []]
for _ in range(10000):
    inputs, outputs = generate_test_case()
    test_cases[0].append(inputs)
    test_cases[1].append(outputs)

# Write test cases to JSON file
with open('test_cases.json', 'w') as file:
    json.dump(test_cases, file, indent=2)
