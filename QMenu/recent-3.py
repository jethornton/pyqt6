#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Recent Files')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.view = QPlainTextEdit()
		layout = QVBoxLayout(central_widget)
		layout.addWidget(self.view)

		file_menu = self.menuBar().addMenu('&File')
		self.recent_menu = file_menu.addMenu('&Recent')
		quitAction = file_menu.addAction('Quit')
		quitAction.triggered.connect(self.close)


		self.show()


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

