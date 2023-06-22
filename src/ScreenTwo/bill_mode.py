"""
Bill mode screen that allows users to input values and calculate the total
value of money notes.

The class inherits from `MDScreen`, which is a KivyMD class for a full-screen
layout widget.

Attributes:
----------
None

Methods:
-------
None
"""
from kivymd.uix.screen import MDScreen
from apputils import load_kv

load_kv("ScreenTwo/bill_mode.kv")


class BillMode(MDScreen):
    """
    A screen for handling bill-related functionality.

    Methods
    -------
    on_pre_enter(*args)
        Sets the focus to the 500 euro note input field
        when the screen is entered.
    """

    def on_pre_enter(self, *args):
        self.ids.five_hundred_euro_Note.focus = True

    def truncate_text(self, text_field_id, max_length=10):
        """Truncate the text in a text field if it exceeds a certain length.

        Args:
            text_field_id (MDTextField): _description_
            max_length (int, optional): _description_. Defaults to 10.
        """
        if len(text_field_id.text) > max_length:
            text_field_id.text = text_field_id.text[:max_length]
        text_field_id.text = text_field_id.text
