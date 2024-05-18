from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QListWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from database.scripts.db import Data
from app.admin.createTaskWin import CreateTaskWin


class CreateTestWin(QWidget):
    close_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.db = Data('database/Museum.db')
        self.init_ui()
        self.tasks = list()

    def init_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска: создание теста')
        self.resize(500, 400)
        self.setFixedWidth(500)
        # self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        self.title = QLineEdit()
        self.title.setPlaceholderText('Задайте название теста')
        answers_lbl = QLabel('Вопросы в тесте')
        self.tasks_list = QListWidget()
        self.add_answer_btn = QPushButton('Добавить вопрос')
        self.edit_answer_btn = QPushButton('Изменить вопрос')
        self.del_answer_btn = QPushButton('Удалить вопрос')
        self.write_test_btn = QPushButton('Сохранить тест')
        main_l = QVBoxLayout()
        main_l.addStretch()
        main_l.addWidget(self.title, 1)
        main_l.addWidget(answers_lbl)
        main_l.addWidget(self.tasks_list, 5)
        h_l1 = QHBoxLayout()
        h_l1.addWidget(self.add_answer_btn, 4)
        h_l1.addStretch(1)
        h_l1.addWidget(self.edit_answer_btn, 4)
        h_l1.addStretch(1)
        h_l1.addWidget(self.del_answer_btn, 4)
        main_l.addLayout(h_l1, 1)
        main_l.addStretch()
        h_l2 = QHBoxLayout()
        h_l2.addStretch(3)
        h_l2.addWidget(self.write_test_btn, 5)
        h_l2.addStretch(3)
        main_l.addLayout(h_l2)
        self.setLayout(main_l)
        self.add_answer_btn.clicked.connect(self.showCreateAnswerWin)
        self.write_test_btn.clicked.connect(self.test_formation)
        self.close_signal.connect(self.close)

    def showCreateAnswerWin(self):
        self.win_ct = CreateTaskWin()
        self.win_ct.data_signal.connect(self.addData)
        self.win_ct.show()

    def addData(self, data):
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
                    self.db.add_answer(id_task=id_task, text=answer[1], is_correct=answer[0])
            self.close()
        elif not self.title.text():
            self.title.setStyleSheet('''border: 1px solid red;''')
            self.tasks_list.setStyleSheet('''''')
        elif not len(self.tasks):
            self.tasks_list.setStyleSheet('''border: 1px solid red;''')
            self.title.setStyleSheet('''''')

    def closeEvent(self, event):
        self.close_signal.emit(True)
        event.accept()
