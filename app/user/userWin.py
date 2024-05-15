from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QSize


class UserWin(QWidget):
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
        self.games_btn.clicked.connect(self.init_list_tests_ui)