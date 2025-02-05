# sudoku_gui.py
import tkinter as tk
import numpy as np
from sudoku_solver import solve, is_valid  # Import the solve function from the previous file

def create_gui(board):
    root = tk.Tk()
    root.title("Sudoku Solver")

    entries = {}

    # Create a 9x9 grid of Entry widgets for Sudoku input
    for row in range(9):
        for col in range(9):
            entry = tk.Entry(root, width=5, font=("Arial", 20), borderwidth=2, relief="solid", justify="center")
            entry.grid(row=row, column=col)
            if board[row][col] != 0:
                entry.insert(0, str(board[row][col]))
                entry.config(state="readonly")
            entries[(row, col)] = entry

    # Function to solve the board when the button is clicked
    def solve_button_click():
        if solve(board):
            for row in range(9):
                for col in range(9):
                    entries[(row, col)].delete(0, tk.END)
                    entries[(row, col)].insert(0, str(board[row][col]))

    solve_button = tk.Button(root, text="Solve", command=solve_button_click, font=("Arial", 14))
    solve_button.grid(row=9, column=0, columnspan=9)

    root.mainloop()

# Example initial Sudoku puzzle
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

create_gui(board)
