#!/usr/bin/env python3

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QRadialGradient, QPainter, QColor, QBrush, QPainter
from PyQt5.QtCore import Qt, pyqtProperty, QPointF
import sys


class MyQPushButton(QPushButton):
	_led = False

	def paintEvent(self, event):
		super().paintEvent(event)
		painter = QPainter(self)
		size = self.rect()
		#print(size.topRight())
		diameter = 20
		x_offset = 5
		x_center = size.width() - ((diameter / 2) + x_offset)
		#print(size.width())
		#print(x_center)
		y_offset = 5
		y_center = (diameter / 2) + y_offset
		self._right_edge_offset = 5
		self._top_edge_offset = 5
		on_color = QColor(0, 255, 0, 255)
		off_color = QColor(125, 0, 0, 255)
		x = int(size.width() - diameter - self._right_edge_offset)
		y = int(0 + self._top_edge_offset)
		gradient = QRadialGradient(x + diameter / 2, y + diameter / 2,
			diameter * 0.4, diameter * 0.4, diameter * 0.4)
		gradient.setColorAt(0, Qt.GlobalColor.white)
		painter.setRenderHint(QPainter.Antialiasing, True)

		if self._led:
			gradient.setColorAt(1, on_color)
			painter.setBrush(QBrush(gradient))
			painter.setPen(on_color)
			# Draws the ellipse positioned at center with radii rx and ry.
			painter.drawEllipse(QPointF(x_center, y_center), diameter / 2, diameter / 2)
			#painter.drawEllipse(x, y, diameter - 1, diameter - 1)
			#painter.fillRect(size.width() - 20, size.height() - 20, 10, 10, QColor(80, 255, 80, 255))
		else:
			gradient.setColorAt(1, off_color)
			painter.setBrush(QBrush(gradient))
			painter.setPen(off_color)
			painter.drawEllipse(QPointF(x_center, y_center), diameter / 2, diameter / 2)
			#painter.drawEllipse(x, y, diameter - 1, diameter - 1)
			#painter.fillRect(size.width() - 20, size.height() - 20, 10, 10, QColor(255, 80, 80, 255))

	def setLed(self, val):
		self._led = val
		#print("Led is set to", val)
		self.update()

	def getLed(self):
		#print("read Led = ", self._led)
		self.update()
		return self._led

	led = pyqtProperty(bool, getLed, setLed)

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('LED Button')
		self.setGeometry(100, 100, 400, 400)
		self.UiComponents()
		self.show()
 
	def UiComponents(self):
		self.button = MyQPushButton("OFF", self)
		self.button.setGeometry(150, 150, 100, 50)
		self.button.clicked.connect(self.clickme)
 
	def clickme(self):
		self.button.led = not self.button.led
		if self.button.led:
			self.button.setText('ON')
		else:
			self.button.setText('OFF')
		#print(self.button.led)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())



