#!/usr/bin/env python3

import sys, os

from PyQt5.QtCore import Qt, pyqtProperty, QPointF, QEvent
from PyQt5.QtGui import QRadialGradient, QPainter, QColor, QBrush, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6 import uic

class MyQPushButton(QPushButton):
	_led = False

	def paintEvent(self, event):
		print(event)
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


class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'indicator.ui'), self)
		self.setGeometry(50, 50, 300, 300)
		self.setWindowTitle("PyQT6 Indicator Buttons!")

		self.estop_pb.toggled.connect(self.indicator)
		self.power_pb.toggled.connect(self.indicator)
		self.quit_pb.released.connect(self.close)
		for child in self.findChildren(QPushButton):
			if child.property('indicator'):
				print(child)
				layout = child.parent().layout()
				index = layout.indexOf(child)
				#Remove the old button
				#layout.removeWidget(child)
				#child.deleteLater()
				#child = None
				child = MyQPushButton('OFF')
				#if index != -1:
				#	row, column, rowspan, columnspan = layout.getItemPosition(index)
				#	layout.addWidget(MyQPushButton('Test', self), row, column, rowspan, columnspan)
				#layout.addWidget(MyQPushButton(), row, column, rowspan, columnspan)


				#layout.addWidget(index, replacement)

				#child = MyQPushButton()
				#child.installEventFilter(self)
				#print(child.parent())
				#print(layout)
				#print(layout.count())
				#print(index)
				#	print(row, column, rowspan, columnspan)
				#layout.addWidget(MyQPushButton('OFF'), row, column, rowspan, columnspan)
				#layout.replaceWidget(child, replacement)
				#print(child.parent().layout().getItemPosition())
				#replacement = MyQPushButton("OFF", self)

				#child = replacement
				#child.parent().layout().replaceWidget(child, replacement)
				#layout.replaceWidget(original_button, custom_button)

		with open('style.qss','r') as fh:
			self.setStyleSheet(fh.read())
		self.show()

	def indicator(self):
		btn = self.sender()
		print(f'{btn.objectName()} {btn.isChecked()}')
		btn.update()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())
