from functools import partial
from random import shuffle
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QCheckBox, QPushButton, \
    QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from components.new_widgets import ScaledPixmapLabel, OutlineLabel
from components.functions import load_image_pixmap, button_animation


class TestingWin(QWidget):
    def init_testing_ui(self):
        self.current_task = -1
        self.answers_users = dict()
        self.answers_true = dict()
        self.answers = []

        self.wid = QWidget()
        self.setCentralWidget(self.wid)
        self.setWindowIcon(QIcon('resources/favicon.ico'))

        self.question = OutlineLabel('', '#E8C68D', '#70000E')
        self.image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
        self.image.setFixedWidth(500)
        self.accept = QPushButton(' Ответить')

        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        h_l4 = QHBoxLayout()
        self.answers_label = OutlineLabel('Ответы', '#E8C68D', '#70000E')
        self.answers_group = QGroupBox('')
        main_l.addStretch()
        main_l.addWidget(self.question)
        h_l1.addStretch(5)
        h_l1.addWidget(self.image, 2)
        h_l1.addStretch(5)
        main_l.addLayout(h_l1, 3)
        main_l.addLayout(h_l2)
        self.vg_l = QVBoxLayout()
        self.answers_group.setLayout(self.vg_l)
        main_l.addWidget(self.answers_label, alignment=Qt.AlignLeft)
        main_l.addWidget(self.answers_group)
        h_l4.addStretch()
        h_l4.addWidget(self.accept)
        main_l.addLayout(h_l4)
        main_l.addStretch()
        self.wid.setLayout(main_l)
        self.test_formation(self.list_activity.currentItem().text())

        self.accept.setObjectName('main')
        self.wid.setObjectName('transparent')
        self.accept.clicked.connect(partial(button_animation, btn=self.accept, win=self, f=self.next_task))
        self.accept.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5,
                                                                xOffset=4,
                                                                yOffset=4,
                                                                color=QColor(0, 0, 0)))

    def add_answer(self, text_test):
        correct = QCheckBox(text_test)
        correct.stateChanged.connect(self.save_answer)
        self.answers.append(correct)
        h_l = QHBoxLayout()
        h_l.addWidget(correct)
        self.vg_l.addLayout(h_l)

    def test_formation(self, text_test):
        self.setWindowTitle(f'Краеведческий музей Благовещенска: Тест - {text_test}')
        self.db.get_test(id_test=[x[0] for x in self.filter if text_test in x[2]][0])
        self.questions = list(set([(x[0], x[1]) for x in self.db.data]))
        shuffle(self.questions)
        self.tasks = dict()
        for task in self.db.data:
            if task[0] not in self.tasks:
                self.tasks[task[0]] = [task[2:]]
            else:
                self.tasks[task[0]].append(task[2:])
        for task in self.tasks:
            self.answers_true[task] = [answer[0] for answer in self.tasks[task] if answer[1] == 1]
        self.next_task()

    def task_formation(self):
        for elem in self.answers:
            elem.deleteLater()
        self.answers = []
        self.question.setText(self.questions[self.current_task][0])
        for answer in self.tasks[self.questions[self.current_task][0]]:
            self.add_answer(answer[0])
        if self.questions[self.current_task][1]:
            self.image.setPixmap(load_image_pixmap(self.questions[self.current_task][1]))
        self.answers_users[self.questions[self.current_task][0]] = []

    def next_task(self):
        if any([True if x.isChecked() else False for x in self.answers]) or self.answers_users == dict():
            if self.accept.text() == ' Завершить':
                self.show_results()
            if self.current_task < len(self.questions) - 1:
                self.current_task += 1
                self.task_formation()
                if self.current_task == len(self.questions) - 1:
                    self.accept.setText(' Завершить')

    def save_answer(self):
        if self.sender().isChecked():
            self.answers_users[self.questions[self.current_task][0]].append(self.sender().text())
        else:
            self.answers_users[self.questions[self.current_task][0]].remove(self.sender().text())

    def show_results(self):
        self.score = 0
        result = 0
        for question in self.answers_users:
            if self.answers_true[question] == self.answers_users[question]:
                result += 1
        self.result_win = QMessageBox()
        self.result_win.setText(f'Твой результат: {result} из {self.current_task + 1}')
        self.result_win.show()
        if self.result_win.exec_():
            self.init_user_ui()
