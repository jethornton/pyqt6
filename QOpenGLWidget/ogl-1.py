#!/usr/bin/env python3

import sys

from OpenGL import GL as gl
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtWidgets import QApplication


class Widget(QOpenGLWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("PyQt6, OpenGL 3.3")
		self.resize(400, 400)

	def initializeGL(self):
		gl.glClearColor(0.5, 0.5, 0.5, 1)

	def paintGL(self):
		gl.glClear(gl.GL_COLOR_BUFFER_BIT)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = Widget()
	w.show()
	sys.exit(app.exec())

