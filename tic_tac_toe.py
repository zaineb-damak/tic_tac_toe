import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

class TikTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display=tk.Label(
            master=display_frame,
            text="Ready?"
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):   
            self.rowconfigure(row, weight=1, minsize=50)
            self.rowconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    width=3,
                    height=2
                )
                self._cells[button]=(row,col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

class Player(NamedTuple):
     label: str
     color: str

class Move(NamedTuple):
     row: int
     col: int
     label: str     

class TicTacToeGame:
    BOARD_SIZE=3
    
    DEFAULT_PLAYERS = (
        Player(label="X", color="blue"),
        Player(label="O", color="green")
    )
    def __init__(self, players= DEFAULT_PLAYERS, board_size=BOARD_SIZE):
          self._players= cycle(players)
          self.current_player = next(self._players)
          self.winner_combo = []
          self._current_moves = []
          self._has_winner = False
          self._winning_combos = []
          self._setup_board()

    def _setup_board():
         return
    
    
            
def main():
        board = TikTacToeBoard()
        board.mainloop()

if __name__ =="__main__":
        main()
