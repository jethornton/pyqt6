#!/usr/bin/env python3

import re

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QPlainTextEdit, QPushButton, QLineEdit, QLabel
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtGui import QTextDocument, QTextCursor
	
class FindReplaceWidget(QWidget):
	def __init__(self):
		super().__init__()

		self.text_edit = QPlainTextEdit()
		self.text_edit.setPlainText('This code provides a basic find and replace\n'
		'functionality, including "Find," "Replace," and "Replace All" options,\n'
		'along with a status label to display messages.')
		self.find_input = QLineEdit('Replace')
		self.replace_input = QLineEdit('destroy')
		self.find_button = QPushButton("Find")
		self.replace_button = QPushButton("Replace")
		self.replace_button.setEnabled(False)
		self.replace_all_button = QPushButton("Replace All")
		self.status_label = QLabel("")

		# Input Layout
		input_layout = QHBoxLayout()
		input_layout.addWidget(QLabel("Find:"))
		input_layout.addWidget(self.find_input)
		input_layout.addWidget(QLabel("Replace:"))
		input_layout.addWidget(self.replace_input)

		# Option Layout
		option_layout  = QHBoxLayout()
		option_layout.addWidget(QCheckBox("Match Case"))
		option_layout.addWidget(QCheckBox("Whole Word"))
		option_layout.addWidget(QCheckBox("Search Backwards"))

		# Button Layout
		button_layout = QHBoxLayout()
		button_layout.addWidget(self.find_button)
		button_layout.addWidget(self.replace_button)
		button_layout.addWidget(self.replace_all_button)

		# Main Layout
		main_layout = QVBoxLayout()
		main_layout.addWidget(self.text_edit)
		main_layout.addLayout(input_layout)
		main_layout.addLayout(option_layout)
		main_layout.addLayout(button_layout)
		main_layout.addWidget(self.status_label)
		self.setLayout(main_layout)

		# Connections
		self.find_button.clicked.connect(self.find_text)
		self.replace_button.clicked.connect(self.replace_text)
		self.replace_all_button.clicked.connect(self.replace_all_text)


	def find_text(self):
		text_to_find = self.find_input.text()
		if not text_to_find:
			return

		#cursor = self.text_edit.textCursor()

		if self.text_edit.find(text_to_find):
			self.status_label.setText("Text found.")
			self.replace_button.setEnabled(True)
		else:
			self.status_label.setText("Text not found.")
			self.replace_button.setEnabled(False)
			self.text_edit.moveCursor(QTextCursor.MoveOperation.Start) #reset cursor to start if not found

	def replace_text(self):
		text_to_find = self.find_input.text()
		replace_with = self.replace_input.text()

		if not text_to_find:
			return

		cursor = self.text_edit.textCursor()

		if self.text_edit.find(text_to_find):
			cursor.insertText(replace_with)
			self.status_label.setText("Text replaced.")
		else:
			self.status_label.setText("Text not found.")
			self.replace_button.setEnabled(False)
			self.text_edit.moveCursor(QTextCursor.MoveOperation.Start) #reset cursor to start if not found

	def replace_all_text(self):
		text_to_find = self.find_input.text()
		replace_with = self.replace_input.text()
		if not text_to_find:
			return

		text = self.text_edit.toPlainText()
		new_text = re.sub(text_to_find, replace_with, text, flags=re.IGNORECASE)
		#new_text = text.replace(text_to_find, replace_with)
		self.text_edit.setPlainText(new_text)
		self.status_label.setText("All occurrences replaced.")
		self.replace_button.setEnabled(False)


if __name__ == '__main__':
	app = QApplication([])
	widget = FindReplaceWidget()
	widget.show()
	app.exec()
