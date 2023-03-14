import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.cells = {}
    def _create_board_display():
        diplay_frame = tk.Frame(master = self)
        display_frame.pack(fill=tk.X)
        self.display = tk.label(
            master = display_frame,
            text="Ready?",
            font=font.Font(size=28,weight="bold"),
        )
        self.display.pack()
    def _create_board_grid_(self):
        grid_frame_ = tk.Frame(master=self)
        grid_frame.pack()
        
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for column in range(3):
                


