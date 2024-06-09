import sys
from PyQt5.Qt import *


class Example(QWidget):
    def __init__(self):
        super().__init__()

        cb = QCheckBox('Show title', self)
        cb.stateChanged.connect(self.changeTitle)

        vbox = QVBoxLayout(self)
        vbox.addWidget(cb)

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('Hrllo Worjd')


StyleSheet = '''
QCheckBox {
    spacing: 5px;
    font-size:25px;     
}

QCheckBox::indicator {
    width:  33px;
    height: 33px;
}
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    ex = Example()
    ex.resize(300, 200)
    ex.show()
    sys.exit(app.exec_())