#!/usr/bin/env python3

from PyQt6 import QtWidgets, QtCore

class TabShortcutEater(QtCore.QObject):
	def eventFilter(self, obj, event):
		#print(f'event type {event.type()}')
		if event.type() == QtCore.QEvent.Type.KeyPress:
			print(event.key())
			return True
			# Check for Ctrl+Tab (Qt.Key_Tab with Qt.ControlModifier)
			if event.key() == QtCore.Qt.Key.Key_Tab and \
				event.modifiers() == QtCore.Qt.KeyboardModifier.ControlModifier:
				return True  # Consume the event, preventing QTabWidget from processing it
			elif event.key() == QtCore.Qt.Key.Key_Left:
				print('KeyPress Key_Left')
				return True  # Consume the event, preventing QTabWidget from processing it
			elif event.key() == QtCore.Qt.Key.Key_Right:
				print('KeyPress Key_Right')
				return True  # Consume the event, preventing QTabWidget from processing it
		elif event.type() == QtCore.QEvent.Type.ShortcutOverride:
			if event.key() == QtCore.Qt.Key.Key_Left:
				print('ShortcutOverride Key_Left')
				return True  # Consume the event, preventing QTabWidget from processing it
			elif event.key() == QtCore.Qt.Key.Key_Right:
				print('ShortcutOverride Key_Right')
				return True  # Consume the event, preventing QTabWidget from processing it
		elif event.type() == QtCore.QEvent.Type.LayoutRequest:
			return True
		return super().eventFilter(obj, event)

'''
QEvent::KeyRelease	7
QEvent::ShortcutOverride	51
QEvent::LayoutRequest	76
QEvent::Paint	12
'''


class MyWindow(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QTabWidget Shortcut Disabler")

		self.tab_widget = QtWidgets.QTabWidget()
		self.tab_widget.addTab(QtWidgets.QLabel("Tab 1 Content"), "Tab 1")
		self.tab_widget.addTab(QtWidgets.QLabel("Tab 2 Content"), "Tab 2")
		self.tab_widget.addTab(QtWidgets.QLabel("Tab 3 Content"), "Tab 3")

		# Install the event filter on the QTabWidget
		self.shortcut_eater = TabShortcutEater()
		app.installEventFilter(self.shortcut_eater)

		layout = QtWidgets.QVBoxLayout(self)
		layout.addWidget(self.tab_widget)

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = MyWindow()
	window.show()
	app.exec()
