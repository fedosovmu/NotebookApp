import kivy
kivy.require('2.0.0')
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel


Builder.load_file('app.kv')


class NotesListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label1 = MDLabel(text='Hello world', halign='center')
        self.add_widget(label1)

    def test_event(self):
        print('test event')

class NoteScreen(Screen):
    pass


class NotebookApp(MDApp):
    title = 'Блокнот'

    def build(self):
        sm = ScreenManager()
        sm.add_widget(NotesListScreen(name='main'))
        sm.add_widget(NoteScreen(name='note'))
        return sm

    def set_list(self):
        for i in range(10):
            self.root.ids.notes_list.add_widget(
                OneLineListItem(text=f'Item {i+1}')
            )

    def on_start(self):
        pass #self.set_list()

if __name__ == '__main__':
    NotebookApp().run()