from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0.5, 0, 1)
ALTERNATIVE_COLOUR = (1, 0, 1, 1)


class DynamicLabelsApp(App):
    """Main app for dynamic label creation"""
    name_display = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name and add to the GUI"""
        for name in self.names:
            temp_label = Label(text=name, font_size='30sp')
            temp_label.color = NEW_COLOUR
            self.root.ids.label_box.add_widget(temp_label)


DynamicLabelsApp().run()
