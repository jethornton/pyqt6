#!/usr/bin/env python3

import sys, os
# disable cache usage must be before any local imports
sys.dont_write_bytecode = True


from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6 import uic


#from qss import Ui_MainWindow


class example(QMainWindow):
	def __init__(self):
		super().__init__()
		#self.setupUi(self)
		# get the path to the executable
		self.path = os.path.dirname(os.path.realpath(sys.argv[0]))

		# set the library path
		if self.path == '/usr/bin':
			self.gui_path = '/usr/lib/libflexgui'
		else:
			self.gui_path = self.path
		uic.loadUi(os.path.join(self.gui_path, 'qss.ui'), self)

		# Add any additional functionality here

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		#main_window = ()  # Create a main window (optional)
		self.button = QPushButton("Push for Window")
		self.button.clicked.connect(self.open_example)
		self.setCentralWidget(self.button)
		self.new_window = example()

		self.show()

	def open_example(self):
		self.new_window.show()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())

