import tkinter as tk
from shared.models import Ring
from ui.components.array_input import ArrayInput
from ui.components.button import Button
from ui.components.label import Label
import modules.checker import Checker

class MatrixInputPage(tk.Frame):
    def __init__(self, parent, on_submit):
        super().__init__(parent)

        self.size_var = tk.IntVar(value = 3)
        self.on_submit = on_submit

        frame_input_size = tk.Frame(self)

        Label(frame_input_size, text = "Elements :").pack(side = "left")
        
        input_elements = ArrayInput(frame_input_size, on_add = self._on_elements)
        input_elements.pack(side = "left")

        self.elements = []
        
        frame_input_size.pack()


        self.frame = tk.Frame(self, bg="#e0e0e0")
        self.frame.pack(fill = "both", expand = True, padx = 12, pady = 12)
        self.frame.pack_propagate(False)
        self.rows = self.cols = self.size_var.get()
        self.entries = []

        self._draw_matrix()

        submit = Button(self, text = "Check", command = self._on_submit)
        submit.pack(fill="x", padx = 4, pady = 4)



    def _on_submit(self):
        ring = Ring(elements = self.elements, mul)

        pass

    def _on_elements(self, value) -> None:
        length = value.__len__()
        self.elements = value

        self.rows = self.cols = length
        self._draw_matrix()


    def _on_resize(self):
        try:
            new_size = int(self.size_var.get())
            if new_size > 0:
                self.rows = self.cols = new_size
                self._draw_matrix()
        except ValueError:
            pass


    def _draw_matrix(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.entries = []

        for i in range(50):  # arbitrary max
            self.frame.grid_rowconfigure(i, weight=0)
            self.frame.grid_columnconfigure(i, weight=0)

        for r in range(self.rows):
            self.frame.grid_rowconfigure(r, weight=1)
            row_entries = []
            for c in range(self.cols):
                self.frame.grid_columnconfigure(c, weight=1)
                entry = tk.Entry(self.frame, justify="center")
                
                entry.grid(row=r, column=c, padx=4, pady=4)
                entry.configure(width=4)  # approx character width; actual size also depends on font
                row_entries.append(entry)
            self.entries.append(row_entries)



    def update_size(self, new_size):
        self.cols = self.rows = new_size
        self._draw_matrix()

    def get_matrix(self):
        return [[entry.get() for entry in row] for row in self.entries]
