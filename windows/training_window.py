import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import windows.menu_window as menu
from ui.training import Ui_Training


class Training(QtWidgets.QMainWindow):
    file = ""
    dir = ""
    training_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Training, self).__init__()
        self.ui = Ui_Training()
        self.ui.setupUi(self)
        Training.training_info = info
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_next.clicked.connect(self.next)
        self.ui.pushButton_dir.clicked.connect(self.open_dir)

    def back(self):
        self.open_menu = menu.Menu(Training.training_info)
        self.open_menu.show()
        self.close()

    def next(self):
        # Training.file = self.ui.lineEdit_file.text()
        # Training.dir = self.ui.lineEdit_dir.text()
        # self.open_progress = test4.Progress_training(Training.training_info, Training.file, Training.dir)
        # self.open_progress.show()
        self.close()

    def open_dir(self):
        fdir = QFileDialog.getExistingDirectory(self, 'Open dir', os.getcwd())
        self.ui.lineEdit_dir.setText(fdir)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Training()
    application.show()

    sys.exit(app.exec())
