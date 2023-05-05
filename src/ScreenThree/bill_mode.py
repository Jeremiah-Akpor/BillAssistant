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

load_kv(__name__)


class BillMode(MDScreen):
    pass
