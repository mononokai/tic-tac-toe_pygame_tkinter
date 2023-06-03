import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        # non-public dictionary for cells of the board
        self._cells = {}
    
    def _create_board_display(self):
        # create the frame for display
        display_frame = tk.Frame(master=self)
        # .pack() is a geometry manager being used to fill the frame to the window
        display_frame.pack(fill=tk.X)
        # the label object must be inside the frame object, which is why it references the display_frame itself as "master"
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        # packing the display label in the frame
        self.display.pack()

    def _create_board_grid(self):
        # create a grid of the cells
        grid_frame = tk.Frame(master=self)
        # place the Frame object on the window
        grid_frame.pack()
        # loop from 0-2 to get row coordinates
        for row in range(3):
            # configure size of rows and columns
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            # loop through the column coordinates to create buttons for each cell in the grid
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                # add the buttons to the ._cells dictionary with buttons being keys and row/col numbers being values
                self._cells[button] = (row, col)
                # add each button to the window with some styling
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew",
                )
