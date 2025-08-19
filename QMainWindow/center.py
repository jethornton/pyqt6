#!/usr/bin/env python3

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)
	
class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.setWindowTitle("Main Window")
		self.setGeometry(self.top, self.left, self.width, self.height)

		menu = self.menuBar()
		action = menu.addMenu("&Action")
		show_window2 = QAction("Show Window2", self)
		action.addAction(show_window2)
		show_window2.triggered.connect(self.show_window2_centered)

		self.show()

	def show_window2_centered(self):
		self.w = Window2(parent=self)
		self.w.show()

class Window2(QMainWindow):
	def __init__(self, parent=None):
		self.parent = parent
		super().__init__()
		self.setWindowTitle("Centered Window")

		geo = self.geometry()
		geo.moveCenter(self.parent.geometry().center())
		self.setGeometry(geo)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec())

