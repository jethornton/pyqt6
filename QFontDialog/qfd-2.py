#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QSizePolicy, QLabel, QFontDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		vbox = QVBoxLayout()

		btn = QPushButton('Dialog', self)
		btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		btn.move(20, 20)

		vbox.addWidget(btn)

		btn.clicked.connect(self.showDialog)

		self.lbl = QLabel('Font Example', self)
		self.lbl.move(130, 20)
		self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

		vbox.addWidget(self.lbl)
		self.setLayout(vbox)

		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle('Font dialog')
		self.show()


	def showDialog(self):
		options = QFontDialog.FontDialogOption.MonospacedFonts
		options |= QFontDialog.FontDialogOption.DontUseNativeDialog

		font, ok = QFontDialog.getFont(self.font(), self, "Choose a Font", options)
		if ok:
			self.lbl.setFont(QFont(font.family(), int(font.pointSize())))
			print(f'family {font.family()}')
			print(f'pointSizeF {font.pointSizeF()}')
			print(f'pointSize {font.pointSize()}')
			print(f'pixelSize {font.pixelSize()}')


def main():

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()
	

