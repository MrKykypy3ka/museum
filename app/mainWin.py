from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QApplication
from PyQt5.QtGui import QIcon

from app.admin.adminWin import AdminWin
from app.admin.createTestWin import CreateTestWin
from app.user.listEventWin import ListEventWin
from app.user.testingWin import TestingWin
from app.user.userWin import UserWin
from database.scripts.db import Data


class MainWin(QMainWindow, AdminWin, UserWin, TestingWin, ListEventWin):
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

    def closeEvent(self, event):
        QApplication.quit()

    def get_close_signal(self, data):
        self.show()

    def show_create_test_win(self):
        self.win_ct = CreateTestWin()
        self.win_ct.close_signal.connect(self.get_close_signal)
        self.win_ct.show()
        self.hide()
