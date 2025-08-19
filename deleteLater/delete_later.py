#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class Example(QWidget):
	def __init__(self):
		super().__init__()

		self.button1 = QPushButton("Delete Button 1", self)
		self.button1.clicked.connect(self.delete_button)
		self.button2 = QPushButton("Print Buttons", self)
		self.button2.clicked.connect(self.print_children)


		vbox = QVBoxLayout()
		vbox.addWidget(self.button1)
		vbox.addWidget(self.button2)
		self.setLayout(vbox)
		for btn in self.findChildren(QPushButton):
			print(btn)

	def delete_button(self):
		sender = self.sender()
		if sender is not None:
			sender.deleteLater()
			print('sender deleted')
			for btn in self.findChildren(QPushButton):
				print(btn)

		else:
			print('wtf')

	def print_children(self):
		print('buttons')
		for btn in self.findChildren(QPushButton):
			print(btn)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec())
