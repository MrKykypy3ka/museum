from PyQt5.QtWidgets import QApplication
from app.mainWin import MainWin
import sys


def main():
    app = QApplication([])
    app.setStyleSheet("\n".join(open('styles/style.css').readlines()))
    win = MainWin()
    win.showFullScreen()
    sys.exit(app.exec_())


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))


sys.excepthook = excepthook

if __name__ == '__main__':
    main()
