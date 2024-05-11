from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPainter
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGroupBox, QApplication


class ScaledPixmapLabel(QLabel):
    scaled = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(1, 1)

    def resizeEvent(self, event):
        if self.pixmap() and not self.pixmap().isNull():
            self.scaled = self.pixmap().scaled(
                self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def paintEvent(self, event):
        if self.pixmap() and not self.pixmap().isNull():
            if not self.scaled:
                self.scaled = self.pixmap().scaled(
                    self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            available = self.rect()
            rect = self.scaled.rect()
            rect.moveCenter(available.center())
            align = self.alignment()
            if align & Qt.AlignLeft:
                rect.moveLeft(available.left())
            elif align & Qt.AlignRight:
                rect.moveRight(available.right())
            if align & Qt.AlignTop:
                rect.moveTop(available.top())
            elif align & Qt.AlignBottom:
                rect.moveBottom(available.bottom())
            qp = QPainter(self)
            qp.drawPixmap(rect, self.scaled)
