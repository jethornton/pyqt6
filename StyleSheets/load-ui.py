#!/usr/bin/env python3

import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPalette, QColor
from PyQt6 import uic

import resources

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'load-ui.ui'), self)
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT6 Load UI File!")
		# Now use a palette to switch to dark colors:
		palette = QPalette()
		palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
		palette.setColor(QPalette.ColorRole.WindowText, QColor('white'))
		palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
		palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
		palette.setColor(QPalette.ColorRole.ToolTipBase, QColor('white'))
		palette.setColor(QPalette.ColorRole.ToolTipText, QColor('white'))
		palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, QColor('white'))
		palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, QColor(53, 53, 53))
		palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, QColor('white'))
		palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, QColor('red'))
		palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
		palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
		palette.setColor(QPalette.ColorRole.HighlightedText, QColor('black'))
		palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, QColor(35, 35, 35))
		palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(35, 35, 35))
		app.setPalette(palette)

		with open('load-ui.qss','r') as fh:
			self.setStyleSheet(fh.read())
		self.show()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())
