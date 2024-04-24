#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PyQt6.QtWidgets import QDialogButtonBox, QVBoxLayout, QLabel, QComboBox
from PyQt6.QtWidgets import QWidget

class CustomDialog(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Editor not found!")

		QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		self.layout = QVBoxLayout()
		message = QLabel("Select the Editor to use.")
		self.layout.addWidget(message)
		self.choice = QComboBox()
		self.choice.addItem('Select', False)
		editors = [['Gedit', 'gedit'], ['Geany', 'geany']]
		for key, value in editors:
			self.choice.addItem(key, value)
		self.layout.addWidget(self.choice)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")
		central_widget = QWidget()
		#self.layout = QVBoxLayout()
		self.setCentralWidget(central_widget)
		layout = QVBoxLayout(central_widget)
		dialog_button = QPushButton("Press me for Dialog!")
		dialog_button.clicked.connect(self.open_dialog)
		layout.addWidget(dialog_button)
		exit_button = QPushButton("Exit!")
		exit_button.clicked.connect(self.close)
		layout.addWidget(exit_button)
		self.show()

	def open_dialog(self, s):
		print("click", s)
		dlg = CustomDialog()
		if dlg.exec():
			print("Success!")
			if dlg.choice.currentData():
				print(dlg.choice.currentText())
			else:
				print('No Editor Selected!')
		else:
			print("Cancel!")


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
