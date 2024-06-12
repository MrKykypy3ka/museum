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
            request = """INSERT INTO Questions (id_test, text, picture)
                                      VALUES (?, ?, ?);"""
            data = (kwargs['id_test'], kwargs['text'], kwargs['picture'])
            print(data)
            self.cur.execute(request, data).fetchall()
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def add_answer(self, **kwargs):
        try:
            request = """INSERT INTO Answers (id_question, text, is_correct)
                                      VALUES (?, ?, ?);"""
            data = (kwargs['id_question'], kwargs['text'], kwargs['is_correct'])
            self.cur.execute(request, data).fetchall()
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def add_game(self, **kwargs):
        try:
            request = """INSERT INTO Games (id_type, text, picture)
                                      VALUES (?, ?, ?);"""
            data = (kwargs['id_type'], kwargs['text'], kwargs['picture'])
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

    def get_games_types(self, **kwargs):
        try:
            request = """SELECT id_type, name FROM Types_event
                         WHERE name <> 'Тест'"""
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_text_test(self, **kwargs):
        try:
            request = """SELECT id_test FROM Tests
                         WHERE text = ?"""
            self.data = self.cur.execute(request, (kwargs['text'],)).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_task(self, **kwargs):
        try:
            request = """SELECT id_question FROM Questions
                         WHERE text = ?"""
            self.data = self.cur.execute(request, (kwargs['text'],)).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_all_tests(self, **kwargs):
        try:
            request = """SELECT id_test, id_type, text FROM Tests"""
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_all_games(self, **kwargs):
        try:
            request = """SELECT Games.id_game, Types_event.name, Games.text FROM Games
                         INNER JOIN Types_event ON Games.id_type = Types_event.id_type"""
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_test(self, **kwargs):
        try:
            request = """SELECT Questions.text, Questions.picture, Answers.text, Answers.is_correct FROM Questions
                         INNER JOIN Answers ON Questions.id_question = Answers.id_question
                         WHERE Questions.id_test == ?"""
            self.data = self.cur.execute(request, (kwargs['id_test'],)).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_game(self, **kwargs):
        try:
            request = """SELECT text, picture FROM Games
                         WHERE id_game == ?"""
            self.data = self.cur.execute(request, (kwargs['id_game'],)).fetchall()
        except sqlite3.Error as e:
            print(e)