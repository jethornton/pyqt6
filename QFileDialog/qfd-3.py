#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("File Dialog Example")
		self.setGeometry(50, 50, 1000, 1000)

		button = QPushButton("Open File", self)
		button.clicked.connect(self.openFileDialog)
		self.setCentralWidget(button)

	def openFileDialog(self):
		dialog = QFileDialog(self)
		dialog.setStyleSheet('''
		QPushButton:hover {
		background-color: red);
		color: white;
		}
		''')
		dialog.setWindowTitle("Select File")

		if dialog.exec():
			#filename = dialog.getOpenFileName()
			print("Selected file:", filename)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
