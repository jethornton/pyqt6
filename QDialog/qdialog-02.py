#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout

class MyDialog(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My Dialog")
		layout = QVBoxLayout()

		ok_button = QPushButton("OK")
		ok_button.clicked.connect(self.accept)
		layout.addWidget(ok_button)

		cancel_button = QPushButton("Cancel")
		cancel_button.clicked.connect(self.reject)
		layout.addWidget(cancel_button)

		self.setLayout(layout)
		self.accepted.connect(self.on_accepted)
		self.rejected.connect(self.on_rejected)

	def on_accepted(self):
		print("Dialog accepted!")

	def on_rejected(self):
		print('Dialog rejected')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	dialog = MyDialog()
	if dialog.exec():
		print("Dialog result: Accepted")
	else:
		print("Dialog result: Rejected")
	app.exec()
