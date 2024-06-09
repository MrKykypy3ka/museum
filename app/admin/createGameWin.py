from functools import partial

from components.functions import button_animation
from components.new_widgets import ScaledPixmapLabel

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMainWindow, QComboBox,
                             QGraphicsDropShadowEffect, QFileDialog, QMessageBox, QLabel)
from PyQt5.QtGui import QIcon, QColor, QPixmap, QImage
from PyQt5.QtCore import pyqtSignal, Qt
from database.scripts.db import Data


class CreateGameWin(QMainWindow):
    close_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.db = Data('database/Museum.db')
        self.db.get_games_types()
        self.puzzle_ui()
        self.changeling_ui()
        self.init_ui()
        self.edit_configurator()
        self.tasks = list()

    def init_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска: создание игр')
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        self.resize(1280, 720)
        self.setFixedSize(1280, 720)
        self.win = QWidget()
        self.setCentralWidget(self.win)
        self.list_games = QComboBox()
        for elem in self.db.data:
            self.list_games.addItem(elem[1])
        self.main_l = QVBoxLayout()
        self.main_l.addStretch()
        self.main_l.addWidget(self.list_games)


        self.list_games.currentTextChanged.connect(self.edit_configurator)
        self.accept_btn = QPushButton('Создать игру')

        h_l3 = QHBoxLayout()
        h_l3.addStretch(5)
        h_l3.addWidget(self.accept_btn, 2)

        self.accept_btn.setObjectName('create')
        self.win.setObjectName('transparent')
        self.accept_btn.clicked.connect(partial(button_animation, btn=self.accept_btn, win=self, f=self.game_formation))
        self.accept_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5,
                                                                    xOffset=4,
                                                                    yOffset=4,
                                                                    color=QColor(0, 0, 0)))
        self.main_l.addWidget(self.puzzle_win)
        self.main_l.addWidget(self.changeling_win)
        self.main_l.addStretch()
        self.main_l.addLayout(h_l3)

        self.win.setLayout(self.main_l)

    def edit_configurator(self):
        if self.list_games.currentText() == 'Пятнашки':
            self.puzzle_win.show()
            self.changeling_win.hide()
        elif self.list_games.currentText() == 'Перевёртыши':
            self.puzzle_win.hide()
            self.changeling_win.show()
        else:
            self.puzzle_win.hide()
            self.changeling_win.hide()

    def puzzle_ui(self):
        self.puzzle_win = QWidget()
        main_l = QVBoxLayout()
        self.title = QLineEdit()
        self.title.setPlaceholderText('Введите название игры')
        self.image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
        self.image.setStyleSheet('border: 1px solid black;')
        self.image.setScaledContents(False)
        self.image.setFixedSize(200, 200)
        self.add_image_btn = QPushButton('Добавить изображение')
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        main_l.addStretch()
        main_l.addWidget(self.title)
        h_l1.addWidget(self.image, 2)
        h_l1.addStretch(5)
        main_l.addLayout(h_l1, 3)
        h_l2.addWidget(self.add_image_btn, 2)
        h_l2.addStretch(5)
        main_l.addLayout(h_l2)
        main_l.addStretch()
        self.puzzle_win.setLayout(main_l)

        self.add_image_btn.setObjectName('create')
        self.puzzle_win.setObjectName('games')
        self.add_image_btn.clicked.connect(partial(button_animation, btn=self.add_image_btn, win=self, f=self.load_image))
        self.add_image_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))

    def changeling_ui(self):
        self.changeling_win = QWidget()
        self.changeling_win.setObjectName('games')
        main_l = QVBoxLayout()
        self.title = QLineEdit()
        self.title.setPlaceholderText('Введите название игры')
        images_l1 = QHBoxLayout()
        images_l2 = QHBoxLayout()
        self.images_list = []
        for i in range(4):
            image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
            image.setStyleSheet('border: 1px solid black;')
            image.setScaledContents(False)
            image.setFixedSize(200, 200)
            self.images_list.append(image)
            images_l1.addWidget(image)
        for i in range(4):
            image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
            image.setStyleSheet('border: 1px solid black;')
            image.setScaledContents(False)
            image.setFixedSize(200, 200)
            self.images_list.append(image)
            images_l2.addWidget(image)
        self.add_image_btn = QPushButton('Добавить изображение')
        main_l.addWidget(self.title)
        main_l.addLayout(images_l1)
        main_l.addLayout(images_l2)
        main_l.addWidget(self.add_image_btn)
        self.changeling_win.setLayout(main_l)

        self.add_image_btn.clicked.connect(partial(button_animation, btn=self.add_image_btn, win=self, f=self.load_image))
        self.add_image_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))

    def load_image(self, count_image=8):
        fnames, _ = QFileDialog.getOpenFileNames(self, 'Open files', '/home', "Images (*.png *.jpeg *.jpg)")
        if len(fnames) == count_image:
            self.pixmaps = []
            self.byte_images = []
            for fname in fnames:
                pixmap = QPixmap.fromImage(QImage(fname))
                self.pixmaps.append(pixmap)
                with open(fname, 'rb') as file:
                    byte_image = file.read()
                    self.byte_images.append(byte_image)
            for i in range(8):
                self.images_list[i].setPixmap(self.pixmaps[i])
        else:
            QMessageBox.warning(self, 'Недостаточно изображений', 'Необходимо выбрать 8 картинок', buttons=QMessageBox.Ok)

    def game_formation(self):
        self.title.setStyleSheet('''''')
        if not self.title.text():
            self.title.setStyleSheet('''border: 1px solid red;''')
        elif not self.image.pixmap():
            self.image.setStyleSheet('''border: 1px solid red;''')
        else:
            id_type = [x[0] for x in self.db.data if x[1] == self.list_games.currentText()][0]
            text = self.title.text()
            print(id_type, text)
            self.db.add_game(id_type=id_type, text=text, picture=self.byte_image)
            self.close()