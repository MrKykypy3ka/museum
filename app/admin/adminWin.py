from functools import partial

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import QSize

from app.admin.createTestWin import CreateTestWin
from app.admin.createGameWin import CreateGameWin
from components.functions import button_animation


class AdminWin(QWidget):
    def init_admin_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.create_test = QPushButton(' + Создать викторину')
        self.list_test = QPushButton(' # Список викторин')
        self.create_game = QPushButton(' + Создать игру')
        self.list_game = QPushButton(' # Список игр')
        self.back = QPushButton(' ← Назад')
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

        self.create_test.setObjectName('main')
        self.list_test.setObjectName('main')
        self.create_game.setObjectName('main')
        self.list_game.setObjectName('main')
        self.back.setObjectName('main')

        self.create_test.clicked.connect(partial(button_animation, btn=self.create_test, win=self, f=self.show_create_test_win))
        self.create_game.clicked.connect(partial(button_animation, btn=self.create_game, win=self, f=self.show_create_game_win))
        self.back.clicked.connect(partial(button_animation, btn=self.back, win=self, f=self.init_main_ui))

        self.create_test.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.list_test.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.create_game.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.list_game.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.back.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))

    def get_close_signal(self, data):
        self.show()

    def show_create_test_win(self):
        self.win_ct = CreateTestWin()
        self.win_ct.close_signal.connect(self.get_close_signal)
        self.win_ct.show()
        self.hide()

    def show_create_game_win(self):
        self.win_cw = CreateGameWin()
        self.win_cw.close_signal.connect(self.get_close_signal)
        self.win_cw.show()
        self.hide()