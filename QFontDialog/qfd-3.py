#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFontDialog

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.button = QPushButton("Choose Font", self)
		self.button.clicked.connect(self.choose_font)

	def choose_font(self):
		options = QFontDialog.FontDialogOption.MonospacedFonts
		options |= QFontDialog.FontDialogOption.DontUseNativeDialog

		font, ok = QFontDialog.getFont(self.font(), self, "Choose a Font", options)
		if ok:
			self.setFont(font)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
