import config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from db_handler import DbHandler
from main_screen import MainScreen


class NoteScreen(Screen):
    title = 'Заметка'


class NotebookApp(MDApp):
    title = 'Мои заметки'

    def build(self):
        self.db_handler = DbHandler()
        self.db_handler.connect()
        self.db_handler.create_tables_if_not_exists()
        Builder.load_file('app.kv')
        self.main_screen = MainScreen(self, name='main')
        self.note_screen = NoteScreen(name='note')
        self.sm = ScreenManager()
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.note_screen)
        return self.sm

    def on_stop(self):
        self.db_handler.close()

    def go_to_note_screen(self, text):
        self.note_screen.ids.content_lable.text = text + ' Content'
        self.main_screen.manager.transition.direction = 'left'
        self.main_screen.manager.current = 'note'

    def go_to_main_screen(self):
        self.main_screen.manager.transition.direction = 'right'
        self.main_screen.manager.current = 'main'

if __name__ == '__main__':
    NotebookApp().run()