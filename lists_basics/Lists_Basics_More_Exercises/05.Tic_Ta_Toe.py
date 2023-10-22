board = []

first_player = "First player won"
second_player = "Second player won"
winner = ""

for i in range(3):
    row_input = input().split()
    row_digits = [int(x) for x in row_input]
    board.append(row_digits)

for player in range(3):
    if board[player][0] == board[player][1] == board[player][2] != 0:
        if board[player][0] == 1:
            winner = first_player
        else:
            winner = second_player
        break

    elif board[0][player] == board[1][player] == board[2][player] != 0:
        if board[player][0] == 1:
            winner = first_player
        else:
            winner = second_player
        break

else:
    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        if board[1][1] == 1:
            winner = first_player
        else:
            winner = second_player
    else:
        winner = "Draw!"

print(winner)
