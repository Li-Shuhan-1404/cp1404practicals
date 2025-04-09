from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_km = "0.0"

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """ handle calculation (could be button press or other call), output result to label widget """
        miles = self.convert_to_number(text)
        self.update_result(float(miles))

    def handle_increment(self, text, change):
        """handle up/down button press, update the text input with new value, call calculation function"""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        """Convert mile to kilometer"""
        self.output_km = str(miles * MILES_TO_KM)
        self.root.ids.output_label.text = self.output_km

    @staticmethod
    def convert_to_number(text):
        """get text input from text entry widget, convert to float"""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
