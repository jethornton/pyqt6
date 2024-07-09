#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout
from PyQt6.QtWidgets import QSpinBox, QDoubleSpinBox

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
		sb = QSpinBox()
		layout.addWidget(sb)
		dsb = QDoubleSpinBox()
		layout.addWidget(dsb)


		with open('spinbox.qss','r') as fh:
			self.setStyleSheet(fh.read())
		self.show()

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

