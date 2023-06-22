"""
This module contains the `SM` and `MainApp` classes for the BillAssistant app.
"""
import os
import sys
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.resources import resource_add_path, resource_find
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

from ScreenThree.calculator import Calculator


class SM(ScreenManager):
    """A `ScreenManager` that manages the screens for the BillAssistant app."""


class Splash(MDScreen):
    pass


class MainApp(MDApp):
    """The main class for the BillAssistant app."""

    sm = None

    def build(self):
        """Build the app UI.

        Returns:
            `SM`: The root `SM` object representing the app UI.
        """
        # Set the desired window size
        Window.size = (1000, 700)
        self.sm = SM()
        self.title = "BillAssistant"
        self.icon = "images/icon.jpeg"
        self.sm.current = "Splash"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.accent_palette = "BlueGray"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.95
        return self.sm

    def on_start(self):
        Clock.schedule_once(self.welcome, 5)

    def welcome(self, *args):  # pylint: disable=unused-argument
        self.sm.current = "Welcome"

    def toggle_theme(self, is_dark):
        """Toggle the app's theme.

        Args:
            is_dark (`bool`): Whether to switch to dark mode.
        """
        self.theme_cls.theme_style = "Dark" if is_dark else "Light"

    def calculate(self, total_id, money_note: str, amount: MDTextField):
        try:
            amount = int(amount.text)
            total = money_note * amount
            total_id.text = str(total)
        except ValueError:
            # Handle the case where money_note or amount
            # cannot be converted to integers
            if amount.text == "":
                total_id.text = "0"
            else:
                total_id.text = "Invalid input"

    def focus_next(self, textfield_id):
        textfield_id.focus = True

    def total_sum(self, notes: list, total_label_id):
        total = sum(int(textfield.text) for textfield in notes)
        total_label_id.text = str(total)

    def clear_all(self, notes: list):
        for note in notes:
            note.text = ""

    def current_screen_name(self, screen_name):
        Calculator.current_screen_name = screen_name


if __name__ == "__main__":
    try:
        if hasattr(sys, "_MEIPASS"):
            resource_add_path(os.path.join(sys._MEIPASS))
        app = MainApp()
        app.run()
    except Exception as e:
        print(e)
        input("Press enter.")
