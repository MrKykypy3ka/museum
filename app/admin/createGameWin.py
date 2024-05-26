from functools import partial

from components.functions import button_animation
from components.new_widgets import ScaledPixmapLabel

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMainWindow,
                             QGraphicsDropShadowEffect, QFileDialog)
from PyQt5.QtGui import QIcon, QColor, QPixmap, QImage
from PyQt5.QtCore import pyqtSignal, Qt
from database.scripts.db import Data


class CreateGameWin(QMainWindow):
    close_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.db = Data('database/Museum.db')
        self.init_ui()
        self.tasks = list()

    def init_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска: создание теста')
        self.resize(700, 450)
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        win = QWidget()
        win.setObjectName('transparent')
        self.setCentralWidget(win)
        self.title = QLineEdit()
        self.title.setPlaceholderText('Введите название игры')
        self.image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
        self.image.setStyleSheet('border: 1px solid black;')
        self.image.setScaledContents(False)
        self.image.setFixedSize(200, 200)
        self.add_image = QPushButton('Добавить изображение')
        self.accept = QPushButton('Добавить вопрос')

        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        h_l3 = QHBoxLayout()

        main_l.addStretch()
        main_l.addWidget(self.title)
        h_l1.addWidget(self.image, 2)
        h_l1.addStretch(5)
        main_l.addLayout(h_l1, 3)

        h_l2.addWidget(self.add_image, 2)
        h_l2.addStretch(5)
        main_l.addLayout(h_l2)

        h_l3.addStretch(5)
        h_l3.addWidget(self.accept, 2)
        main_l.addLayout(h_l3)

        main_l.addStretch()
        win.setLayout(main_l)

        self.add_image.clicked.connect(partial(button_animation, btn=self.add_image, win=self, f=self.load_image))
        self.accept.clicked.connect(partial(button_animation, btn=self.accept, win=self, f=self.game_formation))

        self.add_image.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5,
                                                                   xOffset=4,
                                                                   yOffset=4,
                                                                   color=QColor(0, 0, 0)))
        self.accept.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5,
                                                                xOffset=4,
                                                                yOffset=4,
                                                                color=QColor(0, 0, 0)))

    def load_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', "Images (*.png *.jpeg *.jpg)")
        if fname[0]:
            self.pixmap = QPixmap.fromImage(QImage(fname[0]))
            self.image.setPixmap(self.pixmap)
            with open(fname[0], 'rb') as file:
                self.byte_image = file.read()

    def game_formation(self):
        pass
        # self.check_correct()
        # if not self.bad_answers and self.question.text():
        #     self.task = list()
        #     self.task.append(self.question.text())
        #     self.task.append(self.byte_image)
        #     self.task.append([])
        #     for i in range(len(self.answers)):
        #         self.task[2].append((self.answers[i][0].isCheckable(), self.answers[i][1].text()))
        #     self.close()
        # elif not self.question.text():
        #     self.question.setStyleSheet('''border: 1px solid red;''')
        # elif self.question.text():
        #     self.question.setStyleSheet('''''')
