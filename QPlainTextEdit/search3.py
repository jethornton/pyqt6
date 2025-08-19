#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QPlainTextEdit
from PyQt6.QtGui import QTextDocument

app = QApplication([])

plain_text_edit = QPlainTextEdit()
plain_text_edit.setPlainText("This is a sample text. This text contains the word text twice.")

# Find the first occurrence of "text"
found = plain_text_edit.find("text")
print(f"First 'text' found: {found}")

# Find the next occurrence of "text"
found = plain_text_edit.find("text")
print(f"Second 'text' found: {found}")

# Find "Text" with case sensitivity
found = plain_text_edit.find("Text", QTextDocument.FindFlag.FindCaseSensitively)
print(f"'Text' (case-sensitive) found: {found}")

# Find "text" backwards from the end
cursor = plain_text_edit.textCursor()
cursor.movePosition(cursor.MoveOperation.End)
plain_text_edit.setTextCursor(cursor)
found = plain_text_edit.find("text", QTextDocument.FindFlag.FindBackward)
print(f"'text' (backwards) found: {found}")

plain_text_edit.show()
app.exec()
