#!/usr/bin/env python3

import sys, re

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QFrame
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import Qt

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



class MainWindow(QMainWindow):
	gcode = [
	';TYPE:SKIN',
	'G1 F1200 X1 Y-9.843 Z-0.36222',
	'G0 X2 Y-9.914',
	'X3 Y1.1 Z10.1',
	'; comment',
	'G10 F1200 X9.914 Y9.843 Z.65844',
	'G0 F9000 X4 Y9.702',
	'G89 X2.5 Y1.1 Z0.1',
	'X333 Y1.1 Z10.1',
	'G1 F1200 X5 Y-9.914 Z.95254',
	'G0 F9000 X6 Y-9.914',
	]

	def __init__(self):
		super().__init__()

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)

		central_layout = QVBoxLayout(central_widget)
		self.plot = QOpenGLWidget(self)
		self.plot.initializeGL()
		self.plot.paintGL = self.paintGL
		central_layout.addWidget(self.plot)

		self.label_frame = QFrame()
		self.label_frame.setMaximumHeight(25)
		sp = self.label_frame.sizePolicy()
		sp.setVerticalPolicy(QSizePolicy.Policy.Minimum)
		#self.label_frame.sizePolicy.Policy.Minimum()
		label_layout = QHBoxLayout(self.label_frame)
		central_layout.addWidget(self.label_frame)

		self.x_lb = QLabel('X')
		label_layout.addWidget(self.x_lb)

		self.path = []

		self.parse(self.gcode)

		self.show()

	def parse(self, gcode):
		codes = ['g0', 'g1', 'g2', 'g3']
		coord = False
		gcode_type = False
		for line in gcode:
			line = line.strip().lower()
			result = re.search(r'[gG].?\d', line) # search for all g codes
			if result: # a g code found
				if result.group() in codes:
					gcode_type = result.group()
					coord = re.findall(r'[xyz][-+]?(?:\d*\.*\d+)', line, re.IGNORECASE)
					coord.insert(0, gcode_type)
					self.path.append(coord)
				else: # not a g code for movement
					gcode_type = False
			else: # no g code
				if gcode_type: # g code still in effect
					coord = re.findall(r'[xyz][-+]?(?:\d*\.*\d+)', line, re.IGNORECASE)
					if coord:
						coord.insert(0, gcode_type)
						self.path.append(coord)

		for item in self.path:
			print(item)


	def paintGL(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()

		glBegin(GL_LINES)
		for move in self.path:
			x = move[1]
			y = move[1]
			glVertex3fv(self.verticies[vertex])
		glEnd()


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

