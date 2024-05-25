from functools import partial
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QApplication, \
    QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor

from app.admin.adminWin import AdminWin
from app.admin.createTestWin import CreateTestWin
from app.user.listEventWin import ListEventWin
from app.user.testingWin import TestingWin
from app.user.userWin import UserWin
from components.functions import button_animation
from database.scripts.db import Data


class MainWin(QMainWindow, AdminWin, UserWin, TestingWin, ListEventWin):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        self.db = Data('database/Museum.db')
        self.init_main_ui()

    def init_main_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.resize(700, 450)
        self.wid = QWidget()
        self.setCentralWidget(self.wid)
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
        self.main_win_vl.addStretch()
        self.wid.setLayout(self.main_win_vl)

        self.user_btn.clicked.connect(partial(button_animation, btn=self.user_btn, win=self.wid, f=self.init_user_ui))
        self.admin_btn.clicked.connect(partial(button_animation, btn=self.admin_btn, win=self.wid, f=self.init_admin_ui))

        self.user_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5,
                                                                  xOffset=4,
                                                                  yOffset=4,
                                                                  color=QColor(0, 0, 0)))
        self.admin_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5,
                                                                   xOffset=4,
                                                                   yOffset=4,
                                                                   color=QColor(0, 0, 0)))

    def closeEvent(self, event):
        QApplication.quit()


