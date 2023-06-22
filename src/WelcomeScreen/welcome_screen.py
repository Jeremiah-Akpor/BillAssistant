"""
    this is the welcome screen
"""

from kivymd.uix.screen import MDScreen
from apputils import load_kv


load_kv("WelcomeScreen/welcome_screen.kv")


class Welcome(MDScreen):
    pass
