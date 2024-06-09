from functools import partial
from random import shuffle
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QCheckBox, QPushButton, \
    QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from components.new_widgets import ScaledPixmapLabel
from components.functions import load_image, button_animation


class PlayGameWin(QWidget):

    def init_play_puzzle_ui(self):
        self.puzzle_win = QWidget()
        self.setCentralWidget(self.puzzle_win)
        main_l = QVBoxLayout()

        self.puzzle_win.setLayout(main_l)

    def init_play_changeling_ui(self):
        self.changeling_win = QWidget()
        self.setCentralWidget(self.changeling_win)
        self.title =  QLabel()
        self.group_pictures = QGroupBox()
        group_main_l = QVBoxLayout()
        group_list = []
        self.group_pictures.setLayout(group_main_l)
        self.pictures = [[] for _ in range(4)]
        for i in range(4):
            group_list.append(QHBoxLayout())
            group_main_l.addLayout(group_list[0])
            for j in range(4):
                button = QPushButton(str((i+1)*(j+1)+j))
                group_list[i].addWidget(button)
        main_l = QVBoxLayout()
        self.changeling_win.setLayout(main_l)