#!/usr/bin/env python3

import sys, os
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

import resources

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(50, 150, 400, 400)
		self.setWindowTitle('Main window')
		uic.loadUi(os.path.join(os. getcwd(), 'touch.ui'), self)
		with open('touch.qss','r') as fh:
			self.setStyleSheet(fh.read())
		self.show()

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

