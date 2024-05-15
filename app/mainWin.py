from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QMainWindow,
                             QHBoxLayout, QApplication, QLineEdit, QListWidget, QLabel, QCheckBox, QGroupBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from app.createTestWin import TestWin
from classes.new_widgets import ScaledPixmapLabel
from database.scripts.db import Data
from functools import partial


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_main_ui()
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        self.db = Data('database/Museum.db')

    def init_main_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.resize(700, 450)
        self.setFixedSize(700, 450)
        wid = QWidget()
        self.setCentralWidget(wid)
        self.user_btn = QPushButton(' Зал')
        self.admin_btn = QPushButton(' Методист')
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

    def init_admin_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.resize(700, 450)
        self.setFixedSize(700, 450)
        self.create_test = QPushButton('+ Создать тест')
        self.list_test = QPushButton('# Список тестов')
        self.create_game = QPushButton('+ Создать игру')
        self.list_game = QPushButton('# Список игр')
        self.back = QPushButton('Назад')
        self.back.setIcon(QIcon('resources/back.png'))
        self.back.setIconSize(QSize(40, 40))
        wid = QWidget()
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
        wid = QWidget()
        self.setCentralWidget(wid)
        self.tests_btn = QPushButton(' Викторины')
        self.games_btn = QPushButton(' Игры')
        self.back = QPushButton('Назад')
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
        wid_list = QWidget()
        self.setCentralWidget(wid_list)
        self.search_test = QLineEdit()
        self.search_test.setPlaceholderText('Введите название теста')
        self.list_tests = QListWidget()
        self.start_test_btn = QPushButton(' Запустить викторину')
        self.back = QPushButton('Назад')
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
        self.start_test_btn.clicked.connect(self.init_testing_ui)

    def init_list_games_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        wid_list = QWidget()
        self.setCentralWidget(wid_list)
        self.search_game = QLineEdit()
        self.search_game.setPlaceholderText('Введите название теста')
        self.list_games = QListWidget()
        self.start_test_btn = QPushButton(' Запустить игру')
        self.back = QPushButton('Назад')
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

    def init_testing_ui(self):
        text_test = self.list_tests.currentItem().text()
        self.setWindowTitle(f'Краеведческий музей Благовещенска: Тест - {text_test}')
        wid = QWidget()
        self.setCentralWidget(wid)
        self.db.get_test(id_test=[x[0] for x in self.filter if text_test in x[2]][0])
        print(self.db.data)


        self.setWindowTitle('Краеведческий музей Благовещенска: создание вопроса')
        self.resize(600, 400)
        self.setFixedWidth(600)
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        self.question = QLineEdit()
        self.question.setPlaceholderText('Введите название вопроса')
        self.image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
        self.image.setStyleSheet('border: 1px solid black;')
        self.image.setScaledContents(False)
        self.image.setFixedSize(200, 200)
        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        h_l4 = QHBoxLayout()
        answers_group = QGroupBox('Ответы')
        main_l.addStretch()
        main_l.addWidget(self.question)
        h_l1.addWidget(self.image, 2)
        h_l1.addStretch(5)
        main_l.addLayout(h_l1, 3)
        h_l2.addWidget(self.add_image, 2)
        h_l2.addStretch(5)
        main_l.addLayout(h_l2)
        main_l.addWidget(self.add_image)
        self.vg_l = QVBoxLayout()
        for _ in range(1, 3):
            self.add_answer()
        answers_group.setLayout(self.vg_l)
        main_l.addWidget(answers_group)
        h_l4.addStretch(5)
        h_l4.addWidget(self.add_task, 2)
        main_l.addLayout(h_l4)
        main_l.addStretch()
        self.setLayout(main_l)


    def add_answer(self):
        if len(self.answers) < 8:
            answer = QLabel()
            correct = QCheckBox()
            self.answers.append((correct, answer))
            h_l = QHBoxLayout()
            h_l.addWidget(correct)
            h_l.addWidget(answer)
            self.vg_l.addLayout(h_l)
            self.adjustSize()


    def searching(self, line_w, list_w):
        list_w.clear()
        self.filter = [x for x in self.db.data]
        if line_w.text():
            self.filter = [x for x in self.filter if line_w.text() in x[2]]
        list_w.addItems([x[2] for x in self.filter])

    def closeEvent(self, event):
        QApplication.quit()

    def get_close_signal(self, data):
        self.show()

    def show_create_test_win(self):
        self.win_ct = TestWin()
        self.win_ct.close_signal.connect(self.get_close_signal)
        self.win_ct.show()
        self.hide()

    def showCreateTestWin(self):
        self.win_ct = TestWin()
        self.win_ct.show()
