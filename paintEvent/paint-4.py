#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPainter, QPen
from PyQt6.QtCore import Qt, QRect

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		title="layout management"
		left=500
		top=200
		width=500
		height=400
		iconName="fosseeicon.jpg"
		self.setWindowTitle(title)
		self.setWindowIcon(QIcon(iconName))
		self.setGeometry(left, top, width, height)
		self.should_paint_circle = False
		self.windowcomponents()
		self.label = QLabel(self)
		self.label.hide()
		self.show()

	def windowcomponents(self):
		button=QPushButton("Add", self)
		button.setGeometry(QRect(0, 0, 50, 28))
		button.setIcon(QIcon("addbutton.png"))
		button.setToolTip("<h3>This is for creating random circles<h3>")
		button.clicked.connect(self.paintcircle)
		button=QPushButton("Generate Report", self)
		button.setGeometry(QRect(49,0,150,28))
		button.setIcon(QIcon("generatereport.png"))
		button.setToolTip("This is for generating pdf report of connection between two circles")
		button=QPushButton("Save", self)
		button.setGeometry(QRect(199,0,120,28))
		button.setIcon(QIcon("saveicon.png"))
		button.setToolTip("This is for saving an image of canvas area")

	def paintEvent(self, event):
		super().paintEvent(event)
		if self.should_paint_circle:
			painter = QPainter(self)
			painter.setRenderHint(QPainter.RenderHint.Antialiasing)
			painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.SolidLine))
			painter.drawEllipse(100, 100, 100, 100)

	def paintcircle(self, painter):
		self.should_paint_circle = True
		self.label.setText('<h2>circle<h2>')
		self.label.move(60,100)
		self.label.show()
		self.update()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())
