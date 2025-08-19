#!/usr/bin/env python3


import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QEvent

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		QApplication.instance().installEventFilter(self)

		self.setWindowTitle("My App")

		button = QPushButton("Press me!")
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)
		self.show()

	def button_clicked(self, s):
		print("click", s)

	def eventFilter(self, source, event):
		if event.type() == QEvent.Type.KeyPress:
			if not event.isAutoRepeat():
				print(f'KeyPress: {event.key()} {source}')
		if event.type() == QEvent.Type.KeyRelease:
			if not event.isAutoRepeat():
				print(f'KeyRelease: {event.key()} {source}')
		return super().eventFilter(source, event)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
