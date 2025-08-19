#!/usr/bin/env python3

from PyQt6.QtWidgets import QFileDialog

class CustomFileDialog(QFileDialog):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# Customize the file dialog here
		self.setWindowTitle("My Custom File Dialog")
		self.setNameFilter("Text Files (*.txt);;All Files (*)")
		self.setGeometry(100, 100, 500, 500)

	# Optionally override other methods for more customization
	# def accept(self):
	#	 # Do something before accepting the dialog
	#	 super().accept()

if __name__ == "__main__":
	import sys
	from PyQt6.QtWidgets import QApplication

	app = QApplication(sys.argv)

	dialog = CustomFileDialog()
	if dialog.exec():
		print("Selected file:", dialog.selectedFiles())
	else:
		print('Cancled')
