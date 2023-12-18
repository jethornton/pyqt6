#!/usr/bin/env python3

'''
required dependencies
sudo apt install python3-pyqt6.qtquick3d
sudo apt install python3-pyqt6.qtquick
sudo apt install qml6-module-qtquick
sudo apt install qml6-module-qtquick-controls
sudo apt install qml6-module-qtquick-templates
sudo apt install qml6-module-qtquick-window
sudo apt install qml6-module-qtqml-workerscript
'''

import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QTimer, QObject, pyqtSignal

from time import strftime, localtime

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')


class Backend(QObject):

    updated = pyqtSignal(str, arguments=['time'])

    def __init__(self):
        super().__init__()

        # Define timer.
        self.timer = QTimer()
        self.timer.setInterval(100)  # msecs 100 = 1/10th sec
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        # Pass the current time to QML.
        curr_time = strftime("%H:%M:%S", localtime())
        self.updated.emit(curr_time)


# Define our backend object, which we pass to QML.
backend = Backend()

engine.rootObjects()[0].setProperty('backend', backend)

# Initial call to trigger first update. Must be after the setProperty to connect signals.
backend.update_time()

sys.exit(app.exec())
