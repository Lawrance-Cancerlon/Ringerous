import unittest
import tkinter as tk
from ui.components.text_card import TextCard


class TestTextCard(unittest.TestCase):
    def setUp(self):

        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self):
        self.root.destroy()


    def test_lines(self):
        lines = [
            "Hello",
            "Test"
        ]
        text_card = TextCard(self.root, lines = lines)

        text_card.pack()

        self.assertEqual(
            text_card.winfo_children()[0]['text'], "Hello"
        )




