from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QApplication, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


def get_style_button(widget):
    widget.setStyleSheet('''border-radius : 0;
                            border: 0.5px solid black;
                            background-color: #333;
                            color: #fc9;
                            font-family: Montserrat;
                            font-size: 24pt;
                            width: 7em;
                            height: 1em;''')


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска')
        self.resize(600,400)
        #self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        wid = QWidget()
        wid.setStyleSheet('''background-color: rgb(254, 237, 210)''')
        self.setCentralWidget(wid)
        self.create_test = QPushButton('+ Создать тест')
        get_style_button(self.create_test)
        self.create_game = QPushButton('+ Создать игру')
        get_style_button(self.create_game)
        self.back = QPushButton('Назад')
        get_style_button(self.back)
        self.back.setIcon(QIcon('resources/back.png'))
        self.back.setIconSize(QSize(40, 40))

        main_vl = QVBoxLayout()
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()
        hl3 = QHBoxLayout()

        hl1.addWidget(self.create_test)
        hl1.addStretch()
        hl2.addWidget(self.create_game)
        hl2.addStretch()
        hl3.addStretch()
        hl3.addWidget(self.back)

        main_vl.addStretch()
        main_vl.addLayout(hl1)
        main_vl.addLayout(hl2)
        main_vl.addStretch()
        main_vl.addLayout(hl3)
        wid.setLayout(main_vl)
