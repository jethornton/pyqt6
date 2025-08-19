#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(300, 300, 800, 800)
		self.setWindowTitle("File Dialog Example")
		self.show()
		self.open_file_dialog()

	def open_file_dialog(self):
		dialog = QFileDialog(self)
		#dialog.setGeometry(100, 100, 600, 400)  # Set the position and size of the dialog
		dialog.setWindowTitle("Select a File")
		'''
		QFileDialog.FileMode.AnyFile: The user can select any file, including
		non-existent files. This is useful for "Save As" dialogs.
		QFileDialog.FileMode.ExistingFile: The user can only select existing files.
		QFileDialog.FileMode.Directory: The user can only select a directory.
		QFileDialog.FileMode.ExistingFiles: The user can select multiple existing files.
		QFileDialog.FileMode.DirectoryOnly: The user can only select a directory,
		and no files will be displayed.
		'''


		dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
		if dialog.exec():
			filename = dialog.selectedFiles()[0]
			print("Selected file:", filename)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())
