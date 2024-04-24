#!/usr/bin/env python3

import sys
from PyQt5.QtGui import QOpenGLShader, QOpenGLShaderProgram, QOpenGLVersionProfile, QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QOpenGLWidget
from PyQt5.QtCore import Qt

	
class MyOpenGLWidget(QOpenGLWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

	def initializeGL(self):
		# Create OpenGL context
		profile = QOpenGLVersionProfile()
		profile.setVersion(2, 0)
		self.context().setFormat(QSurfaceFormat())
		self.context().setVersion(profile)
		self.context().create()

		# Set OpenGL state
		self.gl = self.context().versionFunctions(profile)
		self.gl.glClearColor(0.2, 0.3, 0.3, 1.0)
		self.gl.glEnable(self.gl.GL_DEPTH_TEST)

		# Compile shader program
		vertexShader = QOpenGLShader(QOpenGLShader.Vertex)
		vertexShader.compileSourceCode("""
			attribute vec3 aPos;
			void main() {
				gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
			}
		""")

		fragmentShader = QOpenGLShader(QOpenGLShader.Fragment)
		fragmentShader.compileSourceCode("""
			void main() {
				gl_FragColor = vec4(1.0, 0.5, 0.2, 1.0);
			}
		""")

		self.shaderProgram = QOpenGLShaderProgram()
		self.shaderProgram.addShader(vertexShader)
		self.shaderProgram.addShader(fragmentShader)
		self.shaderProgram.link()

		# vertex data
		self.vertices = [
			-0.5, -0.5, 0.0,
			 0.5, -0.5, 0.0,
			 0.0,  0.5, 0.0
		]

		# Create vertex buffer
		self.VBO = self.gl.glGenBuffers(1)
		self.gl.glBindBuffer(self.gl.GL_ARRAY_BUFFER, self.VBO)
		self.gl.glBufferData(self.gl.GL_ARRAY_BUFFER, len(self.vertices) * 4, self.vertices, self.gl.GL_STATIC_DRAW)

		# Create a vertex array object
		self.VAO = self.gl.glGenVertexArrays(1)
		self.gl.glBindVertexArray(self.VAO)
		self.gl.glVertexAttribPointer(0, 3, self.gl.GL_FLOAT, False, 3 * 4, 0)
		self.gl.glEnableVertexAttribArray(0)

	def paintGL(self):
		# Clear screen
		self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)

		# Using shader programs
		self.shaderProgram.bind()

		# draw triangle
		self.gl.glBindVertexArray(self.VAO)
		self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, 3)

	def resizeGL(self, width, height):
		# Set viewport 
		self.gl.glViewport(0, 0, width, height)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My OpenGL Widget")
		self.show()
