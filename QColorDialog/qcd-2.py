#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QColorDialog, QWidget, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

class ColorPicker(QWidget):
	def __init__(self):
		super().__init__()

		self.button = QPushButton('Pick Color', self)
		self.button.clicked.connect(self.choose_color)

	def choose_color(self):
		color_dialog = QColorDialog(self)
		color_dialog.setOption(QColorDialog.ColorDialogOption.DontUseNativeDialog)
		color_dialog.setCurrentColor(QColor(255, 0, 0)) # Set initial color

		if color_dialog.exec():
			color = color_dialog.selectedColor()
			print("Selected color:", color.name()) 

if __name__ == '__main__':
	app = QApplication([])
	window = ColorPicker()
	window.show()
	app.exec()
