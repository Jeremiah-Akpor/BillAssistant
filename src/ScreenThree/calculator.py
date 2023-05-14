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

    def on_pre_enter(self):
        self.ids.calc_input.focus = True

    def clear(self):
        """this function clear the TextInput when the
        c button is pressed
        """
        self.ids.calc_input.text = ""
        self.ids.answer.text = ""

    # create a button pressing function
    def button_press(self, num):
        """
        updates the TextInput with the numbers

        Args:
            button (_type_): _description_

        Returns:
            _type_: _description_
        """
        # get the number/s the is already in the TextInput
        prior = self.ids.calc_input.text

        if "ERROR" in prior:
            prior = ""

        if prior == "0":
            self.ids.calc_input.text = f"{num}"
        else:
            self.ids.calc_input.text = f"{prior}{num}"

    def math_sign(self, sign):
        """
            all the math signs function
        Returns:
            _type_: _description_
        """

        # get the number/s the is already in the TextInput
        prior = self.ids.calc_input.text
        if prior.endswith(" / ") or prior.endswith(" * "):
            self.ids.calc_input.text = f"{prior[:-1]}{sign} "
        else:
            # concat the Text box with the math sign
            self.ids.calc_input.text = f"{prior} {sign} "

    def other_sign(self, sign):
        """
            add other signs like dot and negative to the
            text input
        Returns:
            _type_: _description_
        """
        # get the number/s the is already in the TextInput
        prior = self.ids.calc_input.text
        if sign == "Ans" and self.ids.answer.text != "Invalid Input":
            self.ids.calc_input.text = self.ids.answer.text
            self.ids.answer.text = ""
        elif sign == "Ans" and self.ids.answer.text == "Invalid Input":
            self.ids.calc_input.text = ""
            self.ids.answer.text = ""
        else:
            if "." in prior.split(" ")[-1] and sign == ".":
                pass
            elif prior[0] == "-" and sign == "-":
                self.ids.calc_input.text = f"{prior[1:]}"
            elif prior[0] != "-" and sign == "-":
                self.ids.calc_input.text = f"{sign}{prior}"
            else:
                # concat the Text box with the sign
                self.ids.calc_input.text = f"{prior}{sign}"

    # create equals to function

    def equals(self):
        """
        equals function
        """
        try:
            prior = self.ids.calc_input.text
            answer = eval(prior)  # pylint: disable=eval-used
            # print answer in the text box
            self.ids.answer.text = f"{answer}"
        except (Exception, NameError):  # pylint: disable=broad-except
            # print answer in the text box
            self.ids.answer.text = "Invalid Input"

    def backspace(self):
        """
        backspace function
        """
        prior = self.ids.calc_input.text
        if "ERROR" in prior:
            prior = ""

        length = len(prior)
        if length == 1:
            self.ids.calc_input.text = "0"
        elif prior[-1] == " ":
            self.ids.calc_input.text = f"{prior[:length-2]}"
        else:
            self.ids.calc_input.text = f"{prior[:length-1]}"
            
