import sys, os, os.path
from PyQt5 import QtGui

def load():
    if hasattr(sys, "_MEIPASS"):
        icondir = os.path.join(sys._MEIPASS, 'icon/python_icon.ico')
    else:
        icondir = 'icon/python_icon.ico'
    icon = QtGui.QIcon(icondir)
    return icon