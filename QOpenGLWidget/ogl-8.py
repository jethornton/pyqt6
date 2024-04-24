#!/usr/bin/env python3

from PyQt6.QtWidgets import QMainWindow, QApplication, QMenu
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QTimer
from OpenGL.GL import *


class GLW(QOpenGLWidget):

    def initializeGL(self):
        print('initializeGL')
        glClearColor(0, 0, 1, 1)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.prepare_sel)

    def paintGL(self):
        print('paintGL')
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 1, 1)
        self.timer.stop()
        self.timer.setSingleShot(True)
        self.timer.start(500)

    def resizeGL(self, w, h):
        print('resizeGL')
        glClearColor(0, 1, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 1, 1)

    def buffers_swapped(self):
        print('buffers_swapped')

    def prepare_sel(self):
        print('prepare_sel')
        self.makeCurrent()
        glClearColor(0, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 1, 1)


class GLW2(QOpenGLWidget):

    def initializeGL(self):
        print('initializeGL (2)')
        glClearColor(0, 0, 1, 1)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.prepare_sel)

    def paintGL(self):
        print('paintGL (2)')
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 1, 1)
        self.timer.stop()
        self.timer.setSingleShot(True)
        self.timer.start(500)

    def resizeGL(self, w, h):
        print('resizeGL (2)')
        glClearColor(0, 1, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 1, 1)

    def buffers_swapped(self):
        print('buffers_swapped (2)')

    def prepare_sel(self):
        print('prepare_sel (2)')
        self.makeCurrent()
        glClearColor(0, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 1, 1)


app = QApplication([])

w = QMainWindow()
glw = GLW()
w.setCentralWidget(glw)
glw.frameSwapped.connect(glw.buffers_swapped)
qa = QAction('Quit')
m = QMenu('File')
m.addAction(qa)
w.menuBar().addMenu(m)
qa.triggered.connect(w.close)

w.show()

w2 = QMainWindow()
glw2 = GLW2()
w2.setCentralWidget(glw2)
#glw2.frameSwapped.connect(glw2.buffers_swapped)
qa2 = QAction('Quit')
m2 = QMenu('File')
m2.addAction(qa2)
w2.menuBar().addMenu(m2)
qa2.triggered.connect(w2.close)
w2.show()

app.exec()
