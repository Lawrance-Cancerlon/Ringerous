import tkinter as tk


# Define a label component
class Label(tk.Frame):
    def __init__(self, parent, text="Label", **kwargs):
        super().__init__(parent)

        self.label = tk.Label(parent, text=text, font=("Arial", 14), **kwargs)
        self.label.pack()
