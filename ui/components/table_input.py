import tkinter as tk


class TableInput(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.size_var = tk.IntVar(value = 3)



        self.frame = tk.Frame(self, bg="#e0e0e0")
        self.frame.pack(fill = "both", expand = True, padx = 12, pady = 12)
        self.frame.pack_propagate(False)
        self.rows = self.cols = self.size_var.get()
        self.entries = []



    def resize(self, size) -> None:
        self.size_var.set(size)
        self._draw_matrix()



    def _draw_matrix(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.entries = []

        for i in range(50):  # arbitrary max
            self.frame.grid_rowconfigure(i, weight=0)
            self.frame.grid_columnconfigure(i, weight=0)

        for r in range(self.size_var.get()):
            self.frame.grid_rowconfigure(r, weight=1)
            row_entries = []
            for c in range(self.size_var.get()):
                self.frame.grid_columnconfigure(c, weight=1)
                entry = tk.Entry(self.frame, justify="center")
                
                entry.grid(row=r, column=c, padx=4, pady=4)
                entry.configure(width=4)  # approx character width; actual size also depends on font
                row_entries.append(entry)
            self.entries.append(row_entries)


    def get_matrix(self):
        return [[entry.get() for entry in row] for row in self.entries]


