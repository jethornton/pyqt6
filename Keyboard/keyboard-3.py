#!/usr/bin/env python3


import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt5.QtCore import Qt, QEvent, QObject

class MyEventFilter(QObject):
	#def __init__(self, window):
	#	super().__init__()
	#	print('event filter')

	def eventFilter(self, receiver, event):
		if event.type() == QtCore.QEvent.Type.KeyPress:
			print(event.key())
			return True
		return super().eventFilter(obj, event)

		'''
		# in pyqt5 QWindow gets all events before the widgets inside it do
		# we need the widgets inside it to get their events first
		if isinstance(receiver, QtGui.QWindow):
			return super(MyEventFilter, self).eventFilter(receiver, event)
			# Run in try statement so if we want to event to run through normal event routines,
			# we just raise an error and run the super class event handler.
			# This is necessary because if the widget (such as dialogs) are owned by c++ rather then python,
			# it causes an error and the keystrokes don't get to the widgets.
		try:
			if (event.type() == QtCore.QEvent.KeyPress):
				print(f'key pressed {event.name()}')
				handled = False
				if handled: return True

			elif (event.type() == QtCore.QEvent.KeyRelease):
				handled = False
				if handled: return True
			return super(MyEventFilter, self).eventFilter(receiver, event)
		except:
			return super(MyEventFilter, self).eventFilter(receiver, event)
		'''

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'keyboard-3.ui'), self)
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT6 Key Capture!")
		self.show()
		#self.tabWidget.installEventFilter(self)
		#myFilter = MyEventFilter(main)
		self.event_filter = MyEventFilter()
		app.installEventFilter(self.event_filter)
		#self.installEventFilter(myFilter)

	'''
	def keyPressEvent(self, event):
		if not event.isAutoRepeat():
			print(f'{event.key()} pressed')
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
		if not event.isAutoRepeat():
			print(f'{event.key()} released')

	def eventFilter(self, obj, event):
		print(event)

	def jog(self, key, action):
		print(key)
	'''
app = QApplication(sys.argv)
gui = main()
app.exec()
