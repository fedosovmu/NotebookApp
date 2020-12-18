import config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.stiffscroll import StiffScrollEffect


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        # Установка жесткого эффекта прокрутки
        self.ids.scroll_view.effect_cls = StiffScrollEffect

class NoteScreen(Screen):
    pass


class NotebookApp(MDApp):
    title = 'Блокнот'

    def build(self):
        Builder.load_file('app.kv')
        self.main_screen = MainScreen(name='main')
        self.note_screen = NoteScreen(name='note')
        self.sm = ScreenManager()
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.note_screen)
        return self.sm

    def go_to_note_screen(self, text):
        self.note_screen.ids.content_lable.text = text + ' Content'
        self.main_screen.manager.transition.direction = 'left'
        self.main_screen.manager.current = 'note'

    def go_to_main_screen(self):
        self.main_screen.manager.transition.direction = 'right'
        self.main_screen.manager.current = 'main'

if __name__ == '__main__':
    NotebookApp().run()