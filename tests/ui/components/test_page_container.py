import unittest
from ui.components.page_container import PageContainer
import tkinter as tk


class TestPageContainer(unittest.TestCase):
    def setUp(self) -> None:
        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self) -> None:
        self.root.destroy()

    def test_add_page(self) -> None:
        pages = PageContainer(self.root)

        frame = tk.Frame()
        button = tk.Button(frame, text="Test")
        button.pack()
        frame.pack()

        pages.add_page("Test Page", frame)
        child = pages.get_page("Test Page")
        button = [w for w in child.winfo_children() if isinstance(w, tk.Button)]
        self.assertEqual(button[0]["text"], "Test")
