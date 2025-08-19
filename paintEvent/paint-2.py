#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt

class MyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(100, 100, 300, 200)

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setPen(QPen(QColor(255, 0, 0), 5, Qt.PenStyle.SolidLine))
		painter.drawEllipse(50, 50, 100, 100)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = MyWidget()
	widget.show()
	sys.exit(app.exec())
