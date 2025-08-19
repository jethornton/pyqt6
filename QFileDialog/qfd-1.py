#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.show()
		self.get_file_names()


	def get_file_names(self):
		options = QFileDialog.Option.DontUseNativeDialog
		files, _ = QFileDialog.getOpenFileNames(self,"Open Muliple Files",
		"","All Files (*);;Python Files (*.py)", options=options)
		if files:
			print(files)
		self.close()

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
