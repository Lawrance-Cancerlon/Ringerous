import tkinter as tk


# Define button component
class Button(tk.Frame):
    def __init__(self, parent, text="Button", command=None, **kwargs):
        super().__init__(parent)

        # May overriden by kewags
        style = {"font": ("Arial", 12), "padx": 12, "pady": 4}

        args = {**style, **kwargs}

        self.button = tk.Button(parent, text=text, command=command, **args)
        self.button.pack(fill="both", expand=True)
