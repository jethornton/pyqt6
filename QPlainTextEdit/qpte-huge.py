#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt6.QtCore import QFile, QIODevice, QTextStream
	
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.text_edit = QPlainTextEdit()
		self.setCentralWidget(self.text_edit)

		self.load_file("large.ngc")

	def load_file(self, filename):
		file = QFile(filename)
		if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.Text):
			stream = QTextStream(file)
			while not stream.atEnd():
				chunk = stream.read(1024)  # Adjust the chunk size as needed
				self.text_edit.appendPlainText(chunk)
			file.close()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())
