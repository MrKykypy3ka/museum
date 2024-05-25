from functools import partial
from components.new_widgets import OutlineLabel

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QListWidget, QMainWindow, \
    QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSignal

from components.functions import button_animation
from database.scripts.db import Data
from app.admin.createTaskWin import CreateTaskWin


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