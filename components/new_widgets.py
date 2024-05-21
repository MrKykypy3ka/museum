from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFontMetrics, QColor
from PyQt5.QtWidgets import QLabel


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


class OutlineLabel(QLabel):
    def __init__(self, text, backcolor, outline_color):
        super().__init__(text)
        self.setFont(self.font())
        self.outline_color = outline_color
        self.backcolor = backcolor

    def paintEvent(self, event):
        painter = QPainter(self)
        font_metrics = QFontMetrics(self.font())

        # Контур
        painter.setPen(QColor(self.outline_color))
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                if dx != 0 or dy != 0:
                    painter.drawText(self.rect().adjusted(dx, dy, dx, dy), Qt.AlignCenter, self.text())
        # Основной текст
        painter.setPen(QColor(self.backcolor))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())