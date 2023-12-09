#!/usr/bin/env python3

import sys
from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QTextEdit
from PyQt6.QtGui import QColor, QPainter, QTextFormat

class QLineNumberArea(QWidget):
	def __init__(self, editor):
		super().__init__(editor)
		self.codeEditor = editor

	def sizeHint(self):
		return QSize(self.editor.lineNumberAreaWidth(), 0)

	def paintEvent(self, event):
		self.codeEditor.lineNumberAreaPaintEvent(event)


class QCodeEditor(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle('Main window')
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		self.view = QPlainTextEdit()
		layout = QHBoxLayout(central_widget)
		layout.addWidget(self.view)

		#print(self.view.isReadOnly())
		self.view.setPlainText('Testing')
		self.lineNumberArea = QLineNumberArea(self)
		self.view.blockCountChanged.connect(self.updateLineNumberAreaWidth)
		self.view.updateRequest.connect(self.updateLineNumberArea)
		self.view.cursorPositionChanged.connect(self.highlightCurrentLine)
		self.updateLineNumberAreaWidth(0)
		self.show()

	def lineNumberAreaWidth(self):
		digits = 1
		max_value = max(1, self.view.blockCount())
		while max_value >= 10:
			max_value /= 10
			digits += 1
		space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
		return space

	def updateLineNumberAreaWidth(self, _):
		self.view.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

	def updateLineNumberArea(self, rect, dy):
		if dy:
			self.lineNumberArea.scroll(0, dy)
		else:
			self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
		if rect.contains(self.view.viewport().rect()):
			self.updateLineNumberAreaWidth(0)

	def resizeEvent(self, event):
		super().resizeEvent(event)
		cr = self.view.contentsRect()
		self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

	def highlightCurrentLine(self):
		extraSelections = []
		if not self.view.isReadOnly():
			selection = QTextEdit.ExtraSelection()
			lineColor = QColor('yellow').lighter(160)
			selection.format.setBackground(lineColor)
			selection.format.setProperty(QTextFormat.Property.FullWidthSelection, True)
			selection.cursor = self.view.textCursor()
			selection.cursor.clearSelection()
			extraSelections.append(selection)
		self.view.setExtraSelections(extraSelections)

	def lineNumberAreaPaintEvent(self, event):
		painter = QPainter(self.lineNumberArea)

		painter.fillRect(event.rect(), QColor('lightGray'))

		block = self.view.firstVisibleBlock()
		blockNumber = block.blockNumber()
		top = self.view.blockBoundingGeometry(block).translated(self.view.contentOffset()).top()
		bottom = top + self.view.blockBoundingRect(block).height()

		# Just to make sure I use the right font
		height = self.fontMetrics().height()
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
ex = QCodeEditor()
sys.exit(app.exec())


