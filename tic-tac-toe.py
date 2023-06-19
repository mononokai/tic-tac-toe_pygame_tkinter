import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple


# Player class
class Player(NamedTuple):
    label: str
    color: str


# Player move class
class Move(NamedTuple):
    row: int
    col: int
    label: str = ""


BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)


class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic-Tac-Toe")
        # non-public dictionary for cells of the board
        self._cells = {}
        self._game = game
        self._create_board_display()
        self._create_board_grid()
    
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
        for row in range(self._game.board_size):
            # configure size of rows and columns
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            # loop through the column coordinates to create buttons for each cell in the grid
            for col in range(self._game.board_size):
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
                # bind the buttons to the play() method
                button.bind("<ButtonPress-1>", self.play)
                # add each button to the window with some styling
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew",
                )
        def play(self, event):
            clicked_button = event.widget
            row, col = self._cells[clicked_button]
            move = Move(row, col, self._game.current_player.label)
            if self._game.is_valid_move(move):
                self._update_button(clicked_button)
                self._game.process_move(move)
                if self._game.is_tied():
                    self._update_display(msg="Tie game!", color="red")
                elif self._game.has_winner():
                    self._highlight_cells()
                    msd = f"{self._game.current_player.label} won!"
                    color = self._game.current_player.color
                    self._update_display(msg, color)
                else:
                    self._game.toggle_player
                    msg = f"{self._game.current_player.label}'s turn"
                    self._update_display(msg)


class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self.players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self.players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self.__current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]
    
    def is_valid_move(self, move):
        row = move.row
        col = move.col
        move_was_not_played = self.__current_moves[row][col].label == ""
        no_winner = not self.__has_winner
        return no_winner and move_was_not_played
        
    def process_move(self, move):
        row, col = move.row, move.col
        self.__current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(
                self.__current_moves[n][m].label
                for n, m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        return self._has_winner
    
    def is_tied(self):
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)
    
    def toggle_player(self):
        self.current_player = next(self.players)


def main():
    board = TicTacToeBoard()
    board.mainloop()


if __name__ == "__main__":
    main()