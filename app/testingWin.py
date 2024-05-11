from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QGroupBox, QFileDialog, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import QSize, Qt, pyqtSignal
from classes.new_widgets import ScaledPixmapLabel

class TaskWin(QWidget):
    data_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.byte_image = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска: создание вопроса')
        self.resize(600, 400)
        self.setFixedWidth(600)
        self.setWindowIcon(QIcon('resources/favicon.ico'))