#!/usr/bin/env python3

import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		path = os.path.join(os. getcwd(), 'oglw6-10.ui')
		print(path)
		uic.loadUi('oglw6-10.ui', self)
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT6 Open GL Widget")
		self.show()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())
