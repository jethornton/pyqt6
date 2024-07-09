#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PyQt6.QtWidgets import QLineEdit, QVBoxLayout

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		layout = QVBoxLayout(central_widget)
		self.lb = QLabel('click me')
		layout.addWidget(self.lb)
		self.le = QLineEdit()
		self.le.mousePressEvent = self.clicked
		layout.addWidget(self.le)
		self.le2 = QLineEdit()
		self.le2.mousePressEvent = self.clicked

		self.show()

	def clicked(self, mouseEvent):
		print(self.sender().objectName())
		print('here')

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

