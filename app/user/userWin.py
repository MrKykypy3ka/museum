from functools import partial

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtCore import QSize

from components.functions import button_animation


class UserWin(QWidget):
    def init_user_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.resize(700, 450)
        self.setFixedSize(700, 450)
        wid = QWidget()
        self.setCentralWidget(wid)
        self.tests_btn = QPushButton(' Викторины')
        self.games_btn = QPushButton(' Игры')
        self.back = QPushButton('← Назад')
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

        self.tests_btn.clicked.connect(partial(button_animation, btn=self.tests_btn, win=self, f=self.init_list_tests_ui))
        self.games_btn.clicked.connect(partial(button_animation, btn=self.games_btn, win=self, f=self.init_list_tests_ui))
        self.back.clicked.connect(partial(button_animation, btn=self.back, win=self, f=self.init_main_ui))


        self.tests_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.games_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.back.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))