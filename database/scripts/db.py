import sqlite3


class Data:
    def __init__(self, filename):
        self.data = []
        self.filename = filename
        self.connect()

    def connect(self):
        self.db = sqlite3.connect(self.filename)
        self.cur = self.db.cursor()

    def add_test(self, **kwargs):
        try:
            request = """INSERT INTO Tests (id_type, text)
                                      VALUES (?, ?);"""
            data = (kwargs['id_type'], kwargs['text'])
            self.cur.execute(request, data).fetchall()
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def add_taks(self, **kwargs):
        try:
            request = """INSERT INTO Tasks (id_test, text, picture)
                                      VALUES (?, ?, ?);"""
            data = (kwargs['id_test'], kwargs['text'], kwargs['picture'])
            print(data)
            self.cur.execute(request, data).fetchall()
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def add_answer(self, **kwargs):
        try:
            request = """INSERT INTO Answers (id_task, text, is_correct)
                                      VALUES (?, ?, ?);"""
            data = (kwargs['id_task'], kwargs['text'], kwargs['is_correct'])
            self.cur.execute(request, data).fetchall()
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def get_type(self, **kwargs):
        try:
            request = """SELECT id_type FROM Types_event
                         WHERE name = ?"""
            self.data = self.cur.execute(request, (kwargs['name'],)).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_test(self, **kwargs):
        try:
            request = """SELECT id_test FROM Tests
                         WHERE text = ?"""
            self.data = self.cur.execute(request, (kwargs['text'],)).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_task(self, **kwargs):
        try:
            request = """SELECT id_task FROM Tasks
                         WHERE text = ?"""
            self.data = self.cur.execute(request, (kwargs['text'],)).fetchall()
        except sqlite3.Error as e:
            print(e)
