#!/usr/bin/env python3

from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal

class MyObject(QObject):
	nameChanged = pyqtSignal()

	def __init__(self, name="default"):
		super().__init__()
		self._name = name

	def _get_name(self):
		return self._name

	def _set_name(self, value):
		if self._name != value:
			self._name = value
			self.nameChanged.emit()

	name = pyqtProperty(str, _get_name, _set_name, notify=nameChanged)

	# Example with read-only property:
	@pyqtProperty(str)
	def read_only_name(self):
		return "Read-Only: " + self._name

if __name__ == '__main__':
	obj = MyObject("Initial Name")

	# Accessing and modifying the property
	print("Name:", obj.name)
	obj.name = "New Name"
	print("Name:", obj.name)

	# Accessing read-only property
	print("Read Only Name:", obj.read_only_name)
