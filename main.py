import kivy
kivy.require('2.0.0')
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from main_screen import MainScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem



class NotebookApp(MDApp):
    title = 'Блокнот'

    def build(self):
        return Builder.load_file('app.kv') #MainScreen()

    def set_list(self):
        for i in range(10):
            self.root.ids.notes_list.add_widget(
                OneLineListItem(text=f'Item {i+1}')
            )

    def on_start(self):
        self.set_list()

if __name__ == '__main__':
    NotebookApp().run()