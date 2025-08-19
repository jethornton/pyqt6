#!/usr/bin/env python3

from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal

class MyObject(QObject):
	my_property_changed = pyqtSignal()

	def __init__(self, parent=None):
		super().__init__(parent)
		self._my_property = 0
		#self.my_property_changed = pyqtSignal()

	def get_my_property(self):
		return self._my_property

	def set_my_property(self, value):
		if self._my_property != value:
			self._my_property = value
			self.my_property_changed.emit()

	my_property = pyqtProperty(int, get_my_property, set_my_property, notify=my_property_changed)

obj = MyObject()
obj.my_property = 7
print(obj.my_property)

