#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt6.QtCore import QEvent, Qt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.qpte = QPlainTextEdit("Click in this window")
		self.qpte.viewport().installEventFilter(self)
		self.setCentralWidget(self.qpte)

	def eventFilter(self, obj, event):
		if obj is self.qpte.viewport() and event.type() == QEvent.Type.MouseButtonPress:
			if event.button() == Qt.MouseButton.LeftButton:
				print('test')
		return super(MainWindow, self).eventFilter(obj, event)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

