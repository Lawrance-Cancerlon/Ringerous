import tkinter as tk
from tkinter import ttk
from ui.components.flex_container import FlexContainer
from ui.components.radio_group import RadioGroup
from ui.components.text_card import TextCard
from ui.matrix_mode_page import MatrixInputPage
from ui.modulo_mode_page import ModuloModePage


class Index(tk.Frame):
    options = ["integer", "table"]

    def __init__(self, parent, **kwargs) -> None:
        super().__init__()

        """ Module var """
        self.modulo = tk.IntVar(parent, value = 1)
        
        self.main = FlexContainer(parent, direction = "row", gap = 12)
        self._left_panel(self.main)
        self._right_panel(self.main)
        self.main.add(self.panel_left)
        self.main.add(self.panel_right)
        self.main.pack()


    def _left_panel(self, parent) -> None:
        self.panel_left = FlexContainer(parent, direction = "column", gap = 8)

        self.title = tk.Label(self.panel_left, text = "Ringorous | Check your rings for rings")
        self.title.pack(pady = 12)

        self.notebook = ttk.Notebook(self.panel_left)
        self.notebook.pack(fill="none", expand=False, padx=12, pady=8)

        # Number input page
        self.page1 = ModuloModePage(self.panel_left, on_value_change=self._on_modulo_change, on_submit=self._update_result)
        self.notebook.add(self.page1, text="Modulo Integer")

        # Matrix input page
        self.page2 = MatrixInputPage(self.panel_left, on_submit = self._update_result)
        self.notebook.add(self.page2, text="Custom Binary Table")
        self.panel_left.pack()



    def _right_panel(self, parent) -> None:
        self.panel_right = FlexContainer(parent, direction = "column", gap = 8)

        self.result_pane = TextCard(self.panel_right)

        self.result_pane.pack()
        self.panel_right.pack()


    def _update_result(self, lines) -> None:
        self.result_pane.render(lines)


    def _on_modulo_change(self, new_value):
        self.modulo = new_value
