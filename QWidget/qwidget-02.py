#!/usr/bin/env python3

import sys, os

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import Qt

class window(QWidget):
	def __init__(self):
		super().__init__()

		layout = QGridLayout()
		self.setLayout(layout)
		self.resize(300, 100) # width, height
		self.info_lb = QLabel('test', alignment=Qt.AlignmentFlag.AlignHCenter)
		layout.addWidget(self.info_lb, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)
		self.yes_pb = QPushButton('Yes', self)
		layout.addWidget(self.yes_pb, 1, 0, Qt.AlignmentFlag.AlignHCenter)
		self.yes_pb.clicked.connect(self.copy_examples)

		self.no_pb = QPushButton('No', self)
		layout.addWidget(self.no_pb, 1, 1, Qt.AlignmentFlag.AlignHCenter)
		self.no_pb.clicked.connect(self.close)


		path = os.path.join(os.path.expanduser('~'), 'linuxcnc/configs/flex_examples')
		if os.path.isdir(path):
			self.info_lb.setText('The example directory exists\ndo you want to over write it?')

		self.show()

	def copy_examples(self):
		print('copy')
		self.close()

app = QApplication(sys.argv)
win = window()
app.exec()

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
#app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
#window = QWidget()
#window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
#app.exec()

