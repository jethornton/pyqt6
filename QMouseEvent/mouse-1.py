#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.qpte = QPlainTextEdit("Click in this window")
		self.setCentralWidget(self.qpte)

	def mouseMoveEvent(self, e):
		print("mouseMoveEvent")

	def mousePressEvent(self, e):
		print("mousePressEvent")

	def mouseReleaseEvent(self, e):
		print("mouseReleaseEvent")

	def mouseDoubleClickEvent(self, e):
		print("mouseDoubleClickEvent")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

