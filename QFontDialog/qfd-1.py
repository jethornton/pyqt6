#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QFontDialog, QPushButton
from PyQt6.QtGui import QFont  # Import QFont class

def open_font_dialog():
	initial_font = QFont("Monospace", 12)
	font, ok = QFontDialog.getFont(initial_font)
	if ok:
		print("Selected Font:", font.toString())

app = QApplication([])
button = QPushButton("Select Font")
button.clicked.connect(open_font_dialog)
button.show()
app.exec()

