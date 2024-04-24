#!/usr/bin/env python3

import sys
from functools import cached_property
from PyQt5 import QtCore, QtWidgets, QtGui


class Application(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(Application, self).__init__(parent)

		QtWidgets.QMainWindow.__init__(self)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.create_menu_file()

		self.load_settings()

		button = QtWidgets.QPushButton("Load new files")
		button.clicked.connect(self.another_task)
		self.setCentralWidget(button)

	def create_menu_file(self):
		file_menu = QtWidgets.QMenu("&File", self)
		self.recentfiles_menu = file_menu.addMenu("&Open Recent")
		self.recentfiles_menu.triggered.connect(self.handle_triggered_recentfile)
		self.menuBar().addMenu(file_menu)

	@cached_property
	def settings(self):
		return QtCore.QSettings()

	def load_settings(self):
		filenames = self.settings.value("recent_files", [])
		for filename in filenames:
			self.add_recent_filename(filename)

	def save_settings(self):
		recentfiles = []
		for action in self.recentfiles_menu.actions()[::-1]:
			recentfiles.append(action.text())
		self.settings.setValue("recent_files", recentfiles)

	@QtCore.pyqtSlot(QtWidgets.QAction)
	def handle_triggered_recentfile(self, action):
		self.process_filename(action.text())

	def add_recent_filename(self, filename):
		action = QtWidgets.QAction(filename, self)
		actions = self.recentfiles_menu.actions()
		before_action = actions[0] if actions else None
		self.recentfiles_menu.insertAction(before_action, action)

	def process_filename(self, filename):
		print(filename)

	def closeEvent(self, event):
		super(Application, self).closeEvent(event)
		self.save_settings()

	def another_task(self):
		# DEMO
		# load new filenames
		counter = len(self.recentfiles_menu.actions())
		filenames = [f"foo {counter}"]
		for filename in filenames:
			self.add_recent_filename(filename)


qApp = QtWidgets.QApplication(sys.argv)
application_window = Application()
application_window.setWindowTitle(f"My App")
application_window.show()

sys.exit(qApp.exec_())
