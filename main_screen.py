from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label


class MainScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        label1 = MDLabel(text='Hello world', halign='center')
        self.add_widget(label1)

        label2 = MDLabel(text='Ololol olol', halign='center')
        self.add_widget(label2)