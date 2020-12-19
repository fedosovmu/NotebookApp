import config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.stiffscroll import StiffScrollEffect
from db_handler import DbHandler


class MainScreen(Screen):
    def __init__(self, app, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.app = app
        # Установка жесткого эффекта прокрутки
        self.ids.scroll_view.effect_cls = StiffScrollEffect
        self.load_notes()
        self.note_number = 0

    def load_notes(self):
        notes = self.app.db_handler.select_notes()
        for note in notes:
            self.add_note_to_screen(note['id'], note['title'])

    def create_note(self):
        self.note_number += 1
        title = 'Новая заметка {}'.format(self.note_number)
        db_id = self.app.db_handler.insert_note(title)
        self.add_note_to_screen(db_id=db_id, title=title)

    def add_note_to_screen(self, db_id, title):
        new_note = OneLineListItem(text=title)
        new_note.db_id = db_id
        new_note.bind(on_press=lambda x: self.app.go_to_note_screen('db_id: {}'.format(new_note.db_id)))
        self.ids.notes_list.add_widget(
                new_note
            )


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