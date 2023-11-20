def rps(p1, p2):
    # Define the possible moves
    moves = ['rock', 'paper', 'scissors']

    # Check if inputs are valid moves
    if p1 not in moves or p2 not in moves:
        return "Invalid input. Please choose from 'rock', 'paper', or 'scissors'."

    # Determine the winner
    if p1 == p2:
        return "Draw!"
    elif (p1 == 'rock' and p2 == 'scissors') or \
         (p1 == 'paper' and p2 == 'rock') or \
         (p1 == 'scissors' and p2 == 'paper'):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

result = rps('rock', 'scissors')
print(result)