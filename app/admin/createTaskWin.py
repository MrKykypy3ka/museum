from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox, QFileDialog, QCheckBox, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt, pyqtSignal
from components.new_widgets import ScaledPixmapLabel


class CreateTaskWin(QMainWindow):
    data_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.byte_image = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Краеведческий музей Благовещенска: создание вопроса')
        self.resize(600, 400)
        # self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('resources/favicon.ico'))
        win = QWidget()
        self.setCentralWidget(win)
        win.setObjectName('transparent')
        self.question = QLineEdit()
        self.question.setPlaceholderText('Введите название вопроса')
        self.image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
        self.image.setStyleSheet('border: 1px solid black;')
        self.image.setScaledContents(False)
        self.image.setFixedSize(200, 200)
        self.add_image = QPushButton('Добавить изображение')
        self.answers = list()
        self.add_task = QPushButton('Добавить вопрос')
        self.add_answer_btn = QPushButton('+')
        self.del_answer_btn = QPushButton('-')
        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        h_l3 = QHBoxLayout()
        h_l4 = QHBoxLayout()
        answers_group = QGroupBox('Ответы')
        main_l.addStretch()
        main_l.addWidget(self.question)
        h_l1.addWidget(self.image, 2)
        h_l1.addStretch(5)
        main_l.addLayout(h_l1, 3)
        h_l2.addWidget(self.add_image, 2)
        h_l2.addStretch(5)
        main_l.addLayout(h_l2)
        self.vg_l = QVBoxLayout()
        for _ in range(1, 3):
            self.add_answer()
        answers_group.setLayout(self.vg_l)
        main_l.addWidget(answers_group)
        h_l3.addWidget(self.del_answer_btn, 1)
        h_l3.addWidget(self.add_answer_btn, 1)
        h_l3.addStretch(5)
        main_l.addLayout(h_l3)
        h_l4.addStretch(5)
        h_l4.addWidget(self.add_task, 2)
        main_l.addLayout(h_l4)
        main_l.addStretch()
        win.setLayout(main_l)
        self.add_answer_btn.clicked.connect(self.add_answer)
        self.del_answer_btn.clicked.connect(self.del_answer)
        self.add_image.clicked.connect(self.load_image)
        self.add_task.clicked.connect(self.task_formation)
        self.data_signal.connect(self.close)

    def add_answer(self):
        if len(self.answers) < 8:
            answer = QLineEdit()
            answer.setPlaceholderText(f'Запишите {len(self.answers)+1}-й варинат ответа')
            correct = QCheckBox()
            self.answers.append((correct, answer))
            h_l = QHBoxLayout()
            h_l.addWidget(correct)
            h_l.addWidget(answer)
            self.vg_l.addLayout(h_l)
            self.adjustSize()

    def del_answer(self):
        if len(self.answers) > 2:
            self.answers[-1][0].deleteLater()
            self.answers[-1][1].deleteLater()
            self.answers = self.answers[:-1]
            self.adjustSize()

    def load_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', "Images (*.png *.jpeg *.jpg)")
        if fname[0]:
            self.pixmap = QPixmap.fromImage(QImage(fname[0]))
            self.image.setPixmap(self.pixmap)
            with open(fname[0], 'rb') as file:
                self.byte_image = file.read()

    def task_formation(self):
        self.check_correct()
        if not self.bad_answers and self.question.text():
            self.task = list()
            self.task.append(self.question.text())
            self.task.append(self.byte_image)
            self.task.append([])
            for i in range(len(self.answers)):
                self.task[2].append((self.answers[i][0].isCheckable(), self.answers[i][1].text()))
            self.close()
        elif not self.question.text():
            self.question.setStyleSheet('''border: 1px solid red;''')
        elif self.question.text():
            self.question.setStyleSheet('''''')

    def check_correct(self):
        for i in range(len(self.answers)):
            self.answers[i][1].setStyleSheet('''''')
        self.bad_answers = 0
        for i in range(len(self.answers)):
            for j in range(len(self.answers)):
                if self.answers[i][1] != self.answers[j][1] and self.answers[i][1].text() == self.answers[j][1].text():
                    self.bad_answers += 1
                    self.answers[i][1].setStyleSheet('''border: 1px solid red;''')
                    self.answers[j][1].setStyleSheet('''border: 1px solid red;''')

    def closeEvent(self, event):
        self.data_signal.emit(self.task)
        event.accept()
