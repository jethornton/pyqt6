#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPlainTextEdit
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt

class KeyboardEventApp(QMainWindow):
	def __init__(self):
		super().__init__()

		#QApplication.instance().installEventFilter(self)

		self.setWindowTitle("Keyboard Jog Example")
		self.setGeometry(100, 200, 400, 200)

		self.central_widget = QWidget(self)
		self.setCentralWidget(self.central_widget)
		self.central_widget.installEventFilter(self)

		self.key_label = QLabel("Last Key Pressed: None", self.central_widget)
		self.key_label.setGeometry(10, 10, 390, 30)
		self.action_label = QLabel("Action: None", self.central_widget)
		self.action_label.setGeometry(10, 50, 390, 30)
		self.pte = QPlainTextEdit('', self.central_widget)
		self.pte.setGeometry(10, 85, 380, 100)


	def eventFilter(self, source, event):
		if isinstance(event, QKeyEvent):
				match event.key():
					case Qt.Key.Key_Right:
						self.key_label.setText('Key Pressed: Key_Right')
					case _:
						return super().eventFilter(source, event)


	'''
	def keyPressEvent(self, event):
		if isinstance(event, QKeyEvent):
			if not event.isAutoRepeat():
				match event.key():
					case Qt.Key.Key_Right:
						self.key_label.setText('Key Pressed: Key_Right')
						self.jog(event.key(), True)
					case Qt.Key.Key_Left:
						self.key_label.setText('Key Pressed: Key_Left')
						self.jog(event.key(), True)
					case Qt.Key.Key_Up:
						self.key_label.setText('Key Pressed: Key_Up')
						self.jog(event.key(), True)
					case Qt.Key.Key_Down:
						self.key_label.setText('Key Pressed: Key_Down')
						self.jog(event.key(), True)
					case Qt.Key.Key_PageUp:
						self.key_label.setText('Key Pressed: Key_PageUp')
						self.jog(event.key(), True)
					case Qt.Key.Key_PageDown:
						self.key_label.setText('Key Pressed: Key_PageDown')
						self.jog(event.key(), True)
					case _:
						if len(event.text()) > 0:
							self.key_label.setText(f'Key Pressed: {event.text()} is not a Jog Key')
						else:
							self.key_label.setText(f'Key Pressed: {event.key()} is not a Jog Key')

	def keyReleaseEvent(self, event):
		if isinstance(event, QKeyEvent):
			if not event.isAutoRepeat():
				self.key_label.setText('Key Released')
				self.jog(event.key(), False)

	def jog(self, key, action):
		if action:
			match key:
				case Qt.Key.Key_Right:
					self.action_label.setText('Action: Jogging X+')
				case Qt.Key.Key_Left:
					self.action_label.setText('Action: Jogging X-')
				case Qt.Key.Key_Up:
					self.action_label.setText('Action: Jogging Y+')
				case Qt.Key.Key_Down:
					self.action_label.setText('Action: Jogging Y-')
				case Qt.Key.Key_PageUp:
					self.action_label.setText('Action: Jogging Z+')
				case Qt.Key.Key_PageDown:
					self.action_label.setText('Action: Jogging Z-')

				case _:
					self.key_label.setText('Key Pressed: Not a Jog Key')
		else:
			self.action_label.setText('Action: Stopped')
	'''

def main():
	app = QApplication(sys.argv)
	window = KeyboardEventApp()
	window.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()
