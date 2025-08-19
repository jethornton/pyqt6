#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt6.QtGui import QColor
	
class ColorPicker(QWidget):
	def __init__(self):
		super().__init__()

		self.button = QPushButton("Choose Color", self)
		self.button.clicked.connect(self.openColorDialog)

	def openColorDialog(self):
		initial_color = QColor(255, 0, 0)  # Initial color: Red
		color_dialog = QColorDialog(initial_color, self)

		if color_dialog.exec():
			selected_color = color_dialog.selectedColor()
			print("Selected Color:", selected_color.name())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ColorPicker()
	window.show()
	sys.exit(app.exec())
