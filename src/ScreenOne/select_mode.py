"""
Select mode screen where users choose whether to enter
Calculator mode or Bill mode.
"""

from kivymd.uix.screen import MDScreen
from apputils import load_kv


load_kv("ScreenOne/select_mode.kv")


class SelectMode(MDScreen):
    """
    A screen widget that displays two buttons, allowing users to select between
    Calculator mode and Bill mode.

    Methods
    -------
    None
    """

    pass
