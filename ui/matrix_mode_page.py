import tkinter as tk
from shared.models.Ring import Ring
from ui.components.array_input import ArrayInput
from ui.components.button import Button
from ui.components.label import Label
import modules.checker as Checker
from ui.components.table_input import TableInput

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


        addition_frame = tk.Frame(self)
        Label(addition_frame, "Addition operation").pack()
        self.addition_table = TableInput(addition_frame)
        self.addition_table.pack()
        addition_frame.pack()

        multiplication_frame = tk.Frame(self)
        Label(multiplication_frame, "Multiplication operation").pack()
        self.multiplication_table = TableInput(multiplication_frame)
        self.multiplication_table.pack()
        multiplication_frame.pack()

        submit = Button(self, text = "Check", command = self._on_submit)
        submit.pack(fill="x", padx = 4, pady = 4)



    def _on_submit(self):
        addition = self.addition_table.get_matrix()
        multiplication = self.multiplication_table.get_matrix()

        ring = Ring(elements = self.elements, mul_table = multiplication, add_table = addition)
        results = Checker.check_all_properties(ring)

        self.on_submit(results)



        pass

    def _on_elements(self, value) -> None:
        length = value.__len__()
        self.elements = value
        print(self.elements)
        self.addition_table.resize(length)
        self.multiplication_table.resize(length)


