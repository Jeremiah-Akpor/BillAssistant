"""
This module contains the `SM` and `MainApp` classes for the BillBuddy app.
"""

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp


class SM(ScreenManager):
    """A `ScreenManager` that manages the screens for the BillBuddy app."""


class MainApp(MDApp):
    """The main class for the BillBuddy app."""

    sm = None

    def build(self):
        """Build the app UI.

        Returns:
            `SM`: The root `SM` object representing the app UI.
        """
        self.sm = SM()
        self.sm.current = "SelectMode"
        self.title = "BillBuddy"
        self.icon = "images/icon.jpeg"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.accent_palette = "Red"
        return self.sm

    def toggle_theme(self, is_dark):
        """Toggle the app's theme.

        Args:
            is_dark (`bool`): Whether to switch to dark mode.
        """
        self.theme_cls.theme_style = "Dark" if is_dark else "Light"


if __name__ == "__main__":
    app = MainApp()
    app.run()
