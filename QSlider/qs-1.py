#!/usr/bin/env python3

#!/usr/bin/python

from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QLabel, QApplication
from PyQt6.QtCore import Qt
import sys

class Example(QWidget):
	def __init__(self):
		super().__init__()

		hbox = QHBoxLayout()

		sld = QSlider(Qt.Orientation.Horizontal, self)
		sld.setRange(0, 100)
		sld.setPageStep(5)

		sld.valueChanged.connect(self.updateLabel)

		self.label = QLabel('0', self)
		self.label.setAlignment(Qt.AlignmentFlag.AlignCenter |
								Qt.AlignmentFlag.AlignVCenter)
		self.label.setMinimumWidth(80)

		hbox.addWidget(sld)
		hbox.addSpacing(15)
		hbox.addWidget(self.label)

		self.setLayout(hbox)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('QSlider')
		self.show()

	def updateLabel(self, value):
		self.label.setText(str(value))


def main():

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()
