#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.view = QPlainTextEdit()
		layout = QVBoxLayout(central_widget)
		layout.addWidget(self.view)
		self.show()

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

