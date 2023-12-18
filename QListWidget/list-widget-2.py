#!/usr/bin/env python3

#!/usr/bin/python

import sys
from PyQt6.QtWidgets import (QListWidget, QWidget, QMessageBox,
							 QApplication, QVBoxLayout)


class Example(QWidget):
	def __init__(self):
		super().__init__()
		vbox = QVBoxLayout(self)
		self.lw = QListWidget(objectName='list_test')

		self.lw.addItem('Item #0')
		self.lw.addItems(['Item #1', 'Item #2', 'Item #3', 'Item #4', ])
		self.lw.itemDoubleClicked.connect(self.item_double_clicked)
		self.lw.itemClicked.connect(self.item_clicked)

		vbox.addWidget(self.lw)
		self.setLayout(vbox)

		self.setGeometry(400, 300, 350, 250)
		self.setWindowTitle('QListWidget')
		if self.findChild(QListWidget, 'list_test'):
			print('found')
		else:
			print('nope')
		lw_list = self.findChildren(QListWidget)
		for item in lw_list:
			print(item.objectName())
		self.show()

	def item_double_clicked(self, item):
		QMessageBox.information(self, "Info", f'Double Clicked on {item.text()}')

	def item_clicked(self, item):
		QMessageBox.information(self, "Info", f'Item: {item.text()}\nRow: {self.lw.currentRow()} ')

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec())

