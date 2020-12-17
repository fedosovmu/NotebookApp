from main_screen import MainScreen
from kivy.app import App
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class NotebookApp(MDApp):
    def build(self):
        return MDLabel(text='Hello world!', halign='center') #MainScreen()


if __name__ == '__main__':
    NotebookApp().run()