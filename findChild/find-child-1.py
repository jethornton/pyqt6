#!/usr/bin/env python3

import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QFrame, QGroupBox, QScrollArea, QStackedWidget
from PyQt6.QtWidgets import QTabWidget, QToolBox, QWidget
from PyQt6.QtWidgets import QListWidget, QTreeWidget, QTableWidget
from PyQt6 import uic

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'find-child-1.ui'), self)
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT6 Find Containers!")
		# In PyQt certain object types behave like Python containers when using
		# truthfulness statements: an empty QListWidget returns False.
		# Use if ... is not None:
		if self.findChild(QFrame, "frame"):
			print('QFrame found')
		elif self.findChild(QFrame, "frame") is not None:
			print('QFrame found with is not None')
		else:
			print('QFrame not found')

		if self.findChild(QGroupBox, "groupBox"):
			print('QGroupBox found')
		elif self.findChild(QGroupBox, "groupBox") is not None:
			print('QGroupBox found with is not None')
		else:
			print('QGroupBox not found')

		if self.findChild(QScrollArea, "scrollArea"):
			print('QScrollArea found')
		elif self.findChild(QScrollArea, "scrollArea") is not None:
			print('QScrollArea found with is not None')
		else:
			print('QScrollArea not found')

		if self.findChild(QStackedWidget, "stackedWidget"):
			print('QStackedWidget found')
		elif self.findChild(QStackedWidget, "stackedWidget") is not None:
			print('QStackedWidget found with is not None')
		else:
			print('QStackedWidget not found')

		if self.findChild(QTabWidget, "tabWidget"):
			print('QTabWidget found')
		elif self.findChild(QTabWidget, "tabWidget") is not None:
			print('QTabWidget found with is not None')
		else:
			print('QTabWidget not found')

		if self.findChild(QToolBox, "toolBox"):
			print('QToolBox found')
		elif self.findChild(QToolBox, "toolBox") is not None:
			print('QToolBox found with is not None')
		else:
			print('QToolBox not found')

		if self.findChild(QWidget, "widget"):
			print('QWidget found')
		elif self.findChild(QWidget, "widget") is not None:
			print('QWidget found with is not None')
		else:
			print('QWidget not found')

		if self.findChild(QListWidget, "listWidget"):
			print('QListWidget found')
		elif self.findChild(QListWidget, "listWidget") is not None:
			print('QListWidget found with is not None')
		else:
			print('QListWidget not found')

		if self.findChild(QTreeWidget, "treeWidget"):
			print('QTreeWidget found')
		elif self.findChild(QTreeWidget, "treeWidget") is not None:
			print('QTreeWidget found with is not None')
		else:
			print('QTreeWidget not found')

		if self.findChild(QTableWidget, "tableWidget"):
			print('QTableWidget found')
		elif self.findChild(QTableWidget, "tableWidget") is not None:
			print('QTableWidget found with is not None')
		else:
			print('QTableWidget not found')




		self.show()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())
