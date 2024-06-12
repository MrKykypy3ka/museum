from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, \
    QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import QSize
from functools import partial
from components.functions import button_animation
import os


class ListEventWin(QWidget):
    def init_list_ui(self, type):
        self.activity = type
        self.setWindowTitle('Краеведческий музей Благовещенска')
        wid_list = QWidget()
        self.setCentralWidget(wid_list)
        self.search_activity = QLineEdit()
        self.search_activity.setPlaceholderText(' Введите название теста')
        self.list_activity = QListWidget()
        self.start_activity_btn = QPushButton(f' Запустить {type}')
        self.back = QPushButton(' ← Назад')
        self.back.setIcon(QIcon('resources/back.png'))
        self.back.setIconSize(QSize(40, 40))
        self.list_tests_win_vl = QVBoxLayout()
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()
        self.list_tests_win_vl.addWidget(self.search_activity)
        self.list_tests_win_vl.addWidget(self.list_activity, 5)
        hl1.addWidget(self.start_activity_btn, 3)
        hl1.addStretch(3)
        self.list_tests_win_vl.addLayout(hl1)
        hl2.addStretch()
        hl2.addWidget(self.back)
        self.list_tests_win_vl.addStretch()
        self.list_tests_win_vl.addLayout(hl2)
        wid_list.setLayout(self.list_tests_win_vl)
        if type == 'викторину':
            self.db.get_all_tests()
        else:
            self.db.get_all_games()
        self.start_activity_btn.setObjectName('main')
        self.back.setObjectName('main')

        self.searching(self.search_activity, self.list_activity)
        self.search_activity.textChanged.connect(partial(self.searching, line_w=self.search_activity, list_w=self.list_activity))
        self.start_activity_btn.clicked.connect(self.show_activity_win)
        self.back.clicked.connect(partial(button_animation, btn=self.back, win=self, f=self.init_user_ui))
        self.search_activity.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.list_activity.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.start_activity_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.back.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))

    def searching(self, line_w, list_w):
        list_w.clear()
        self.filter = [x for x in self.db.data]
        if line_w.text():
            self.filter = [x for x in self.filter if line_w.text() in x[2]]
        list_w.addItems([x[2] for x in self.filter])

    def show_activity_win(self):
        print(self.filter)
        if self.list_activity.currentRow() != -1:
            if self.activity == 'викторину':
                button_animation(btn=self.start_activity_btn, win=self, f=self.init_testing_ui)
            else:
                button_animation(btn=self.start_activity_btn, win=self, f=self.init_play_ui)
