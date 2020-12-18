import config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel


class MainScreen(Screen):
    def main_screen_test(self):
        print('main screen test')

    def load_list(self):
        for i in range(10):
            self.ids.notes_list.add_widget(
                OneLineListItem(text=f'Item {i+1}')
            )


class NoteScreen(Screen):
    def note_screen_test(self):
        print('note screen test')


class NotebookApp(MDApp):
    def __init__(self, **kwargs):
        super(NotebookApp, self).__init__(**kwargs)
        self.title = 'Блокнот'


    def build(self):
        Builder.load_file('app.kv')
        self.main_screen = MainScreen(name='main')
        self.note_screen = NoteScreen(name='note')
        self.sm = ScreenManager()
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.note_screen)
        return self.sm

    def go_to_note_screen(self):
        self.main_screen.manager.transition.direction = 'left'
        self.main_screen.manager.current = 'note'

    def go_to_main_screen(self):
        self.main_screen.manager.transition.direction = 'right'
        self.main_screen.manager.current = 'main'

if __name__ == '__main__':
    NotebookApp().run()