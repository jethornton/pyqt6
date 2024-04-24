#!/usr/bin/env python3

import sys
import math
import numpy as np
from PIL import Image, ImageQt
from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt
from PyQt5.QtGui import QColor, QOpenGLVersionProfile
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QOpenGLWidget, QWidget)

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.glWidget = GLWidget()
		mainLayout = QHBoxLayout()
		mainLayout.addWidget(self.glWidget)
		self.setLayout(mainLayout)
		self.setWindowTitle("SPHERE")

class GLWidget(QOpenGLWidget):
	def __init__(self, parent=None):
		super().__init__()

		self.object = 0
		self.xRot = 0
		self.yRot = 0
		self.zRot = 0

		self.lastPos = QPoint()

		self.main = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
		self.clear = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

		#self.img = Image.open("BWTopo.png")
		self.img = Image.open("test.png")
		self.mapWidth, self.mapHeight = self.img.size
		pgImData = np.asarray(self.img)
		self.inputMapFile = np.flipud(pgImData)

	def sizeHint(self):
		return QSize(400, 400)

	def setXRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.xRot:
			self.xRot = angle
			self.update()

	def setYRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.yRot:
			self.yRot = angle
			self.update()

	def setZRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.zRot:
			self.zRot = angle
			self.update()

	def initializeGL(self):
		version_profile = QOpenGLVersionProfile()
		version_profile.setVersion(2, 0)
		self.gl = self.context().versionFunctions(version_profile)
		self.gl.initializeOpenGLFunctions()

		self.setClearColor(self.clear.darker())
		self.object = self.makeObject()
		self.gl.glShadeModel(self.gl.GL_SMOOTH)
		self.gl.glEnable(self.gl.GL_DEPTH_TEST)
		self.gl.glEnable(self.gl.GL_CULL_FACE)
		self.gl.glEnable(self.gl.GL_LIGHTING)
		self.gl.glLightModelfv(self.gl.GL_LIGHT_MODEL_AMBIENT, [0.9, 0.9, 0.9, 1.0])
		self.gl.glEnable(self.gl.GL_COLOR_MATERIAL)
		self.gl.glColorMaterial(self.gl.GL_FRONT, self.gl.GL_AMBIENT_AND_DIFFUSE)
		
		self.gl.glActiveTexture(self.gl.GL_TEXTURE0)
		self.text_obj = self.gl.glGenTextures(1)
		self.gl.glBindTexture(self.gl.GL_TEXTURE_2D, self.text_obj)
		self.gl.glPixelStorei(self.gl.GL_UNPACK_ALIGNMENT, 1)
		self.gl.glTexImage2D(self.gl.GL_TEXTURE_2D, 0, self.gl.GL_RGB, self.mapWidth, self.mapHeight, 0, self.gl.GL_RGB, self.gl.GL_UNSIGNED_BYTE, self.inputMapFile.tobytes())
		self.gl.glPixelStorei(self.gl.GL_UNPACK_ALIGNMENT, 4)
		self.gl.glTexParameterf(self.gl.GL_TEXTURE_2D, self.gl.GL_TEXTURE_MAG_FILTER, self.gl.GL_LINEAR)
		self.gl.glTexParameterf(self.gl.GL_TEXTURE_2D, self.gl.GL_TEXTURE_MIN_FILTER, self.gl.GL_LINEAR)

	def paintGL(self):
		self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
		self.gl.glLoadIdentity()
		self.gl.glTranslated(0.0, 0.0, -10.0)
		self.gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
		self.gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
		self.gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)

		self.gl.glEnable(self.gl.GL_TEXTURE_2D) 
		self.gl.glBindTexture(self.gl.GL_TEXTURE_2D, self.text_obj)
		self.gl.glColor3f(1, 1, 1)
		self.gl.glCallList(self.object)

	def resizeGL(self, width, height):
		side = min(width, height)
		if side < 0:
			return

		self.gl.glViewport((width - side) // 2, (height - side) // 2, side, side)

		self.gl.glMatrixMode(self.gl.GL_PROJECTION)
		self.gl.glLoadIdentity()
		self.gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
		self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

	def mousePressEvent(self, event):
		self.lastPos = event.pos()
		print(event.pos())

	def mouseMoveEvent(self, event):
		dx = event.x() - self.lastPos.x()
		dy = event.y() - self.lastPos.y()

		if event.buttons() & Qt.LeftButton:
			self.setXRotation(self.xRot + 8 * dy)
			self.setYRotation(self.yRot + 8 * dx)
		elif event.buttons() & Qt.RightButton:
			self.setXRotation(self.xRot + 8 * dy)
			self.setZRotation(self.zRot + 8 * dx)

		self.lastPos = event.pos()

	def makeObject(self):
		genList = self.gl.glGenLists(1)
		self.gl.glNewList(genList, self.gl.GL_COMPILE)
		self.gl.glBegin(self.gl.GL_TRIANGLES)

		UResolution = 18
		VResolution = 36
		r = 0.3
		startU = 0
		startV = 0
		endU = math.pi * 2
		endV = math.pi
		stepU = (endU-startU)/UResolution # step size between U-points on the grid
		stepV = (endV-startV)/VResolution # step size between V-points on the grid
		for i in range(UResolution):  # U-points
			for j in range(VResolution):  # V-points
				u = i*stepU+startU
				v = j*stepV+startV
				un = endU if (i+1==UResolution) else (i+1)*stepU+startU
				vn = endV if (j+1==VResolution) else (j+1)*stepV+startV

				p0 = [ math.cos(u)*math.sin(v)*r, math.cos(v)*r, math.sin(u)*math.sin(v)*r ]
				p1 = [ math.cos(u)*math.sin(vn)*r, math.cos(vn)*r, math.sin(u)*math.sin(vn)*r ] 
				p2 = [ math.cos(un)*math.sin(v)*r, math.cos(v)*r, math.sin(un)*math.sin(v)*r ]
				p3 = [ math.cos(un)*math.sin(vn)*r, math.cos(vn)*r, math.sin(un)*math.sin(vn)*r ]

				t0 = [i/UResolution, 1-j/VResolution]
				t1 = [i/UResolution, 1-(j+1)/VResolution]
				t2 = [(i+1)/UResolution, 1-j/VResolution]
				t3 = [(i+1)/UResolution, 1-(j+1)/VResolution]

				# Output the first triangle of this grid square
				self.gl.glTexCoord2f(*t0)
				self.gl.glVertex3f(*p0)
				self.gl.glTexCoord2f(*t2)
				self.gl.glVertex3f(*p2)
				self.gl.glTexCoord2f(*t1)
				self.gl.glVertex3f(*p1)

				# Output the other triangle of this grid square
				self.gl.glTexCoord2f(*t3)
				self.gl.glVertex3f(*p3)
				self.gl.glTexCoord2f(*t1)
				self.gl.glVertex3f(*p1)
				self.gl.glTexCoord2f(*t2)
				self.gl.glVertex3f(*p2)

		self.gl.glEnd()
		self.gl.glEndList()

		return genList

	def normalizeAngle(self, angle):
		while angle < 0:
			angle += 360 * 16
		while angle > 360 * 16:
			angle -= 360 * 16
		return angle

	def setClearColor(self, c):
		self.gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

	def setColor(self, c):
		self.gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())

if __name__ == '__main__':

	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
