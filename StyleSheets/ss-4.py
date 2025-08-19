#!/usr/bin/env python3

import sys

# disable cache usage must be before any local imports
sys.dont_write_bytecode = True

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout
from PyQt6.QtWidgets import QSpinBox, QDoubleSpinBox

import resources

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('SpinBox QSS')
		self.resize(175, 100)
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.view = QPlainTextEdit()
		layout = QVBoxLayout(central_widget)
		layout.addWidget(self.view)
		sb = QSpinBox()
		sb.setMaximum(10)
		layout.addWidget(sb)
		sbd = QSpinBox()
		sbd.setEnabled(False)
		layout.addWidget(sbd)
		dsb = QDoubleSpinBox()
		layout.addWidget(dsb)

		stylesheet = 'sb-dark.qss'
		#stylesheet = 'sb-light.qss'
		with open(stylesheet,'r') as f:
			style = f.read()
			print(type(style))
			self.set_style(style)
			#self.setStyleSheet(fh.read())
		self.show()

	def set_style(self, style):
		colors = {}
		colors['black-0'] = 'rgb(255, 255, 255)'
		colors['black-20'] = 'rgb(204, 204, 204)'
		colors['black-40'] = 'rgb(153, 153, 153)'
		colors['black-60'] = 'rgb(102, 102, 102)'
		colors['black-80'] = 'rgb(51, 51, 51)'
		colors['black-100'] = 'rgb(0, 0, 0)'
		colors['blue-0'] = 'rgb(128, 128, 128)'
		colors['blue-20'] = 'rgb(102, 102, 153)'
		colors['blue-40'] = 'rgb(77, 77, 179)'
		colors['blue-60'] = 'rgb(51, 51, 204)'
		colors['blue-80'] = 'rgb(25, 25, 230)'
		colors['blue-100'] = 'rgb(0, 0, 255)'
		colors['green-0'] = 'rgb(128, 128, 128)'
		colors['green-20'] = 'rgb(102, 153, 102)'
		colors['green-40'] = 'rgb(77, 179, 77)'
		colors['green-60'] = 'rgb(51, 204, 51)'
		colors['green-80'] = 'rgb(25, 230, 25)'
		colors['green-100'] = 'rgb(0, 255, 0)'
		colors['red-0'] = 'rgb(128, 128, 128)'
		colors['red-20'] = 'rgb(153, 102, 102)'
		colors['red-40'] = 'rgb(179, 77, 77)'
		colors['red-60'] = 'rgb(204, 51, 51)'
		colors['red-80'] = 'rgb(230, 25, 25)'
		colors['red-100'] = 'rgb(255, 0, 0)'
		for key, value in colors.items():
			style = style.replace(key, value)
		self.setStyleSheet(style)

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

