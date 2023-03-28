import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from price_to_word_conv import num_to_word
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty, ObjectProperty, Clock
from kivy.core.window import Window

kivy.require('2.1.0')



class MainWidget(BoxLayout):
    rubles_input = ObjectProperty(None)
    kopeeks_input = ObjectProperty(None)


    def get_data(self):
        rubles = ''.join(self.rubles_input.text.split())
        kopeeks = self.kopeeks_input.text
        return rubles, kopeeks
    def run_converter(self):
        rubles, kop = self.get_data()
        print(rubles, kop)
        try:
            result = num_to_word(int(rubles),int(kop))
            self.output.text = str(result)

        except ValueError:
            self.output.text = 'Enter a correct value'


class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_filter = 'int' # Set value using the default property.

    def insert_text(self, substring, from_undo = False):
        # Override this super-class method.
        if not substring.isdigit(): # Eliminates non digit character.
            return
        else:
            cc, cr = self.cursor
            text = self._lines[cr]
            new_text = text[:cc] + substring + text[cc:]
            int_str = new_text.replace(" ", "") # Removing any inbetween space.
            new_text = '{:,d}'.format(int(int_str)).replace(",", " ") # Here insert seperator.
            super().insert_text(substring, from_undo = from_undo)

            self._set_line_text(cr, new_text) # Super-class method.
            Clock.schedule_once(lambda dt : setattr(self, "cursor", (cc+2, cr))) # Advances the cursor

    def multiplication(self):
        # First remove any inbetween space.
        num_text_1 = self.first_num.text.replace(" ", "")
        num_text_2 = self.second_num.text.replace(" ", "")
        if num_text_1 and num_text_2:  # Non empty values.
            x = int(num_text_1)
            y = int(num_text_2)
            self.result.text = '{:,}'.format(int(x * y)).replace(",", " ")
        else:
            self.result.text = ""  # Or, any other message.


class MyNumToWordConvApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MyNumToWordConvApp().run()
