"""
This is an example using Kaki with Kivy modules.
"""

from kaki.app import App
from kivy.clock import Clock
from kivy.factory import Factory


from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

from ScreenThree.calculator import Calculator


class SM(ScreenManager):
    """A `ScreenManager` that manages the screens for the BillAssistant app."""

    def current_screen_name(self):
        return self.current_screen.name


class Splash(MDScreen):
    pass


# main app class for kaki app with kivy style
class Main(MDApp, App):
    # root app name/title
    name = "Hot Reload"

    # version number
    vernum = "0.1.4"

    # window title
    title = "%s v%s" % (name, vernum)

    # by default it will return to False
    # set this to True so you can make a change to your .kv file
    DEBUG = True
    # *.kv files to watch
    KV_FILES = [
        # screen manager
        "main.kv",
        # screen
        "ScreenTwo/bill_mode.kv",
        "ScreenOne/select_mode.kv",
        "ScreenThree/calculator.kv",
        "WelcomeScreen/welcome_screen.kv",
    ]

    # class to watch
    CLASSES = {
        # screen manager
        "SM": "main",
        # screens
        "BillMode": "ScreenTwo.bill_mode",
        "Welcome": "WelcomeScreen.welcome_screen",
        "Splash": "main",
        "SelectMode": "ScreenOne.select_mode",
        "Calculator": "ScreenThree.calculator",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    sm = None

    # build app
    def build_app(self):
        self.sm = Factory.SM()
        self.title = "BillAssistant"
        self.icon = "images/icon.jpeg"
        self.sm.current = "Splash"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.accent_palette = "BlueGray"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.95

        FMS = self.sm

        return FMS

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

    def current_screen_name(self, screen_name):
        Calculator.current_screen_name = screen_name


# launch the app
if __name__ == "__main__":
    Main().run()
