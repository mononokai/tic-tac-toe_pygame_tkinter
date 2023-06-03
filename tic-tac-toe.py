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
