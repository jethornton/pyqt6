#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenu
from PyQt5.QtGui import QIcon

"""
QMainWindow includes a menu bar, a tool bar and a status bar
"""

class Menu(QMainWindow):

	def __init__(self):
		super().__init__()

		self.actionNew = QAction(QIcon.fromTheme('application-new'), '&New', self)
		self.actionNew.setShortcut('Ctrl+N')
		self.actionNew.setStatusTip('New Something')
		self.actionNew.triggered.connect(self.new)

		self.actionExit = QAction(QIcon.fromTheme('application-exit'), '&Exit', self)
		self.actionExit.setShortcut('Ctrl+Q')
		self.actionExit.setStatusTip('Exit application')
		self.actionExit.triggered.connect(qApp.quit)

		self.statusBar()

		menubar = self.menuBar()
		self.fileMenu = menubar.addMenu('&File')
		self.fileMenu.addAction(self.actionNew)
		self.fileMenu.addAction(self.actionExit)
		#self.fileMenu.addMenu('test')
		#self.fileMenu.insertMenu(self.exitAct, QMenu('Mail', self))

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Menu')
		self.show()

	def new(self):
		print('New Something')
		self.menuRecent = self.fileMenu.insertMenu(self.actionExit, QMenu('Recent', self))
		self.menuRecent.addAction(QAction('File 1'))

app = QApplication(sys.argv)
ex = Menu()
sys.exit(app.exec_())



