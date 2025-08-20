#!/usr/bin/env python3

import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import Qt, QEvent

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'ef.ui'), self)
		QApplication.instance().installEventFilter(self)
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT6 Event Filter!")
		self.show()

	def eventFilter(self, source, event):
		if event.type() == QEvent.Type.KeyPress:
			if not event.isAutoRepeat():
				if event.key() == Qt.Key.Key_Right:
					print('Right Arrow Pressed')
					self.key_lb.setText(f'Right Arrow Pressed {event.key()}')
					return True
				elif event.key() == Qt.Key.Key_Left:
					print('Left Arrow Pressed')
					self.key_lb.setText(f'Left Arrow Pressed {event.key()}')
					return True
				else:
					print(f'KeyPress: {event.key()} {source}')
			elif event.key() == Qt.Key.Key_Right:
				return True
		if event.type() == QEvent.Type.KeyRelease:
			if not event.isAutoRepeat():
				if event.key() == Qt.Key.Key_Right:
					print('Right Arrow Released')
					self.key_lb.setText(f'Right Arrow Released {event.key()}')
					return True
				elif event.key() == Qt.Key.Key_Left:
					print('Left Arrow Released')
					self.key_lb.setText(f'Left Arrow Released {event.key()}')
					return True
				else:
					print(f'KeyRelease: {event.key()} {source}')
		return super().eventFilter(source, event)


app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())
