#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('Login')
		self.setWindowIcon(QIcon('./assets/lock.png'))

		layout = QVBoxLayout()
		self.setLayout(layout)

		heading = QLabel(
			'Welcome Back',
			alignment=Qt.AlignmentFlag.AlignHCenter
		)
		heading.setObjectName('heading')

		subheading = QLabel(
			'Please enter your email and password to log in.',
			alignment=Qt.AlignmentFlag.AlignHCenter
		)
		subheading.setObjectName('subheading')

		self.email = QLineEdit(self)
		self.email.setPlaceholderText('Enter your email')

		self.password = QLineEdit(self)
		self.password.setEchoMode(QLineEdit.EchoMode.Password)
		self.password.setPlaceholderText('Enter your password')

		self.btn_login = QPushButton('Login')

		layout.addStretch()
		layout.addWidget(heading)
		layout.addWidget(subheading)
		layout.addWidget(QLabel('Email:'))
		layout.addWidget(self.email)
		layout.addWidget(QLabel('Password:'))
		layout.addWidget(self.password)
		layout.addWidget(self.btn_login)
		layout.addStretch()

		with open('login.qss','r') as fh:
			self.setStyleSheet(fh.read())


		self.show()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())
