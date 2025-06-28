import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import io

class LatexLabel(tk.Label):
    def __init__(self, parent, latex_fn, **kwargs):
        super().__init__(parent, **kwargs)
        self.latex_fn = latex_fn
        self.image_ref = None
        self.update_latex()

    def update_latex(self):
        latex_str = self.latex_fn()
        img = self.render_latex_to_image(latex_str)
        self.image_ref = ImageTk.PhotoImage(img)
        self.config(image=self.image_ref)


    def render_latex_to_image(self, latex_str):
        fig, ax = plt.subplots(figsize=(1, 1))
        ax.text(0.5, 0.5, latex_str, fontsize=20, ha='center', va='center')
        ax.axis('off')

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=150)
        buf.seek(0)
        img = Image.open(buf)
        plt.close(fig)
        return img

