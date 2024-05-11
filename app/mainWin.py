from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from app.adminWin import AdminWin
from app.createTestWin import TestWin


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
        self.win_ct = None
        self.init_main_ui()

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

        self.main_main_vl = QVBoxLayout()
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()

        hl1.addWidget(self.user_btn)
        hl1.addStretch()
        hl2.addWidget(self.admin_btn)
        hl2.addStretch()
        self.main_main_vl.addStretch()
        self.main_main_vl.addLayout(hl1)
        self.main_main_vl.addLayout(hl2)
        wid.setLayout(self.main_main_vl)
        self.admin_btn.clicked.connect(self.init_admin_ui)
        self.setStyleSheet("background-image : url(resources/background.png)")

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
        wid.setStyleSheet('''background-color: rgb(254, 237, 210)''')
        self.setCentralWidget(wid)

        self.main_admin_vl = QVBoxLayout()
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

        self.main_admin_vl.addStretch()
        self.main_admin_vl.addLayout(hl1)
        self.main_admin_vl.addLayout(hl2)
        self.main_admin_vl.addLayout(hl3)
        self.main_admin_vl.addLayout(hl4)
        self.main_admin_vl.addStretch()
        self.main_admin_vl.addLayout(hl5)
        wid.setLayout(self.main_admin_vl)
        self.create_test.clicked.connect(self.showCreateTestWin)
        self.back.clicked.connect(self.init_main_ui)
        self.setStyleSheet("background-image : url(resources/background.png)")

    def closeEvent(self, event):
        QApplication.quit()

    # def showAdminWin(self):
    #     self.win_adm = AdminWin()
    #     self.win_adm.show()

    # def showUserWin(self):
    #     self.win_urs = UserWin()
    #     self.win_usr.show()

    def showCreateTestWin(self):
        self.win_ct = TestWin()
        self.win_ct.show()
        self.hide()
        if not self.win_ct.closeEvent():
            self.show()