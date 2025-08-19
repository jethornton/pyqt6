#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QPlainTextEdit, QPushButton, QLineEdit
from PyQt6.QtGui import QTextDocument, QTextCursor, QColor, QTextBlockFormat, QBrush

class SearchText(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.text_edit = QPlainTextEdit()
		self.search_input = QLineEdit()
		self.search_button = QPushButton("Search")
		self.search_button.clicked.connect(self.search_text)
		
		layout = QVBoxLayout()
		layout.addWidget(self.text_edit)
		layout.addWidget(self.search_input)
		layout.addWidget(self.search_button)
		self.setLayout(layout)

	def search_text(self):
		search_string = self.search_input.text()
		print(search_string)
		if not search_string:
			return

		document = self.text_edit.document()
		cursor = QTextCursor(document)

		# Clear previous highlights
		format = QTextBlockFormat()
		format.clearBackground()
		cursor.select(QTextCursor.SelectionType.Document)
		cursor.mergeBlockFormat(format)

		# Find and highlight occurrences
		while True:
			cursor = document.find(search_string, cursor)
			if cursor.isNull():
				break
			
			format = QTextBlockFormat()
			format.setBackground(QBrush(QColor("yellow")))
			cursor.mergeBlockFormat(format)

			# Move cursor to the end of the highlighted text, 
			# otherwise it will highlight the same text over and over
			cursor.setPosition(cursor.position() + len(search_string))

if __name__ == '__main__':
	app = QApplication([])
	window = SearchText()
	window.show()
	app.exec()
