import random
import tkinter as tk
from tkinter import messagebox

board = [' ' for _ in range(9)]

HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'

WIN_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


def is_board_full():
    
    return ' ' not in board


def is_winner(player):
    
    for combo in WIN_COMBINATIONS:
        if all(board[i] == player for i in combo):
            return True
    return False


def get_empty_cells():
    
    return [i for i, cell in enumerate(board) if cell == ' ']


def make_human_move(button):
    
    index = button.grid_info()['row'] * 3 + button.grid_info()['column']
    if board[index] == ' ':
        button.config(text=HUMAN_PLAYER)
        board[index] = HUMAN_PLAYER

        if is_winner(HUMAN_PLAYER):
            messagebox.showinfo("Game Over", "You won!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            make_ai_move()


def make_ai_move():
    
    best_score = float('-inf')
    best_move = None

    for cell in get_empty_cells():
        board[cell] = AI_PLAYER
        score = minimax(board, 0, False)
        board[cell] = ' '

        if score > best_score:
            best_score = score
            best_move = cell

    button_index = best_move
    buttons[button_index].config(text=AI_PLAYER)
    board[button_index] = AI_PLAYER

    if is_winner(AI_PLAYER):
        messagebox.showinfo("Game Over", "AI wins!")
        reset_game()
    elif is_board_full():
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()


def minimax(board, depth, is_maximizing):

    if is_winner(HUMAN_PLAYER):
        return -1
    elif is_winner(AI_PLAYER):
        return 1
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for cell in get_empty_cells():
            board[cell] = AI_PLAYER
            score = minimax(board, depth + 1, False)
            board[cell] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for cell in get_empty_cells():
            board[cell] = HUMAN_PLAYER
            score = minimax(board, depth + 1, True)
            board[cell] = ' '
            best_score = min(score, best_score)
        return best_score


def reset_game():

    for button in buttons:
        button.config(text=' ')
    for i in range(9):
        board[i] = ' '


root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text=' ', width=10, height=4,
                           command=lambda row=i, col=j: make_human_move(buttons[row * 3 + col]))
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(button)

root.mainloop()