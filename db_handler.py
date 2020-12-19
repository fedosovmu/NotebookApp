import sqlite3


class DbHandler:
    def __init__(self):
        pass

    def connect(self):
        self.conn = sqlite3.connect('notebook.db')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
        self.conn = None
        self.cursor = None

    def create_tables_if_not_exists(self):
        sql = """
        CREATE TABLE IF NOT EXISTS notes (
            note_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            text TEXT
        );
        """
        self.cursor.execute(sql)
        self.conn.commit()

    def add_note(self, title, text=None):
        if text is None:
            text = title
        sql = 'INSERT INTO notes (title, text) VALUES (?, ?)'
        self.cursor.execute(sql, (title, text))
        self.conn.commit()

    def select_note_titles(self):
        sql = 'SELECT title FROM notes'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return  map(lambda x: x[0], rows)