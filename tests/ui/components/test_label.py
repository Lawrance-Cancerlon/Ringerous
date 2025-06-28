import unittest
from unittest.mock import Mock
from ui.components.label import Label
import tkinter as tk


class TestLabel(unittest.TestCase):
    def setUp(self) -> None:
        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self) -> None:
        self.root.destroy()

    # Assert test label's text
    def test_label_text(self) -> None:
        label = Label(self.root, text="Test")

        self.assertEqual(label.label["text"], "Test")
