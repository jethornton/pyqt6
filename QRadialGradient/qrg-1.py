#!/usr/bin/env python3

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import QPointF
class Example(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(100, 100, 300, 200)

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		
		# Define the gradient
		center = QPointF(150, 100)
		radius = 80
		focal_point = QPointF(100, 50)
		gradient = QtGui.QRadialGradient(center, radius, focal_point)
		gradient.setColorAt(0, QtGui.QColor(255, 255, 255))  # White at the center
		gradient.setColorAt(1, QtGui.QColor(0, 0, 255))	  # Blue at the edge

		# Create a brush with the gradient
		brush = QtGui.QBrush(gradient)

		# Draw a circle filled with the gradient
		painter.setBrush(brush)
		painter.drawEllipse(center, radius, radius)
		painter.end()

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = Example()
	window.show()
	app.exec()


'''
Usage
To use QRadialGradient, you first create an instance of the class, specifying
the center point, radius, and optionally the focal point. You then add color
stops to define how the colors change along the gradient. Finally, you can use
the gradient to fill shapes or backgrounds using QBrush.

Constructor
radial_gradient = QtGui.QRadialGradient(center_x, center_y, radius, focal_x, focal_y)
radial_gradient = QtGui.QRadialGradient(center, radius, focalPoint)
radial_gradient = QtGui.QRadialGradient(center, radius)

center_x, center_y: Coordinates of the center of the gradient.
radius: Radius of the gradient.
focal_x, focal_y: Coordinates of the focal point (optional, defaults to center).
center: A QPointF object representing the center.
focalPoint: A QPointF object representing the focal point.

Methods
setColorAt(position, color): Adds a color stop at the given position (0.0 to 1.0) with the specified color.
setStops(stops): Sets multiple color stops at once, where stops is a list of tuples (position, color).
center(): Returns the center point of the gradient.
focalPoint(): Returns the focal point of the gradient.
radius(): Returns the radius of the gradient.
setCenter(center): Sets the center point of the gradient.
setFocalPoint(focalPoint): Sets the focal point of the gradient.
setRadius(radius): Sets the radius of the gradient.
setCoordinateMode(): Sets the coordinate mode for the gradient (e.g., logical or device coordinates).
setSpread(): Sets the spread method for the gradient (e.g., repeat, reflect, clamp).

'''
