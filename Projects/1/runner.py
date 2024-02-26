# The GUI and main function have been completed for you!
# Do NOT change anything below this line
# This file will not be checked for PEP8

import tkinter as tk
import argparse
from traversals import *

traversal_functions = {
    'row': row_major_traversal,
    'column': column_major_traversal,
    'row_zigzag': row_zigzag_traversal,
    'column_zigzag': column_zigzag_traversal,
    'main': main_diagonal_traversal,
    'secondary': secondary_diagonal_traversal,
    'spiral': spiral_traversal,
}


class GridTraversalApp:
    def __init__(self, master, rows, cols, traversal_functions, debug, speed):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.grid_cells = [[None for _ in range(cols)] for _ in range(rows)]
        self.debug = debug
        self.speed = speed
        
        self.traversal_functions = traversal_functions
        self.current_traversal = None
        
        self.after_id = None
        
        self.create_navigation_bar()
        self.create_grid_frame()

    def create_navigation_bar(self):
        navigation_frame = tk.Frame(self.master)
        navigation_frame.grid(row=0, column=0, columnspan=self.cols)

        texts = ["Row Major", "Column Major", "Row Zigzag", "Column Zigzag", "Main Diagonal", "Secondary Diagonal", "Spiral", "Exit"]

        buttons = zip(texts, [*traversal_functions.values()] + [self.master.destroy])

        for i, (text, command) in enumerate(buttons):
            if text == texts[-1]:
                btn = tk.Button(navigation_frame, text=text, command=command)
            else:
                btn = tk.Button(navigation_frame, text=text, command=lambda cmd=command: self.start_traversal(cmd))
            btn.grid(row=0, column=i, padx=5, pady=5)

    def create_grid_frame(self):
        grid_frame = tk.Frame(self.master)
        grid_frame.grid(row=1, column=0, padx=10, pady=10)

        for i in range(self.rows):
            for j in range(self.cols):
                cell = tk.Canvas(grid_frame, width=50, height=50, bg='white', highlightthickness=1)
                cell.grid(row=i, column=j)
                self.grid_cells[i][j] = cell

        for i in range(self.rows):
            label = tk.Label(grid_frame, text=f"Row {i}")
            label.grid(row=i, column=self.cols, padx=(5, 0))

        for j in range(self.cols):
            label = tk.Label(grid_frame, text=f"Col {j}")
            label.grid(row=self.rows, column=j)

    def start_traversal(self, traversal_function):
        self.reset_grid()
        if self.after_id is not None:
            self.master.after_cancel(self.after_id)
        self.current_traversal = iter(traversal_function(self.grid_cells))
        if self.debug:
            print("Debug:", traversal_function(self.grid_cells))
        self.update_grid()

    def update_grid(self):
        try:
            row, col = next(self.current_traversal)
            self.grid_cells[row][col].configure(bg='orange')
            self.after_id = self.master.after(self.speed, self.update_grid)
        except StopIteration:
            pass
    
    def reset_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid_cells[i][j].configure(bg='white')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Matrix Argument Parser')

    parser.add_argument('--rows', type=int, default=5, choices=range(1, 11), help='Number of rows in the matrix (between 1 and 10)')
    parser.add_argument('--columns', type=int, default=5, choices=range(1, 11), help='Number of columns in the matrix (between 1 and 10)')
    parser.add_argument('--traversal', choices=["row", 'column', 'row_zigzag', 'column_zigzag', 'main', 'secondary', 'spiral'], default='row', help='Type of traversal')
    parser.add_argument('--gui', action='store_true', help='Enable GUI mode')
    parser.add_argument('--speed', type=int, default=100, choices=range(50, 1001, 50), help='Speed of grid updates in milliseconds')
    parser.add_argument('--debug', action='store_true', help='Enable Debugging Prints')
    
    args = parser.parse_args()
    
    if args.gui:
        root = tk.Tk()
        app = GridTraversalApp(root, args.rows, args.columns, traversal_functions, args.debug, args.speed)
        root.mainloop()
    else:
        grid = [[val for val in range(args.columns * row, args.columns * (row + 1))] for row in range(args.rows) ]
        print("[")
        for row in grid:
            print("\t[", end=" ")
            for val in row:
                print(f"{val:3}", end=" ")
            print("]")
        print("]")
        print()
        
        if args.debug:
            print("Debug:", traversal_functions[args.traversal](grid))
            print()
        
        print("Traversal:", args.traversal)
        print()
        for row, col in traversal_functions[args.traversal](grid):
            print(grid[row][col], end=" ")
