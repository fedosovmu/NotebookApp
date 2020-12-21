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
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            text TEXT
        );
        """
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_note(self, title, text=None):
        if text is None:
            text = title
        sql = 'INSERT INTO notes (title, text) VALUES (?, ?)'
        self.cursor.execute(sql, (title, text))
        self.conn.commit()
        return self.cursor.lastrowid

    def delete_note(self, id):
        sql = 'DELETE FROM notes WHERE id = ?'
        self.cursor.execute(sql, (id,))
        self.conn.commit()

    def select_notes(self):
        sql = 'SELECT id, title FROM notes'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return map(lambda x: {'id': x[0], 'title': x[1]}, rows)
