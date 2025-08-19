#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

class CircleButton(QPushButton):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.draw_circle = False

	def paintEvent(self, event):
		super().paintEvent(event)
		if self.draw_circle:
			painter = QPainter(self)
			painter.setBrush(QColor('green'))
			painter.setPen(Qt.PenStyle.NoPen)
			diameter = 15
			right_pad = 10
			offset = (self.width() - diameter) - right_pad
			painter.drawEllipse(offset, 10, diameter, diameter)
			painter.end()

	def set_draw_circle(self, draw):
		 self.draw_circle = draw
		 self.update()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	button = CircleButton("Paint Circle")
	button.setFixedSize(100, 100)
	button.clicked.connect(lambda: button.set_draw_circle(not button.draw_circle))
	button.show()
	sys.exit(app.exec())

'''
self.width() - 
 self.height() - 

'''
