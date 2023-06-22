"""_summary_
"""
import keyboard
import win32api
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from apputils import load_kv


load_kv("ScreenThree\calculator.kv")


class Calculator(MDScreen):
    current_screen_name = "None"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        keyboard.on_press(self.on_key_press)
        # Enable Num Lock if it's not already enabled
        self.enable_num_lock()

    @staticmethod
    def truncate_text(text, max_length=20):
        if len(text) > max_length:
            return text[:max_length] + "..."
        return text

    def clear(self):
        """this function clear the TextInput when the
        c button is pressed
        """
        self.ids.calc_input.text = "0"
        self.ids.answer.text = "0"

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

        if prior == "0" or (prior[-1] == "="):
            self.ids.calc_input.text = f"{num}"
            self.ids.answer.text = "0"
        else:
            self.ids.calc_input.text = self.truncate_text(f"{prior}{num}")

    def math_sign(self, sign):
        """
            all the math signs function
        Returns:
            _type_: _description_
        """
        # get the number/s the is already in the TextInput
        prior = self.ids.calc_input.text
        if prior.endswith("..."):
            pass
        else:
            try:
                if prior[-1] == "=":
                    prior = self.ids.answer.text
                elif prior[-1] in ["+", "*", "/"]:
                    pass
                else:
                    text = self.truncate_text(f"{prior}{sign}")
                    self.ids.calc_input.text = text
                answer = eval(prior)  # pylint: disable=eval-used
                self.ids.answer.text = f"{answer}"  # pylint: disable=eval-used
            except (Exception, NameError):  # pylint: disable=broad-except
                self.ids.answer.text = "Invalid Input"

    def other_sign(self, sign):
        prior = self.ids.calc_input.text
        if sign == "Ans" and self.ids.answer.text != "Invalid Input":
            self.ids.calc_input.text = self.ids.answer.text
            self.ids.answer.text = "0"
        elif sign == "Ans" and self.ids.answer.text == "Invalid Input":
            self.ids.calc_input.text = "0"
            self.ids.answer.text = "0"
        else:
            last_character = prior.split()[-1]
            if "." in last_character and sign == ".":
                pass
            elif sign == "-" and (last_character == ""
                                  or last_character == "-"):
                self.ids.calc_input.text += sign
            else:
                self.ids.calc_input.text += sign

    # create equals to function

    def equals(self):
        """
        equals function
        """
        try:
            prior = self.ids.calc_input.text
            answer = eval(prior)  # pylint: disable=eval-used
            self.ids.calc_input.text = f"{prior} ="
            self.ids.answer.text = self.truncate_text(str(answer))
        except ZeroDivisionError:
            self.ids.answer.text = "Division by zero is not allowed"
        except (Exception, NameError):  # pylint: disable=broad-except
            self.ids.answer.text = "Invalid Input"

    def backspace(self):
        """
        backspace function
        """
        prior = self.ids.calc_input.text
        if "ERROR" in prior:
            prior = ""

        length = len(prior)
        if length == 1 or length == 0:
            self.ids.calc_input.text = "0"
        elif prior[-1] == " ":
            self.ids.calc_input.text = f"{prior[:length-2]}"
        elif prior.endswith("..."):
            self.ids.calc_input.text = f"{prior[:length-3]}"
        else:
            self.ids.calc_input.text = f"{prior[:length-1]}"

    def on_key_press(self, event):
        if Window.focus and self.current_screen_name == "Calculator":
            # Process the key press event
            num_lock_keys = [str(i) for i in range(10)]
            operators = [
                "*",
                "+",
                "-",
                "decimal",
                "/",
                "enter",
                "backspace",
            ]

            if event.name in num_lock_keys:
                key = str(event.name)
                Clock.schedule_once(lambda dt: self.button_press(key), 0)

            if event.name in operators:
                key = str(event.name)
                if key == "enter":
                    Clock.schedule_once(lambda dt: self.equals(), 0)
                elif key == "backspace":
                    Clock.schedule_once(lambda dt: self.backspace(), 0)
                elif key == "decimal":
                    Clock.schedule_once(lambda dt: self.other_sign("."), 0)
                else:
                    Clock.schedule_once(lambda dt: self.math_sign(key), 0)

    def enable_num_lock(self):  # pylint: disable=no-self-argument
        if not (win32api.GetKeyState(0x90) & 1):
            # Simulate pressing and releasing the Num Lock key
            win32api.keybd_event(0x90, 0, 0, 0)
            win32api.keybd_event(0x90, 0, 2, 0)
