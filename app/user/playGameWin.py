from functools import partial
from random import shuffle
from time import sleep

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QCheckBox, QPushButton, \
    QGraphicsDropShadowEffect, QMessageBox, QTimeEdit
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt, QTimer
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
        self.one_picture = None
        self.two_picture = None
        self.score = 0
        self.changeling_win = QWidget()
        self.setCentralWidget(self.changeling_win)
        self.title = OutlineLabel('', '#E8C68D', '#70000E')
        self.time_lbl = OutlineLabel('00:0', '#E8C68D', '#70000E')
        self.timer = QTimer()
        self.mseconds = 0
        self.seconds = 0
        self.minutes = 0
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
        main_l.addWidget(self.time_lbl)
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
        self.timer.timeout.connect(self.showTime)
        self.back.setObjectName('main')
        self.back.clicked.connect(partial(button_animation, btn=self.back, win=self, f=self.init_user_ui))
        self.back.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.timer.start(1)

    def check_picture(self):
        if type(self.sender()) is QPushButton:
            self.start = self.mseconds
            self.sender().setIcon(QIcon(load_image_icon(self.sender().picture)))
            self.sender().setIconSize(self.sender().size())
            if self.sender().picture:
                if self.one_picture is None:
                    self.one_picture = self.sender()
                elif self.two_picture is None:
                    self.two_picture = self.sender()

        if self.one_picture and self.two_picture and self.mseconds - self.start > 120:
            self.one_picture.setIcon(QIcon())
            self.two_picture.setIcon(QIcon())
            if self.one_picture.picture == self.two_picture.picture:
                self.one_picture.setStyleSheet('background-color: rgba(60, 60, 60, 100);')
                self.two_picture.setStyleSheet('background-color: rgba(60, 60, 60, 100);')
                self.one_picture.setEnabled(False)
                self.two_picture.setEnabled(False)
                self.one_picture.picture = None
                self.two_picture.picture = None
                self.score += 1
            self.one_picture = None
            self.two_picture = None
        print(self.score)
        if self.score == 8:
            self.timer.stop()
            self.show_game_results()


    def game_formation(self, text_game):
        self.setWindowTitle(f'Краеведческий музей Благовещенска: Тест - {text_game}')
        self.db.get_game(id_game=[x[0] for x in self.filter if text_game == x[2]][0])
        self.title.setText(self.db.data[0][0])
        self.pictures = pickle.loads(self.db.data[0][1])
        self.pictures *= 2
        shuffle(self.pictures)
        for button in self.pictures_list:
            button.picture = self.pictures[button.index - 1]

    def showTime(self):
        self.mseconds += 1
        if self.mseconds % 1000 == 0:
            self.seconds += 1
            if self.seconds % 60 == 0:
                self.seconds = 0
                self.minutes += 1
        self.time_lbl.setText(f'0{self.minutes}:{self.seconds}:{self.mseconds%1000}')
        self.check_picture()

    def show_game_results(self):
        self.result_win = QMessageBox()
        self.result_win.setText(f'Твой результат: 0{self.minutes}:{self.seconds}:{self.mseconds}')
        self.result_win.show()
        if self.result_win.exec_():
            self.init_user_ui()
