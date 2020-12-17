from main_screen import MainScreen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class NotebookApp(MDApp):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    NotebookApp().run()