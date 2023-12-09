#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout
from PyQt6.QtGui import QTextCursor, QTextBlockFormat, QColor
from PyQt6.QtCore import QEvent, Qt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.view = QPlainTextEdit()
		self.view.viewport().installEventFilter(self)

		for i in range(25): # add some text to the text edit
			self.view.appendPlainText(f'Line: {i}')

		# move cursor to start of document
		self.cursor = self.view.textCursor()
		self.cursor.movePosition(QTextCursor.MoveOperation.Start)
		self.view.setTextCursor(self.cursor)

		self.lbl = QLabel('Click on a line.')
		layout = QVBoxLayout(central_widget)
		layout.addWidget(self.lbl)
		layout.addWidget(self.view)
		self.show()

	def show_line(self):
		# get a copy of the QTextCursor that represents the currently visible cursor
		cursor = self.view.textCursor()
		selected_block = cursor.blockNumber() # get current block number
		self.lbl.setText(f'Current line number: {selected_block}')
		format_normal = QTextBlockFormat()
		format_normal.setBackground(QColor('white'))
		highlight_format = QTextBlockFormat()
		highlight_format.setBackground(QColor('yellow'))
		cursor.select(QTextCursor.SelectionType.Document)
		cursor.setBlockFormat(format_normal) # clear the format
		# I'm not sure what's going on on the next line but it seems that is could be simpler
		#cursor.select(QTextCursor.SelectionType.Document.findBlockByNumber(selected_block))
		cursor = QTextCursor(self.view.document().findBlockByNumber(selected_block))
		cursor.movePosition(QTextCursor.MoveOperation.StartOfBlock, QTextCursor.MoveMode.MoveAnchor)
		cursor.setBlockFormat(highlight_format)
		self.view.setTextCursor(cursor)

	def eventFilter(self, obj, event):
		if obj is self.view.viewport() and event.type() == QEvent.Type.MouseButtonRelease:
			if event.button() == Qt.MouseButton.LeftButton:
				self.show_line()
		return super(MainWindow, self).eventFilter(obj, event)

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

