from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, \
    QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import QSize, Qt
from functools import partial

from components.functions import button_animation


class ListEventWin(QWidget):
    def init_list_tests_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        wid_list = QWidget()
        self.setCentralWidget(wid_list)
        self.search_test = QLineEdit()
        self.search_test.setPlaceholderText('Введите название теста')
        self.list_tests = QListWidget()
        self.start_test_btn = QPushButton(' Запустить викторину')
        self.back = QPushButton('← Назад')
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

        self.db.get_all_tests()

        self.searching(self.search_test, self.list_tests)
        self.search_test.textChanged.connect(partial(self.searching, line_w=self.search_test, list_w=self.list_tests))
        self.start_test_btn.clicked.connect(self.show_testing_win)
        self.back.clicked.connect(partial(button_animation, btn=self.back, win=self, f=self.init_user_ui))

        self.search_test.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.list_tests.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.start_test_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.back.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))

    def searching(self, line_w, list_w):
        list_w.clear()
        self.filter = [x for x in self.db.data]
        if line_w.text():
            self.filter = [x for x in self.filter if line_w.text() in x[2]]
        list_w.addItems([x[2] for x in self.filter])

    def show_testing_win(self):
        if self.list_tests.currentRow() != -1:
            button_animation(btn=self.start_test_btn, win=self, f=self.init_testing_ui)
