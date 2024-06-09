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
        main_l = QVBoxLayout()

        self.changeling_win.setLayout(main_l)