from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Run the program"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Convert input to output format"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_text(self, input_name):
        """Clear input and output"""
        self.root.ids.output_label.text = ""
        input_name.text = ""

BoxLayoutDemo().run()
