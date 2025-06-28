import tkinter as tk


class TableInput(tk.Frame):
    def __init__(self, parent, on_change = None):
        super().__init__(parent)

        self.size_var = tk.IntVar(value = 3)
        self.on_change = on_change

    def update_size(self, size) -> None:
        self.size_var.set(size)
