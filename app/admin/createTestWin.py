from functools import partial
from components.new_widgets import OutlineLabel

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QListWidget, QMainWindow, \
    QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSignal

from components.functions import button_animation
from database.scripts.db import Data
from app.admin.createTaskWin import CreateTaskWin


class CreateTestWin(QMainWindow):
    close_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.db = Data('database/Museum.db')
        self.init_ui()
        self.tasks = list()
        self.set_style()

    def init_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска: создание теста')
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        self.resize(1280, 720)
        self.setFixedSize(1280, 720)
        win = QWidget()
        win.setObjectName('transparent')
        self.setCentralWidget(win)
        self.title = QLineEdit()
        self.title.setPlaceholderText('Задайте название теста')
        answers_lbl = OutlineLabel('Вопросы', '#E8C68D', '#70000E')
        self.tasks_list = QListWidget()
        self.add_answer_btn = QPushButton('Добавить вопрос')
        self.edit_answer_btn = QPushButton('Изменить вопрос')
        self.del_answer_btn = QPushButton('Удалить вопрос')
        self.write_test_btn = QPushButton('Сохранить викторину')
        self.back = QPushButton('← Назад')

        main_l = QVBoxLayout()
        main_l.addStretch()
        main_l.addWidget(self.title, 1)
        main_l.addWidget(answers_lbl)
        main_l.addWidget(self.tasks_list, 5)
        h_l1 = QHBoxLayout()
        h_l1.addWidget(self.add_answer_btn, 1)
        h_l1.addStretch()
        h_l1.addWidget(self.edit_answer_btn, 1)
        h_l1.addStretch()
        h_l1.addWidget(self.del_answer_btn, 1)
        main_l.addLayout(h_l1, 1)
        main_l.addStretch()
        h_l2 = QHBoxLayout()
        h_l2.addWidget(self.back, 5)
        h_l2.addWidget(self.write_test_btn, 5)
        h_l2.addStretch(5)
        main_l.addLayout(h_l2)
        win.setLayout(main_l)
        self.add_answer_btn.clicked.connect(partial(button_animation, btn=self.add_answer_btn, win=self, f=self.show_create_answer_win))
        self.write_test_btn.clicked.connect(partial(button_animation, btn=self.write_test_btn, win=self,  f=self.test_formation))
        self.back.clicked.connect(partial(button_animation, btn=self.back, win=self, f=self.close))
        self.close_signal.connect(self.close)

    def show_create_answer_win(self):
        self.win_ct = CreateTaskWin()
        self.win_ct.data_signal.connect(self.add_data)
        self.win_ct.show()

    def add_data(self, data):
        self.tasks.append(data)
        self.tasks_list.addItem(data[0])

    def test_formation(self):
        if self.title.text() and len(self.tasks):
            self.db.get_type(name='Тест')
            id_type = self.db.data[0][0]
            self.db.add_test(id_type=id_type, text=self.title.text())
            self.db.get_text_test(text=self.title.text())
            id_test = self.db.data[0][0]
            for task in self.tasks:
                self.db.add_taks(id_test=id_test, text=task[0], picture=task[1])
                self.db.get_task(text=task[0])
                id_task = self.db.data[0][0]
                for answer in task[2]:
                    self.db.add_answer(id_question=id_task, text=answer[1], is_correct=answer[0])
            self.close()
        elif not self.title.text():
            self.title.setStyleSheet('''border: 1px solid red;''')
            self.tasks_list.setStyleSheet('''''')
        elif not len(self.tasks):
            self.tasks_list.setStyleSheet('''border: 1px solid red;''')
            self.title.setStyleSheet('''''')

    def closeEvent(self, event):
        self.close_signal.emit(True)
        event.accept_btn()

    def set_style(self):
        self.add_answer_btn.setObjectName('create')
        self.edit_answer_btn.setObjectName('create')
        self.del_answer_btn.setObjectName('create')
        self.back.setObjectName('create')
        self.write_test_btn.setObjectName('create')

        self.back.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.add_answer_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.write_test_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.edit_answer_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))
        self.del_answer_btn.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=4, yOffset=4, color=QColor(0, 0, 0)))