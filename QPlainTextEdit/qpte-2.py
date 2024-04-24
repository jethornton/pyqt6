#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt6.QtCore import QEvent

class Edit(QPlainTextEdit):
	def mouseMoveEvent(self, e):
		print("mouseMoveEvent")
		super().mouseMoveEvent(e)

	def mousePressEvent(self, e):
		print("mousePressEvent")
		super().mousePressEvent(e)

	def mouseReleaseEvent(self, e):
		print("mouseReleaseEvent")
		super().mouseReleaseEvent(e)

	def mouseDoubleClickEvent(self, e):
		print("mouseDoubleClickEvent")
		super().mouseDoubleClickEvent(e)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.qpte = Edit("Click in this window")
		# Mouse move events will only be catched when the mouse is pressed
		# unless setMouseTracking is set to True
		# self.qpte.setMouseTracking(True)
		self.qpte.viewport().installEventFilter(self)
		self.setCentralWidget(self.qpte)

	def eventFilter(self, obj, event):
		if obj == self.qpte.viewport():
			if event.type() == QEvent.Type.FocusIn:
				print(event)
			if event.type() == QEvent.Type.MouseButtonPress:
				print('press')
			elif event.type() == QEvent.Type.MouseMove:
				print('move')
			elif event.type() == QEvent.Type.MouseButtonRelease:
				print('release')
			return super().eventFilter(obj, event)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

