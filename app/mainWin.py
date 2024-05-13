from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QApplication, QLineEdit, \
    QListWidget, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.uic.properties import QtWidgets

from app.adminWin import AdminWin
from app.createTestWin import TestWin
from database.scripts.db import Data
from functools import partial


def get_style_button(widget):
    widget.setStyleSheet('''border-radius : 0;
                            border: 1px solid #cc6;
                            background-color: #333;
                            color: #cc6;
                            font-family: MontserratBolt;
                            font-size: 24pt;
                            width: 7em;
                            height: 1em;
                            text-align: left;''')


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.close_test_win = False
        self.win_ct = None
        self.init_main_ui()
        self.db = Data('database/Museum.db')

    def init_main_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.resize(700, 450)
        self.setFixedSize(700, 450)
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        wid = QWidget()
        wid.setStyleSheet('''background-color: rgb(254, 237, 210)''')
        self.setCentralWidget(wid)

        self.user_btn = QPushButton(' Зал')
        get_style_button(self.user_btn)
        self.admin_btn = QPushButton(' Методист')
        get_style_button(self.admin_btn)

        self.main_win_vl = QVBoxLayout()
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()

        hl1.addWidget(self.user_btn)
        hl1.addStretch()
        hl2.addWidget(self.admin_btn)
        hl2.addStretch()
        self.main_win_vl.addStretch()
        self.main_win_vl.addLayout(hl1)
        self.main_win_vl.addLayout(hl2)
        wid.setLayout(self.main_win_vl)
        self.user_btn.clicked.connect(self.init_user_ui)
        self.admin_btn.clicked.connect(self.init_admin_ui)
        wid.setStyleSheet("background-image : url(resources/background.png)")

    def init_admin_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.resize(700, 450)
        self.setFixedSize(700, 450)
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        self.create_test = QPushButton('+ Создать тест')
        get_style_button(self.create_test)
        self.list_test = QPushButton('# Список тестов')
        get_style_button(self.list_test)
        self.create_game = QPushButton('+ Создать игру')
        get_style_button(self.create_game)
        self.list_game = QPushButton('# Список игр')
        get_style_button(self.list_game)
        self.back = QPushButton('Назад')
        get_style_button(self.back)
        self.back.setIcon(QIcon('resources/back.png'))
        self.back.setIconSize(QSize(40, 40))
        wid = QWidget()
        wid.setStyleSheet("background-image : url(resources/background.png)")
        self.setCentralWidget(wid)

        self.admin_win_vl = QVBoxLayout()
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()
        hl3 = QHBoxLayout()
        hl4 = QHBoxLayout()
        hl5 = QHBoxLayout()

        hl1.addWidget(self.create_test)
        hl1.addStretch()
        hl2.addWidget(self.list_test)
        hl2.addStretch()
        hl3.addWidget(self.create_game)
        hl3.addStretch()
        hl4.addWidget(self.list_game)
        hl4.addStretch()
        hl5.addStretch()
        hl5.addWidget(self.back)

        self.admin_win_vl.addStretch()
        self.admin_win_vl.addLayout(hl1)
        self.admin_win_vl.addLayout(hl2)
        self.admin_win_vl.addLayout(hl3)
        self.admin_win_vl.addLayout(hl4)
        self.admin_win_vl.addStretch()
        self.admin_win_vl.addLayout(hl5)
        wid.setLayout(self.admin_win_vl)
        self.create_test.clicked.connect(self.showCreateTestWin)
        self.back.clicked.connect(self.init_main_ui)

    def init_user_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.resize(700, 450)
        self.setFixedSize(700, 450)
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        wid = QWidget()
        wid.setStyleSheet("background-image : url(resources/background.png)")
        self.setCentralWidget(wid)

        self.tests_btn = QPushButton(' Викторины')
        self.games_btn = QPushButton(' Игры')
        get_style_button(self.tests_btn)
        get_style_button(self.games_btn)

        self.back = QPushButton('Назад')
        get_style_button(self.back)
        self.back.setIcon(QIcon('resources/back.png'))
        self.back.setIconSize(QSize(40, 40))

        self.user_win_vl = QVBoxLayout()
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()
        hl3 = QHBoxLayout()
        hl1.addWidget(self.tests_btn)
        hl1.addStretch()

        hl2.addWidget(self.games_btn)
        hl2.addStretch()

        hl3.addStretch()
        hl3.addWidget(self.back)
        self.user_win_vl.addStretch()
        self.user_win_vl.addLayout(hl1)
        self.user_win_vl.addLayout(hl2)
        self.user_win_vl.addStretch()
        self.user_win_vl.addLayout(hl3)
        wid.setLayout(self.user_win_vl)

        self.back.clicked.connect(self.init_main_ui)
        self.tests_btn.clicked.connect(self.init_list_tests_ui)
        self.games_btn.clicked.connect(self.init_list_games_ui)

    def init_list_tests_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')

        self.setWindowIcon(QIcon('resources/favicon.ico'))
        wid_list = QWidget()
        wid_list.setStyleSheet("""QWidget {background-image: url(resources/background.png);
                              background-clip: border-box}""")
        self.setCentralWidget(wid_list)

        self.search_test = QLineEdit()
        self.search_test.setStyleSheet('''background-image: url();
                                         background-color: #f5f5e6;''')
        self.search_test.setPlaceholderText('Введите название теста')
        self.list_tests = QListWidget()
        self.list_tests.setStyleSheet('''background-image: url();
                                         background-color: #f5f5e6;''')
        self.start_test_btn = QPushButton(' Запустить викторину')
        get_style_button(self.start_test_btn)

        self.back = QPushButton('Назад')
        get_style_button(self.back)
        self.back.setIcon(QIcon('resources/back.png'))
        self.back.setIconSize(QSize(40, 40))

        self.list_tests_win_vl = QVBoxLayout()
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()
        self.list_tests_win_vl.addWidget(self.search_test)
        self.list_tests_win_vl.addWidget(self.list_tests, 5)
        hl1.addWidget(self.start_test_btn, 3)
        hl1.addStretch(3)
        self.list_tests_win_vl.addLayout(hl1)
        hl2.addStretch()
        hl2.addWidget(self.back)
        self.list_tests_win_vl.addStretch()
        self.list_tests_win_vl.addLayout(hl2)
        wid_list.setLayout(self.list_tests_win_vl)

        self.back.clicked.connect(self.init_user_ui)

        self.db.get_all_tests()

        self.searching(self.search_test, self.list_tests)
        self.search_test.textChanged.connect(partial(self.searching, line_w=self.search_test, list_w=self.list_tests))

    def init_list_games_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')

        self.setWindowIcon(QIcon('resources/favicon.ico'))
        wid_list = QWidget()
        wid_list.setStyleSheet("""QWidget {background-image: url(resources/background.png);
                              background-clip: border-box}""")
        self.setCentralWidget(wid_list)

        self.search_game = QLineEdit()
        self.search_game.setStyleSheet('''background-image: url();
                                         background-color: #f5f5e6;''')
        self.search_game.setPlaceholderText('Введите название теста')
        self.list_games = QListWidget()
        self.list_games.setStyleSheet('''background-image: url();
                                         background-color: #f5f5e6;''')
        self.start_test_btn = QPushButton(' Запустить игру')
        get_style_button(self.start_test_btn)

        self.back = QPushButton('Назад')
        get_style_button(self.back)
        self.back.setIcon(QIcon('resources/back.png'))
        self.back.setIconSize(QSize(40, 40))

        self.list_games_win_vl = QVBoxLayout()
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()
        self.list_games_win_vl.addWidget(self.search_game)
        self.list_games_win_vl.addWidget(self.list_games, 5)
        hl1.addWidget(self.start_test_btn, 2)
        hl1.addStretch(5)
        self.list_games_win_vl.addLayout(hl1)
        hl2.addStretch()
        hl2.addWidget(self.back)
        self.list_games_win_vl.addStretch()
        self.list_games_win_vl.addLayout(hl2)
        wid_list.setLayout(self.list_games_win_vl)



        self.db.get_all_games()

        self.searching(self.search_game, self.list_games)
        self.back.clicked.connect(self.init_user_ui)
        self.search_game.textChanged.connect(partial(self.searching, line_w=self.search_game, list_w=self.list_games))

    def searching(self, line_w, list_w):
        list_w.clear()
        self.filter = [x[2] for x in self.db.data]
        if line_w.text():
            self.filter = [x for x in self.filter if line_w.text() in x]
        list_w.addItems(self.filter)






    def closeEvent(self, event):
        QApplication.quit()

    def get_close_signal(self, data):
        self.show()

    def showCreateTestWin(self):
        self.win_ct = TestWin()
        self.win_ct.close_signal.connect(self.get_close_signal)
        self.win_ct.show()
        self.hide()