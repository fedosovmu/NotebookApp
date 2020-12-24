from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.stiffscroll import StiffScrollEffect
from kivymd.uix.menu import MDDropdownMenu
from datetime import datetime
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.list import OneLineAvatarIconListItem


class DeleteMenuItem(OneLineAvatarIconListItem):
    divider = False


class MainScreen(Screen):
    def __init__(self, app, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.app = app
        # Установка жесткого эффекта прокрутки
        self.ids.scroll_view.effect_cls = StiffScrollEffect
        self.load_notes()
        self.note_number = 0
        # Создание диалога удаления записи
        self.delete_note_dialog = MDDialog(
            text='Удалить?',
            type="confirmation",
            items=[
                DeleteMenuItem(text='Удалить item')
            ],
            buttons=[
                MDFlatButton(text="Отмена", text_color=self.app.theme_cls.primary_color)
            ]
        )

    def load_notes(self):
        notes = self.app.db_handler.select_notes()
        for note in notes:
            self.add_note_to_screen(note['id'], note['title'])

    def create_note(self):
        self.note_number += 1
        title = 'Новая заметка {}'.format(self.note_number)
        db_id = self.app.db_handler.insert_note(title)
        self.add_note_to_screen(db_id=db_id, title=title)

    def open_delete_note_dialoge(self, list_item):
        print('Delete item db_id: {}?'.format(list_item.db_id))
        self.delete_note_dialog.open()

    def list_item_on_press_callback(self, list_item):
        list_item.last_press_time = datetime.now()

    def list_item_on_release_callback(self, list_item):
        release_time = datetime.now()
        delay = release_time - list_item.last_press_time
        delay_in_seconds = delay.total_seconds()
        LONG_PRESS_TIME = 0.5
        if delay_in_seconds < LONG_PRESS_TIME:
            # short press
            self.app.go_to_note_screen('db_id: {}'.format(list_item.db_id))
        else:
            # long press
            # self.open_delete_note_dialoge(list_item)
            self.ids.notes_list.remove_widget(list_item)
            self.app.db_handler.delete_note(list_item.db_id)

    def add_note_to_screen(self, db_id, title):
        new_note = OneLineListItem(text=title)
        new_note.db_id = db_id
        new_note.bind(
            on_press=lambda list_item: self.list_item_on_press_callback(list_item)
        )
        new_note.bind(
            on_release=lambda list_item: self.list_item_on_release_callback(list_item)
        )
        self.ids.notes_list.add_widget(
                new_note
        )
