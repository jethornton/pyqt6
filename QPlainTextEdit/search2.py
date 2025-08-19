#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QPlainTextEdit, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout, QLineEdit
from PyQt6.QtWidgets import QDialog, QLabel, QCheckBox, QWidget
from PyQt6.QtGui import QTextDocument, QTextCursor, QPalette, QColor
import sys

class FindDialog(QDialog):
	def __init__(self, parent):
		super().__init__(parent)
		self.setWindowTitle("Find")
		layout = QGridLayout(self)
		label = QLabel("Find Text:")
		layout.addWidget(label, 0, 0)
		self.lineEdit = QLineEdit('bla')
		layout.addWidget(self.lineEdit, 0, 1)
		self.caseSensitive = QCheckBox('Case Sensitive')
		layout.addWidget(self.caseSensitive, 1 ,0)
		self.wholeWord = QCheckBox('Whole Word')
		layout.addWidget(self.wholeWord, 1 ,1)
		self.cancelButton = QPushButton("Cancle")
		layout.addWidget(self.cancelButton, 2, 0)
		self.findForward = QPushButton("Find Forward")
		self.findForward.setObjectName('forward_search')
		layout.addWidget(self.findForward, 3, 1)
		self.findBackward = QPushButton("Find Backward")
		self.findBackward.setObjectName('backward_search')
		layout.addWidget(self.findBackward, 3, 0)

		self.findForward.clicked.connect(self.find_text)
		self.findBackward.clicked.connect(self.find_text)
		self.cancelButton.clicked.connect(self.close) 
		self.text_edit = parent 

	def find_text(self):
		senderName = self.sender().objectName()
		flags = False
		flagList = []
		if senderName == 'backward_search':
			flagList.append('bs')
			flags = QTextDocument.FindFlag.FindBackward
		if self.caseSensitive.isChecked():
			flagList.append('cs')
			flags = QTextDocument.FindFlag.FindCaseSensitively
		if self.wholeWord.isChecked():
			flagList.append('ww')
			flags = QTextDocument.FindFlag.FindWholeWords
		if flagList == ['bs', 'cs', 'ww']:
			flags = QTextDocument.FindFlag.FindWholeWords | \
			QTextDocument.FindFlag.FindCaseSensitively | \
			QTextDocument.FindFlag.FindBackward
		elif flagList == ['bs', 'cs']:
			flags = QTextDocument.FindFlag.FindCaseSensitively | \
			QTextDocument.FindFlag.FindBackward
		elif flagList == ['bs', 'ww']:
			flags = QTextDocument.FindFlag.FindWholeWords | \
			QTextDocument.FindFlag.FindBackward
		elif flagList == ['cs', 'ww']:
			flags = QTextDocument.FindFlag.FindWholeWords | \
			QTextDocument.FindFlag.FindCaseSensitively
		print(flags)

		text_to_find = self.lineEdit.text()
		if text_to_find:
			if flags:
				if self.text_edit.find(text_to_find, flags):
					return
				else:
					self.lineEdit.clear()
					self.lineEdit.setPlaceholderText("Not found.")
			else:
				if self.text_edit.find(text_to_find):
					return
				else:
					self.lineEdit.clear()
					self.lineEdit.setPlaceholderText("Not found.")

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.text_edit = QPlainTextEdit()
		self.text_edit.setPlainText('This is a test of bla\n and bla\n'
		'this is a test of black\nand Bla and bla')
		self.find_button = QPushButton("Find")
		self.find_button.clicked.connect(self.open_find_dialog)
		layout = QVBoxLayout(self)
		layout.addWidget(self.text_edit)
		layout.addWidget(self.find_button)
		self.find_dialog = None

	def open_find_dialog(self):
		self.find_dialog = FindDialog(self.text_edit)
		self.find_dialog.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec())
