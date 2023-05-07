"""_summary_
"""
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from apputils import load_kv

load_kv(__name__)


class NavBar(CommonElevationBehavior, MDFloatLayout):
    pass


class Calculator(MDScreen):
    pass
