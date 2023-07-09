import tkinter as tk
from tkinter import messagebox

# Initialize the game
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create buttons for the board
buttons = [[None for _ in range(3)] for _ in range(3)]

def on_button_click(row, col):
    global current_player

    # Check if the cell is already occupied
    if board[row][col] != ' ':
        return

    # Update the board and button text
    board[row][col] = current_player
    buttons[row][col].config(text=current_player)

    # Check if the current player wins
    if check_winner(current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_game()
        return

    # Check if it's a tie
    if is_board_full():
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()
        return

    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'

def check_winner(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full():
    for row in board:
        if ' ' in row:
            return False
    return True

def reset_game():
    global current_player, board

    current_player = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state=tk.NORMAL)

# Create buttons and bind them to the event handler
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(window, text=' ', font=('Arial', 20), width=6, height=3,
                                 command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Start the main event loop
window.mainloop()
