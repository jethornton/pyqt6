#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
from PyQt6.QtWidgets import QListView

class MainWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.__ui__()
		self.__style__()

	def __ui__(self):
		self.layout = QVBoxLayout()
		self.comboBox = QComboBox()
		self.comboBox.setView(QListView())
		self.comboBox.addItems(["one", "too", "three", "four", "five", "six"])
		self.layout.addWidget(self.comboBox)
		self.setLayout(self.layout)

	def __style__(self):
		self.comboBox.setStyleSheet("QComboBox {min-height:60px;}")
		self.comboBox.setStyleSheet("QListView::item {min-height:60px;}")

if __name__ == "__main__":
	app = QApplication([])
	widget = MainWidget()
	widget.show()
	sys.exit(app.exec())

