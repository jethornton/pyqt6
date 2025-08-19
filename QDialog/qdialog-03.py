#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout
	
class MyDialog(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Minimal QDialog")
		self.button = QPushButton("Close", self)
		self.button.clicked.connect(self.accept)
		layout = QVBoxLayout(self)
		layout.addWidget(self.button)
		self.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	dialog = MyDialog()
	if dialog.exec():
		print("Dialog accepted")
	else:
		print("Dialog rejected")
	app.exec()
