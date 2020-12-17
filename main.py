import kivy
kivy.require('2.0.0')
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from main_screen import MainScreen
from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"

    MDLabel:
        text: "Content"
        halign: "center"
'''

class NotebookApp(MDApp):
    def build(self):
        return Builder.load_string(KV) #MainScreen()


if __name__ == '__main__':
    NotebookApp().run()