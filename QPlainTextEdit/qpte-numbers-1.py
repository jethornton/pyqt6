#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QColor, QTextFormat, QPainter
from PyQt6.QtCore import Qt

class QLineNumberArea(QWidget):
	def __init__(self, editor):
		super().__init__(editor)
		self.codeEditor = editor

	def sizeHint(self):
		return QSize(self.editor.lineNumberAreaWidth(), 0)

	def paintEvent(self, event):
		self.codeEditor.paintEvent(event)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.lineNumberArea = QLineNumberArea(self)

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.view = QPlainTextEdit()
		self.view.blockCountChanged.connect(self.updateLineNumberAreaWidth)
		self.view.updateRequest.connect(self.updateLineNumberArea)
		self.view.cursorPositionChanged.connect(self.highlightCurrentLine)

		layout = QVBoxLayout(central_widget)
		layout.addWidget(self.view)
		self.show()

	def updateLineNumberAreaWidth(self, _):
		self.view.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

	def lineNumberAreaWidth(self):
		digits = 1
		max_value = max(1, self.view.blockCount())
		while max_value >= 10:
			max_value /= 10
			digits += 1
		space = 3 + self.view.fontMetrics().horizontalAdvance('9') * digits
		return space

	def updateLineNumberArea(self, rect, dy):
		if dy:
			self.lineNumberArea.scroll(0, dy)
		else:
			self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
		if rect.contains(self.view.viewport().rect()):
			self.updateLineNumberAreaWidth(0)

	def highlightCurrentLine(self):
		extraSelections = []
		if not self.view.isReadOnly():
			selection = QTextEdit.ExtraSelection()
			lineColor = QColor('yellow').lighter(160)
			selection.format.setBackground(lineColor)
			selection.format.setProperty( QTextFormat.Property.FullWidthSelection , True)
			selection.cursor = self.view.textCursor()
			selection.cursor.clearSelection()
			extraSelections.append(selection)
		self.view.setExtraSelections(extraSelections)

	def paintEvent(self, event):
		painter = QPainter(self.lineNumberArea)

		painter.fillRect(event.rect(),QColor('lightGray'))

		block = self.view.firstVisibleBlock()
		blockNumber = block.blockNumber()
		top = self.view.blockBoundingGeometry(block).translated(self.view.contentOffset()).top()
		bottom = top + self.view.blockBoundingRect(block).height()

		# Just to make sure I use the right font
		height = self.view.fontMetrics().height()
		while block.isValid() and (top <= event.rect().bottom()):
			if block.isVisible() and (bottom >= event.rect().top()):
				number = str(blockNumber + 1)
				painter.setPen(QColor('black'))
				#print(type(top))
				painter.drawText(0, int(top), self.lineNumberArea.width(), height, Qt.AlignmentFlag.AlignRight, number)

			block = block.next()
			top = bottom
			bottom = top + self.view.blockBoundingRect(block).height()
			blockNumber += 1


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())

