#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import Qt, QRect

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('QPainter Example')
		self.show()

	def paintEvent(self, event):
		qp = QPainter(self)
		self.draw_shapes(qp)
		qp.end()

	def draw_shapes(self, qp):
		# Pen Styles
		qp.setPen(QColor(Qt.GlobalColor.red))
		qp.drawLine(20, 30, 200, 30)

		qp.setPen(QColor(Qt.GlobalColor.green))
		qp.drawRect(20, 60, 180, 40)

		qp.setPen(QColor(Qt.GlobalColor.blue))
		qp.drawEllipse(20, 110, 180, 40)
		
		# Brush Styles
		qp.setBrush(QColor(Qt.GlobalColor.yellow))
		qp.drawRect(220, 60, 100, 40)

		qp.setBrush(QColor(200, 100, 50))
		qp.drawEllipse(220, 110, 100, 40)

		# Text
		qp.setPen(QColor(Qt.GlobalColor.black))
		qp.setFont(QFont('Arial', 15))
		qp.drawText(QRect(20, 160, 300, 30), Qt.AlignmentFlag.AlignCenter, "PyQt6 Drawing Example")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())
