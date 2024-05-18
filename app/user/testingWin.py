from functools import partial

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QCheckBox, QPushButton, \
    QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from components.new_widgets import ScaledPixmapLabel
from components.functions import load_image, button_animation


class TestingWin(QWidget):
    def init_testing_ui(self):
        wid = QWidget()
        self.setCentralWidget(wid)
        self.resize(600, 400)
        self.setWindowIcon(QIcon('resources/favicon.ico'))

        self.question = QLabel()
        self.image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
        self.image.setStyleSheet('border: 1px solid black;')
        self.image.setScaledContents(False)
        self.image.setFixedSize(200, 200)
        self.accept = QPushButton('Ответить')

        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        h_l4 = QHBoxLayout()
        answers_group = QGroupBox('Ответы')
        main_l.addStretch()
        main_l.addWidget(self.question)
        h_l1.addStretch(5)
        h_l1.addWidget(self.image, 2)
        h_l1.addStretch(5)
        main_l.addLayout(h_l1, 3)
        main_l.addLayout(h_l2)
        self.vg_l = QVBoxLayout()
        answers_group.setLayout(self.vg_l)
        main_l.addWidget(answers_group)
        h_l4.addStretch()
        h_l4.addWidget(self.accept)
        main_l.addLayout(h_l4)
        main_l.addStretch()
        wid.setLayout(main_l)

        self.task_formation(self.list_tests.currentItem().text())

        self.accept.clicked.connect(partial(button_animation, btn=self.accept, win=self, f=self.next_task))
        self.accept.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5,
                                                                   xOffset=4,
                                                                   yOffset=4,
                                                                   color=QColor(0, 0, 0)))

    def add_answer(self, text_test):
        if len(self.answers) < 8:
            correct = QCheckBox(text_test)
            h_l = QHBoxLayout()
            h_l.addWidget(correct)
            self.vg_l.addLayout(h_l)

    def task_formation(self, text_test):
        self.setWindowTitle(f'Краеведческий музей Благовещенска: Тест - {text_test}')
        self.db.get_test(id_test=[x[0] for x in self.filter if text_test in x[2]][0])
        print(self.db.data)
        self.answers = [(x[2], x[3]) for x in self.db.data]
        self.question.setText(self.db.data[0][0])
        print(self.answers)
        for i in range(len(self.answers)):
            self.add_answer(self.answers[i][0])
        self.adjustSize()
        self.image.setPixmap(load_image(self.db.data[0][1]))

    def next_task(self):
        pass
