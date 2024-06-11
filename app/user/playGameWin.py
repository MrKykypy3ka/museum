from functools import partial
from random import shuffle
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QCheckBox, QPushButton, \
    QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from components.new_widgets import ScaledPixmapLabel, OutlineLabel
from components.functions import load_image_pixmap, button_animation, load_image_icon
import pickle


class PlayGameWin(QWidget):

    def init_play_puzzle_ui(self):
        self.puzzle_win = QWidget()
        self.setCentralWidget(self.puzzle_win)
        main_l = QVBoxLayout()
        self.puzzle_win.setLayout(main_l)

    def init_play_changeling_ui(self):
        self.changeling_win = QWidget()
        self.setCentralWidget(self.changeling_win)
        self.title = OutlineLabel('', '#E8C68D', '#70000E')
        self.group_pictures = QGroupBox()
        group_main_l = QVBoxLayout()
        pictures_layouts = []
        self.pictures_list = []
        self.group_pictures.setLayout(group_main_l)
        self.back = QPushButton(' ← Назад')
        for i in range(4):
            pictures_layouts.append(QHBoxLayout())
            group_main_l.addLayout(pictures_layouts[-1])
            pictures_layouts[i].addStretch()
            for j in range(4):
                button = QPushButton()
                button.index = 4 * i + j + 1
                button.setObjectName('game')
                button.clicked.connect(self.check_picture)
                pictures_layouts[i].addWidget(button)
                pictures_layouts[i].addStretch()
                self.pictures_list.append(button)
        main_l = QVBoxLayout()
        main_l.addWidget(self.title)
        group_l = QHBoxLayout()
        group_l.addStretch()
        group_l.addWidget(self.group_pictures)
        group_l.addStretch()
        main_l.addLayout(group_l)
        back_l = QHBoxLayout()
        back_l.addStretch()
        back_l.addWidget(self.back)
        main_l.addLayout(back_l)
        self.changeling_win.setLayout(main_l)
        self.game_formation(self.list_activity.currentItem().text())


        self.back.setObjectName('main')
        self.back.clicked.connect(partial(button_animation, btn=self.back, win=self, f=self.init_user_ui))
        self.back.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))

    def check_picture(self):
        print(self.sender().index)

    def game_formation(self, text_game):
        self.setWindowTitle(f'Краеведческий музей Благовещенска: Тест - {text_game}')
        self.db.get_game(id_game=[x[0] for x in self.filter if text_game == x[2]][0])
        self.title.setText(self.db.data[0][0])
        self.pictures = pickle.loads(self.db.data[0][1]) + pickle.loads(self.db.data[0][1])
        shuffle(self.pictures)
        for button in self.pictures_list:
            # button.setIcon(load_image_icon(self.pictures[button.index]))
            temp = self.pictures[button.index - 1]
            icon = QIcon(load_image_icon(temp))
            button.setIcon(icon)
            button.setIconSize(button.size())
