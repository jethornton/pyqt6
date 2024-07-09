#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtWidgets import QDoubleSpinBox, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(400, 400, 400, 300)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.dsb = QDoubleSpinBox()
		self.dsb.setSingleStep(0.1)
		self.dsb.setMinimum(-100.0)
		self.dsb.setDecimals(4)
		self.dsb.valueChanged.connect(self.show_value)
		self.lbl_1 = QLabel('1')
		self.lbl_2 = QLabel('2')
		self.lbl_3 = QLabel('3')
		self.lbl_4 = QLabel('4')
		layout = QVBoxLayout(central_widget)
		layout.addWidget(self.dsb)
		layout.addWidget(self.lbl_1)
		layout.addWidget(self.lbl_2)
		layout.addWidget(self.lbl_3)
		layout.addWidget(self.lbl_4)
		self.show()

	def show_value(self):
		self.lbl_1.setText("f'{self.dsb.value()}'")
		self.lbl_2.setText(f'{self.dsb.value()}')
		self.lbl_3.setText("f'{self.dsb.value():.4f}'")
		self.lbl_4.setText(f'{self.dsb.value():.4f}')

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

