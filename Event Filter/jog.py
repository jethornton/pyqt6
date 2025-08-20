#!/usr/bin/env python3

import sys, os

from PyQt6.QtCore import QObject, QEvent, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class KeyboardJog(QObject):
	def __init__(self, window):
		super().__init__()
	def eventFilter(self, obj, event):
		#print(event.type())
		# only handle the keys if keyboard jog is checked
		if window.keyboard_jog_cb.isChecked():
			if event.type() == QEvent.Type.KeyPress:
				if not event.isAutoRepeat():
					print(f'KeyPress {event.key()}')
					if event.key() == Qt.Key.Key_Up:
						window.key_lb.setText('KeyPress Key_Up')
						return True  # Consume the event
					elif event.key() == Qt.Key.Key_Down:
						window.key_lb.setText('KeyPress Key_Down')
						return True  # Consume the event
					elif event.key() == Qt.Key.Key_PageUp:
						window.key_lb.setText('KeyPress Key_PageUp')
						return True  # Consume the event
					elif event.key() == Qt.Key.Key_PageDown:
						window.key_lb.setText('KeyPress Key_PageDown')
						return True  # Consume the event
					elif event.key() == Qt.Key.Key_Left:
						window.key_lb.setText('ShortcutOverride Key_Left')
						return True  # Consume the event, preventing QTabWidget from processing it
					elif event.key() == Qt.Key.Key_Right:
						window.key_lb.setText('ShortcutOverride Key_Right')
						return True  # Consume the event, preventing QTabWidget from processing it
				elif event.isAutoRepeat():
					return True
			elif event.type() == QEvent.Type.ShortcutOverride:
				if not event.isAutoRepeat():
					print(f'ShortcutOverride {event.key()}')
					if event.key() == Qt.Key.Key_Up:
						window.key_lb.setText('KeyPress Key_Up')
						return True  # Consume the event
					elif event.key() == Qt.Key.Key_Down:
						window.key_lb.setText('KeyPress Key_Down')
						return True  # Consume the event
					elif event.key() == Qt.Key.Key_PageUp:
						window.key_lb.setText('KeyPress Key_PageUp')
						return True  # Consume the event
					elif event.key() == Qt.Key.Key_PageDown:
						window.key_lb.setText('KeyPress Key_PageDown')
						return True  # Consume the event
					if event.key() == Qt.Key.Key_Left:
						window.key_lb.setText('ShortcutOverride Key_Left')
						return True  # Consume the event, preventing QTabWidget from processing it
					elif event.key() == Qt.Key.Key_Right:
						window.key_lb.setText('ShortcutOverride Key_Right')
						return True  # Consume the event, preventing QTabWidget from processing it
				elif event.isAutoRepeat():
					return True
			elif event.type() == QEvent.Type.KeyRelease:
				if not event.isAutoRepeat():
					window.key_lb.setText('KeyRelease')
					return True  # Consume the event, preventing QTabWidget from processing it

		return super().eventFilter(obj, event)

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'jog.ui'), self)
		self.setGeometry(50, 50, 300, 300)
		self.setWindowTitle("PyQT6 Load UI File!")
		self.show()

		self.keyboard_jog = KeyboardJog(self)
		app.installEventFilter(self.keyboard_jog)

		app.aboutToQuit.connect(self.cleanup)

	def cleanup(self):
		app.removeEventFilter(self.keyboard_jog)

app = QApplication(sys.argv)
window = main()
app.exec()
