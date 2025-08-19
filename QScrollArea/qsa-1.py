#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget, QFrame, QPushButton
from PyQt6.QtWidgets import QGridLayout, QScrollArea, QScroller
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
window_layout = QGridLayout()

scrollarea = QScrollArea()

frame = QFrame()
frame_layout = QGridLayout()

button1 = QPushButton()
button1.setStyleSheet("background-color:rgb(150,0,0);")
button1.setFixedSize(200,200)

button2 = QPushButton()
button2.setStyleSheet("background-color:rgb(150,0,0);")
button2.setFixedSize(200,200)

button3 = QPushButton()
button3.setStyleSheet("background-color:rgb(150,0,0);")
button3.setFixedSize(200,200)

button4 = QPushButton()
button4.setStyleSheet("background-color:rgb(150,0,0);")
button4.setFixedSize(200,200)

frame_layout.addWidget(button1)
frame_layout.addWidget(button2)
frame_layout.addWidget(button3)
frame_layout.addWidget(button4)
frame.setLayout(frame_layout)

scrollarea.setWidget(frame)

QScroller.grabGesture(scrollarea.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)

window_layout.addWidget(scrollarea)
window.setLayout(window_layout)
window.show()
app.exec()


