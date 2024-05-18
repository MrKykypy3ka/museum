from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from components.new_widgets import ScaledPixmapLabel


class TestingWin(QWidget):
    def init_testing_ui(self):
        wid = QWidget()
        self.setCentralWidget(wid)
        self.resize(600, 400)
        self.setFixedWidth(600)
        self.setWindowIcon(QIcon('resources/favicon.ico'))

        self.question = QLabel()
        self.image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
        self.image.setStyleSheet('border: 1px solid black;')
        self.image.setScaledContents(False)
        self.image.setFixedSize(200, 200)

        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        h_l4 = QHBoxLayout()
        answers_group = QGroupBox('Ответы')
        main_l.addStretch()
        main_l.addWidget(self.question)
        h_l1.addWidget(self.image, 2)
        h_l1.addStretch(5)
        main_l.addLayout(h_l1, 3)
        main_l.addLayout(h_l2)
        self.vg_l = QVBoxLayout()
        answers_group.setLayout(self.vg_l)
        main_l.addWidget(answers_group)
        main_l.addLayout(h_l4)
        main_l.addStretch()
        wid.setLayout(main_l)

        self.task_formation(self.list_tests.currentItem().text())

    def add_answer(self):
        if len(self.answers) < 8:
            answer = QLabel()
            correct = QCheckBox()
            self.answers.append((correct, answer))
            h_l = QHBoxLayout()
            h_l.addWidget(correct)
            h_l.addWidget(answer)
            self.vg_l.addLayout(h_l)
            self.adjustSize()

    def task_formation(self, text_test):
        self.setWindowTitle(f'Краеведческий музей Благовещенска: Тест - {text_test}')
        self.db.get_test(id_test=[x[0] for x in self.filter if text_test in x[2]][0])
        print(self.db.data)
        self.answers = [(x[2], x[3]) for x in self.db.data]
        print(self.answers)
        for _ in range(1, 3):
            self.add_answer()
