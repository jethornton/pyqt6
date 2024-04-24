#!/usr/bin/env python3


import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout
from PyQt6.QtCore import QSettings

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.view = QPlainTextEdit()
		layout = QVBoxLayout(central_widget)
		layout.addWidget(self.view)

		self.settings = QSettings('JET', 'Flex GUI')
		#print(len(self.settings.allKeys()))
		#print(self.settings.applicationName())

		self.settings.beginGroup("recent_files")
		self.settings.setValue('1', 'file-1.ngc')
		self.settings.setValue('2', 'file-2.ngc')
		self.settings.setValue('3', 'file-3.ngc')
		self.settings.endGroup()
		'''
		self.settings.beginGroup("old_files")
		self.settings.setValue('1', 'old-file-1.ngc')
		self.settings.setValue('2', 'old-file-2.ngc')
		self.settings.setValue('3', 'old-file-3.ngc')
		self.settings.endGroup()
		'''

		#print(self.settings.childGroups())
		#print(self.settings.childKeys())
		keys = self.settings.allKeys()
		files = []
		for key in keys:
			if key.startswith('recent_files'):
				files.append(self.settings.value(key))
				#print(self.settings.value(key))
		files.insert(0, 'file-4.ngc')
		print(files)
		files = files[:5]
		print(files)
		self.settings.beginGroup('recent_files')
		self.settings.remove('')
		for i, item in enumerate(files):
			self.settings.setValue(str(i), item)
		self.settings.endGroup()


		#for key in keys:
		#	print(self.settings.value(key))

		self.show()

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

