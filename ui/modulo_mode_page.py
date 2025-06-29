import tkinter as tk
from tkinter import ttk, filedialog
from shared.exceptions import ValidationException
from ui.components.button import Button
from shared.models.Ring import Ring
import modules.checker as Checker
from PIL import ImageTk
from ui.components.latex import LatexLabel 

class ModuloModePage(tk.Frame):
    def __init__(self, parent, on_value_change, on_submit):
        super().__init__(parent)
        self.var = tk.IntVar(value = 1)

        self.latex_label = LatexLabel(self, latex_fn = lambda: rf"$ℤ_{{{self.var.get()}}}$")
        self.latex_label.pack(pady = 12)

        tk.Label(self, text="Enter modulo number: ").pack(pady=(10, 0));
        spin = tk.Spinbox(self, from_ = 1, to = 100, textvariable = self.var, command = self._on_change)
        spin.pack( pady = 5 )

        button = Button(self, text = "Enter", command = self._on_submit)
        button.pack(padx = 12, fill="none")

        self.on_value_change = on_value_change
        self.on_submit = on_submit

        self.ring = Ring(self.var.get())


    def _on_change(self):
        self.latex_label.update_latex() 
        if self.on_value_change:
            return self.on_value_change
    def _on_submit(self):

        try:
            self.ring = Ring(self.var.get())
            result = Checker.check_all_properties(self.ring)
        except ValidationException as e:
            result = e.message
        
        if self.on_submit:
            return self.on_submit(result)

    def get_value(self):
        return self.var.get()
