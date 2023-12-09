#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QInputDialog, QApplication, QWidget,  QGridLayout
from PyQt6.QtWidgets import QListWidget,  QPushButton
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('List Widget')
		self.setGeometry(100, 100, 400, 100)
		layout = QGridLayout(self)
		self.setLayout(layout)

		self.lw = QListWidget(self)
		self.lw.addItem('List Item #0')
		self.lw.addItems(['List Item #1', 'List Item #2', 'List Item #3'])
		layout.addWidget(self.lw, 0, 0, 4, 1)

		# create buttons
		add_button = QPushButton('Add')
		add_button.clicked.connect(self.add)
		insert_button = QPushButton('Insert')
		insert_button.clicked.connect(self.insert)
		remove_button = QPushButton('Remove')
		remove_button.clicked.connect(self.remove)
		clear_button = QPushButton('Clear')
		clear_button.clicked.connect(self.clear)

		layout.addWidget(add_button, 0, 1)
		layout.addWidget(insert_button, 1, 1)
		layout.addWidget(remove_button, 2, 1)
		layout.addWidget(clear_button, 3, 1)
		self.show()

	def add(self):
		text, ok = QInputDialog.getText(self, 'New Item', 'Add an item to end:')
		if ok and text:
			self.lw.addItem(text)

	def insert(self):
		text, ok = QInputDialog.getText(self, 'Insert Item', 'Insert an item above selection:')
		if ok and text:
			current_row = self.lw.currentRow()
			self.lw.insertItem(current_row, text)

	def remove(self):
		current_row = self.lw.currentRow()
		if current_row >= 0:
			current_item = self.lw.takeItem(current_row)
			del current_item

	def clear(self):
		self.lw.clear()

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
