#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(50, 50, 750, 750)
		button = QPushButton("Open File", self)
		button.clicked.connect(self.get_file_names)
		self.setCentralWidget(button)

		self.show()
		#self.get_file_names()


	def get_file_names(self):
		dialog = QFileDialog()
		dialog.setStyleSheet('''
		QPushButton:hover {
		background-color: rgba(0, 96, 192, 90%);
		color: white;
		}
		''')
		dialog.setWindowTitle('Specify File')
		dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
		dialog.setOptions(QFileDialog.Option.DontUseNativeDialog)
		file_path, file_type = dialog.getOpenFileName(self)
		#file_path, file_type = dial.exec()
		print(file_path)
		#if dial.exec() == QFileDialog.Accepted:
		#	path = dial.selectedFiles()[0]


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
