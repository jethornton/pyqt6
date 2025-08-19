#!/usr/bin/env python3

from PyQt6.QtCore import QObject, QEvent, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QLineEdit
from PyQt6.QtWidgets import QTabWidget, QLabel, QVBoxLayout

class TabShortcutEater(QObject):
	def __init__(self, window):
			super().__init__()
	def eventFilter(self, obj, event):
		#print(f'event type {event.type()}')
		if event.type() == QEvent.Type.KeyPress:
			# Check for Ctrl+Tab (Qt.Key_Tab with Qt.ControlModifier)
			if event.key() == Qt.Key.Key_Tab and \
				event.modifiers() == Qt.KeyboardModifier.ControlModifier:
				return True  # Consume the event, preventing QTabWidget from processing it
			elif event.key() == Qt.Key.Key_Up:
				window.label.setText('KeyPress Key_Up')
				return True  # Consume the event
			elif event.key() == Qt.Key.Key_Down:
				window.label.setText('KeyPress Key_Down')
				return True  # Consume the event
			elif event.key() == Qt.Key.Key_PageUp:
				window.label.setText('KeyPress Key_PageUp')
				return True  # Consume the event
			elif event.key() == Qt.Key.Key_PageDown:
				window.label.setText('KeyPress Key_PageDown')
				return True  # Consume the event
		elif event.type() == QEvent.Type.ShortcutOverride:
			if event.key() == Qt.Key.Key_Left:
				window.label.setText('ShortcutOverride Key_Left')
				return True  # Consume the event, preventing QTabWidget from processing it
			elif event.key() == Qt.Key.Key_Right:
				window.label.setText('ShortcutOverride Key_Right')
				return True  # Consume the event, preventing QTabWidget from processing it
		return super().eventFilter(obj, event)

'''
QEvent::KeyRelease	7
QEvent::ShortcutOverride	51
QEvent::LayoutRequest	76
QEvent::Paint	12
'''


#class MyWindow(QWidget):

class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(100, 100, 400, 200)
		self.setWindowTitle("QTabWidget Shortcut Disabler")
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		layout = QVBoxLayout(central_widget)

		self.line = QLineEdit()
		self.label = QLabel('No Key Pressed')

		self.tab_widget = QTabWidget()
		self.tab_widget.addTab(QLabel("Tab 1 Content"), "Tab 1")
		self.tab_widget.addTab(QLabel("Tab 2 Content"), "Tab 2")
		self.tab_widget.addTab(QLabel("Tab 3 Content"), "Tab 3")

		# Install the event filter on the QTabWidget
		self.shortcut_eater = TabShortcutEater(self)
		app.installEventFilter(self.shortcut_eater)

		#layout = QVBoxLayout(self)
		layout.addWidget(self.label)
		layout.addWidget(self.line)
		layout.addWidget(self.tab_widget)


		self.show()


app = QApplication([])
window = MyWindow()
#window.show()
app.exec()
