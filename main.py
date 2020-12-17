import kivy
kivy.require('2.0.0')
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from main_screen import MainScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.label import Label


class NotebookApp(MDApp):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    NotebookApp().run()