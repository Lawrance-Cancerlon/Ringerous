import unittest
from unittest.mock import Mock
from ui.components.button import Button
import tkinter as tk


class TestButton(unittest.TestCase):
    def setUp(self) -> None:
        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self) -> None:
        self.root.destroy()

    def test_button_text(self) -> None:
        btn = Button(self.root, text="Test")
        self.assertEqual(btn.button["text"], "Test")

    def test_button_command(self) -> None:
        cmd = Mock()

        btn = Button(self.root, command=cmd)
        btn.button.invoke()
        cmd.assert_called_once()


if __name__ == "__main__":
    unittest.main()
