#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

	
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")

		button = QPushButton("Press me!")
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)
		self.show()

	def button_clicked(self, s):
		print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
