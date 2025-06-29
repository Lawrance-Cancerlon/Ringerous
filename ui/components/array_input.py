
import tkinter as tk

class ArrayInput(tk.Frame):
    def __init__(self, parent, placeholder="1, 2, 3", on_add=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.on_add = on_add  # callback function
        self.var = tk.StringVar()
        self.var.trace_add("write", self._on_change)

        self.entry = tk.Entry(self, textvariable=self.var, width=30)
        self.entry.insert(0, placeholder)
        self.entry.pack(fill="x", expand=True)


    def get(self, value_type=str):
        raw = self.var.get()
        try:
            return [value_type(item.strip()) for item in raw.split(",") if item.strip() != ""]
        except ValueError:
            return []

    def _on_change(self, *_):
        current = self.get()
        if self.on_add :
            self.on_add(current)
