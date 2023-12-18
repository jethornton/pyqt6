#!/usr/bin/env python3

import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'list-widget-3.ui'), self)
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQT6 List Widget!")
		widget_list = ['listWidget', 'treeWidget', 'tableWidget', 
		'groupBox', 'tabWidget', 'toolBox', 'stackedWidget',
		'comboBox', 'fontComboBox']
		for item in widget_list:
			widget = self.findChild(QWidget, item)
			print(f'{item} isinstance {isinstance(widget, QWidget)}')
			if widget:
				print(f'{item}: Evaluates to True')
			else:
				print(f'{item}: Evaluates to False')

		#if isinstance(self.findChild(QListWidget, "mdi_history_lw"), QListWidget):
		#	print('yes')
		#if type(self.findChild(QListWidget, "mdi_history_lw")) is QListWidget:
		#	print('yes')
		#print(f'{self.findChild(QListWidget, "mdi_history_lw").objectName()}')
		#print(f'{self.findChild(QListWidget, "mdi_history_lw")}')
		#lw = self.findChild(QListWidget, "mdi_history_lw")
		#print(type(lw))
		#print(lw.objectName())
		# In PyQt certain object types behave like Python containers when using
		# truthfulness statements: an empty QListWidget returns False.
		# Use if ... is not None:
		#lw_list = self.findChildren(QListWidget)
		#print(lw_list)
		#for item in lw_list:
		#	print(item.objectName())
		#if self.findChild(QListWidget, "mdi_history_lw"):
		#	print('found')
		#if self.findChild(QListWidget, "mdi_history_lw") is not None:
		#	print('found with is not None')
		#else:
		#	print('not found')
		self.show()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())
