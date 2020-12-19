from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.stiffscroll import StiffScrollEffect
from kivymd.uix.menu import MDDropdownMenu
from datetime import datetime


class MainScreen(Screen):
    def __init__(self, app, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.app = app
        # Установка жесткого эффекта прокрутки
        self.ids.scroll_view.effect_cls = StiffScrollEffect
        self.load_notes()
        self.note_number = 0
        # Создание выпадающего меню
        self.menu = MDDropdownMenu()

    def test_button_on_press(self):
        self.ids.test_button.last_press_time = datetime.now()
        print('test button press')

    def test_button_on_release(self):
        release_time = datetime.now()
        delay = release_time - self.ids.test_button.last_press_time
        delay_in_seconds = round(delay.total_seconds(), 2)
        print('test button on release {}'.format(delay_in_seconds))

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
        new_note.bind(
            on_press=lambda x: self.app.go_to_note_screen('db_id: {}'.format(new_note.db_id))
        )
        new_note.bind(
            on_long_press=lambda x: print('on_release')
        )
        self.ids.notes_list.add_widget(
                new_note
            )