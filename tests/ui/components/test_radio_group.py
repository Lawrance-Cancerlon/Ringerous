import unittest
from unittest.mock import Mock
from ui.components.radio_group import RadioGroup
import tkinter as tk


class TestRadioGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self) -> None:
        self.root.destroy()

    # Assert test default value set
    def test_radio_default_value(self) -> None:
        options = ["A", "B"]
        radio = RadioGroup(self.root, options=options, default="A")

        self.assertEqual(radio.get_value(), "A")

    # Test setter
    def test_radio_set_value(self) -> None:
        options = [1, 2, 3]
        radio = RadioGroup(self.root, options=options, default=1)

        radio.set_value(options[0])
        self.assertEqual(radio.get_value(), str(options[0]))

    def test_on_change_callback(self) -> None:
        callback = Mock()

        options = [1, 2]
        radio = RadioGroup(
            self.root, options=options, default=options[0], command=callback
        )
        radio.set_value(options[1])
        radio._on_change()
        callback.assert_called_with(str(options[1]))


if __name__ == "__main__":
    unittest.main()
