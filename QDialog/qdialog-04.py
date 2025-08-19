#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QLineEdit, QPushButton, QDialogButtonBox
from PyQt6.QtCore import Qt
	
class MyDialog(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("My Dialog")

		self.name_label = QLabel("Name:")
		self.name_input = QLineEdit()

		button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
		button_box.accepted.connect(self.accept)
		button_box.rejected.connect(self.reject)

		layout = QVBoxLayout()
		layout.addWidget(self.name_label)
		layout.addWidget(self.name_input)
		layout.addWidget(button_box)
		self.setLayout(layout)

	def get_name(self):
		return self.name_input.text()

if __name__ == '__main__':
	app = QApplication([])

	dialog = MyDialog()
	result = dialog.exec()

	if result == QDialog.DialogCode.Accepted:
		name = dialog.get_name()
		print(f"Entered name: {name}")
	else:
		print("Dialog cancelled")
