#!/usr/bin/env python3

import sys
from PyQt5 import QtCore, QtWidgets
	
class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Main Window')
		self.setGeometry(400, 100, 300, 200)
		self._help_dialog = None
		self._other_dialog = None
		self.buttonHelp = QtWidgets.QPushButton('Open Help')
		self.buttonHelp.clicked.connect(self.handleOpenHelp)
		self.buttonDialog = QtWidgets.QPushButton('Open Dialog')
		self.buttonDialog.clicked.connect(self.handleOpenDialog)
		layout = QtWidgets.QHBoxLayout(self)
		layout.addWidget(self.buttonDialog)
		layout.addWidget(self.buttonHelp)
		#self.handleOpenHelp()

	def handleOpenDialog(self):
		if self._other_dialog is None:
			self._other_dialog = QtWidgets.QDialog(self)
			self._other_dialog.setWindowModality(QtCore.Qt.WindowModal)
			self._other_dialog.setWindowTitle('Other Dialog')
			self._other_dialog.resize(200, 100)
		self._other_dialog.exec_()

	def handleOpenHelp(self):
		if self._help_dialog is None:
			self._help_dialog = QtWidgets.QDialog()
			self._help_dialog.setWindowTitle('Help Dialog')
			self._help_dialog.setGeometry(750, 100, 250, 250)
		self._help_dialog.show()

	def closeEvent(self, event):
		if self._help_dialog is not None:
			self._help_dialog.close()

if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())



