import tkinter as tk
from tkinter import ttk


class PageContainer(ttk.Notebook):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pages = {}

    def add_page(self, title, frame=None):
        frame = frame or tk.Frame(self)
        self.add(frame, text=title)
        self.pages[title] = frame
        return frame

    def get_page(self, title):
        return self.pages.get(title)
