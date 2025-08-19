#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit
from PyQt6.QtGui import QTextCursor
import sys

class FindReplaceWidget(QWidget):
	def __init__(self):
		super().__init__()

		self.text_edit = QPlainTextEdit()
		self.text_edit.setPlainText("Short of profiling you're going to have\n"
		'trouble finding exactly what the slow down is, but its probably to do\n'
		'with a few factors: PyQT is really tied to its C libraries, handling\n'
		'data between the two might cause slow downs.')
		self.find_input = QLineEdit('to')
		self.replace_input = QLineEdit('yo')
		self.find_button = QPushButton("Find")
		self.replace_button = QPushButton("Replace")
		self.replace_all_button = QPushButton("Replace All")

		self.find_button.clicked.connect(self.find_text)
		self.replace_button.clicked.connect(self.replace_text)
		self.replace_all_button.clicked.connect(self.replace_all_text)

		input_layout = QHBoxLayout()
		input_layout.addWidget(self.find_input)
		input_layout.addWidget(self.replace_input)

		button_layout = QHBoxLayout()
		button_layout.addWidget(self.find_button)
		button_layout.addWidget(self.replace_button)
		button_layout.addWidget(self.replace_all_button)

		main_layout = QVBoxLayout()
		main_layout.addWidget(self.text_edit)
		main_layout.addLayout(input_layout)
		main_layout.addLayout(button_layout)

		self.setLayout(main_layout)

	def find_text(self):
		text_to_find = self.find_input.text()
		if text_to_find:
			found = self.text_edit.find(text_to_find)
			if not found:
				cursor = self.text_edit.textCursor()
				cursor.setPosition(0)
				self.text_edit.setTextCursor(cursor)
				self.text_edit.find(text_to_find)

	def replace_text(self):
		text_to_find = self.find_input.text()
		replacement_text = self.replace_input.text()

		if text_to_find and self.text_edit.find(text_to_find):
			cursor = self.text_edit.textCursor()
			cursor.removeSelectedText()
			cursor.insertText(replacement_text)

	def replace_all_text(self):
		text_to_find = self.find_input.text()
		replacement_text = self.replace_input.text()

		if text_to_find:
			while self.text_edit.find(text_to_find):
				cursor = self.text_edit.textCursor()
				cursor.removeSelectedText()
				cursor.insertText(replacement_text)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = FindReplaceWidget()
	widget.show()
	sys.exit(app.exec())
