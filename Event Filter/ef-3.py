#!/usr/bin/env python3

import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QObject, QEvent, Qt
from PyQt6 import uic

class MyEventFilter(QObject):
	def eventFilter(self, obj, event):
		#print(event.type())
		if event.type() == QEvent.Type.KeyPress:
			print(f'Other key pressed {event.key()}')
			return True  # Event handled, stop propagation
		elif event.type() == QEvent.Type.ShortcutOverride:
			print(f'Shortcut key pressed {event.key()}')
			return False  # Event handled, stop propagation

		return super().eventFilter(obj, event)

		'''
		if obj == self.parent() and event.type() == QEvent.Type.KeyPress:
			print(f"Key pressed on QMainWindow: {event.key()}")
			return True  # Event handled, stop propagation
		elif event.type() == QEvent.Type.KeyPress:
			print(f'Other key pressed {event.key()}')
			return True  # Event handled, stop propagation
		'''

class MyMainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'keyboard-3.ui'), self)
		self.setWindowTitle("QMainWindow with Event Filter")
		self.setGeometry(100, 100, 400, 300)

		#self.label = QLabel("Press a key in this window", self)
		#self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		#self.setCentralWidget(self.label)

		# Install the event filter on this QMainWindow instance
		self.event_filter = MyEventFilter(self) # Pass self as parent to the event filter
		self.installEventFilter(self.event_filter)

if __name__ == "__main__":
	app = QApplication([])
	window = MyMainWindow()
	window.show()
	app.exec()
