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


from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

from apputils import load_kv

load_kv(__name__)


class NavBar(CommonElevationBehavior, MDFloatLayout):
    pass


class BillMode(MDScreen):
    def on_pre_enter(self):  # pylint: disable=arguments-differ
        self.ids.five_hundred_euro_Note.focus = True
