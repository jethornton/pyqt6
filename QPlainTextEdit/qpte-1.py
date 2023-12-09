#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.view = QPlainTextEdit()
		self.view.setCenterOnScroll(True)
		layout = QVBoxLayout(central_widget)
		layout.addWidget(self.view)
		self.view.blockCountChanged.connect(self.test)
		self.show()

	def test(self):
		print(f'{self.view.blockCount()}')

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

