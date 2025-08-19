#!/usr/bin/env python3

from PyQt6.QtCore import pyqtProperty, pyqtSignal, QObject


class CustomObject(QObject):
	valueChanged = pyqtSignal(int)

	def __init__(self):
		super().__init__()
		self._value = 0		# the default value

	def getValue(self):
		return self._value

	@value.setter
	def value(self, value):
		# here, the check is very important..
		# to prevent unneeded signal being propagated.
		if value != self._value:
			self._value = value
			self.valueChanged.emit(value)

	value = pyqtProperty(int, getValue, setValue)

obj = CustomObject()
obj.value = 7
print(obj.value)

