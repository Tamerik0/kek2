import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pixmap = QPixmap(self.width(), self.height())
        self.pixmap.fill(QColor(0, 0, 0, 0))

        def click():
            painter = QPainter(self.pixmap)
            painter.setBrush(QColor(255, 255, 0))
            r = random.randint(10, 300)
            painter.drawEllipse(random.randrange(0, self.width()), random.randrange(0, self.height()), r, r)
            self.repaint()

        self.pushButton.clicked.connect(click)

    def paintEvent(self, a0):
        QPainter(self).drawPixmap(0, 0, self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    app.exec()
