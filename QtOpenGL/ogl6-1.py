#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QVBoxLayout, QSlider

from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor
from PyQt6.QtOpenGLWidgets import QOpenGLWidget # provides QGLWidget, a special OpenGL QWidget

import OpenGL.GL as gl # python wrapping of OpenGL
from OpenGL import GLU # OpenGL Utility Library, extends OpenGL functionality

import sys # we'll need this later to run our Qt application

from OpenGL.arrays import vbo
import numpy as np


class GLWidget(QOpenGLWidget):
	def __init__(self, parent=None):
		self.parent = parent
		QOpenGLWidget.__init__(self, parent)

	def initializeGL(self):
		red = 0 / 255.0
		green = 128 / 255.0
		blue = 255 / 255.0
		gl.glClearColor(red, green, blue, 1) # initialize the screen to blue
		gl.glEnable(gl.GL_DEPTH_TEST) # enable depth testing

		self.initGeometry()

		self.rotX = 0.0
		self.rotY = 0.0
		self.rotZ = 0.0

	def resizeGL(self, width, height):
		gl.glViewport(0, 0, width, height)
		gl.glMatrixMode(gl.GL_PROJECTION)
		gl.glLoadIdentity()
		aspect = width / float(height)

		GLU.gluPerspective(45.0, aspect, 1.0, 100.0)
		gl.glMatrixMode(gl.GL_MODELVIEW)

	def paintGL(self):
		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

		gl.glPushMatrix()	# push the current matrix to the current stack

		gl.glTranslate(0.0, 0.0, -50.0)	# third, translate cube to specified depth
		gl.glScale(20.0, 20.0, 20.0)	   # second, scale cube
		gl.glRotate(self.rotX, 1.0, 0.0, 0.0)
		gl.glRotate(self.rotY, 0.0, 1.0, 0.0)
		gl.glRotate(self.rotZ, 0.0, 0.0, 1.0)
		gl.glTranslate(-0.5, -0.5, -0.5)   # first, translate cube center to origin

		gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
		gl.glEnableClientState(gl.GL_COLOR_ARRAY)

		gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vertVBO)
		gl.glColorPointer(3, gl.GL_FLOAT, 0, self.colorVBO)

		gl.glDrawElements(gl.GL_QUADS, len(self.cubeIdxArray), gl.GL_UNSIGNED_INT, self.cubeIdxArray)

		gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
		gl.glDisableClientState(gl.GL_COLOR_ARRAY)

		gl.glPopMatrix()	# restore the previous modelview matrix

	def initGeometry(self):
		self.cubeVtxArray = np.array(
				[[0.0, 0.0, 0.0],
				 [1.0, 0.0, 0.0],
				 [1.0, 1.0, 0.0],
				 [0.0, 1.0, 0.0],
				 [0.0, 0.0, 1.0],
				 [1.0, 0.0, 1.0],
				 [1.0, 1.0, 1.0],
				 [0.0, 1.0, 1.0]])
		self.vertVBO = vbo.VBO(np.reshape(self.cubeVtxArray,
										  (1, -1)).astype(np.float32))
		self.vertVBO.bind()

		self.cubeClrArray = np.array(
				[[0.0, 0.0, 0.0],
				 [1.0, 0.0, 0.0],
				 [1.0, 1.0, 0.0],
				 [0.0, 1.0, 0.0],
				 [0.0, 0.0, 1.0],
				 [1.0, 0.0, 1.0],
				 [1.0, 1.0, 1.0],
				 [0.0, 1.0, 1.0 ]])
		self.colorVBO = vbo.VBO(np.reshape(self.cubeClrArray,
										   (1, -1)).astype(np.float32))
		self.colorVBO.bind()

		self.cubeIdxArray = np.array(
				[0, 1, 2, 3,
				 3, 2, 6, 7,
				 1, 0, 4, 5,
				 2, 1, 5, 6,
				 0, 3, 7, 4,
				 7, 6, 5, 4 ])

	def setRotX(self, val):
		self.rotX = np.pi * val

	def setRotY(self, val):
		self.rotY = np.pi * val

	def setRotZ(self, val):
		self.rotZ = np.pi * val


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.resize(300, 300)
		self.setWindowTitle('PyQt6 OpenGL App')

		self.glWidget = GLWidget(self)
		self.initGUI()

		timer = QTimer(self)
		timer.setInterval(20)   # period, in milliseconds
		timer.timeout.connect(self.glWidget.update)
		timer.start()

	def initGUI(self):
		central_widget = QWidget()
		gui_layout = QVBoxLayout()
		central_widget.setLayout(gui_layout)

		self.setCentralWidget(central_widget)

		gui_layout.addWidget(self.glWidget)

		sliderX = QSlider(Qt.Orientation.Horizontal)
		sliderX.valueChanged.connect(lambda val: self.glWidget.setRotX(val))

		sliderY = QSlider(Qt.Orientation.Horizontal)
		sliderY.valueChanged.connect(lambda val: self.glWidget.setRotY(val))

		sliderZ = QSlider(Qt.Orientation.Horizontal)
		sliderZ.valueChanged.connect(lambda val: self.glWidget.setRotZ(val))

		gui_layout.addWidget(sliderX)
		gui_layout.addWidget(sliderY)
		gui_layout.addWidget(sliderZ)



app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec())

