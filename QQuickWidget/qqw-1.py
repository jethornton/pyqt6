#!/usr/bin/env python3

import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'qqw-1.ui'), self)
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT6 QQuickWidget!")
		self.show()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())
