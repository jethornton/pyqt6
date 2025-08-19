#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import QRect
import sys

class MyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(100, 100, 300, 200)
		self.button = QPushButton("Get Rect", self)
		self.button.clicked.connect(self.print_rect)

	def print_rect(self):
		rect: QRect = self.rect()
		print(f"Widget Rect: x={rect.x()}, y={rect.y()}, width={rect.width()}, height={rect.height()}")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = MyWidget()
	widget.show()
	sys.exit(app.exec())
