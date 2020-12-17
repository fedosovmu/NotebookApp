from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        label1 = Label(text='Hello world')
        self.add_widget(label1)

        label2 = Label(text='Ololol olol')
        self.add_widget(label2)
