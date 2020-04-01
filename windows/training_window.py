from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import windows.menu_window as menu
import windows.progress_training_window as progress
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
        self.ui.pushButton_next.setDisabled(True)
        self.ui.lineEdit_file.textChanged.connect(self.disableButton)
        self.ui.lineEdit_dir.textChanged.connect(self.disableButton)

    def disableButton(self):
        if len(self.ui.lineEdit_file.text()) > 0 and len(self.ui.lineEdit_dir.text()) > 0:
            self.ui.pushButton_next.setDisabled(False)

    def back(self):
        self.open_menu = menu.Menu(Training.training_info)
        self.open_menu.show()
        self.close()

    def next(self):
        Training.file = self.ui.lineEdit_file.text()
        Training.dir = self.ui.lineEdit_dir.text()
        self.open_progress = progress.Progress_training(Training.training_info, Training.file, Training.dir)
        self.open_progress.show()
        self.close()

    def open_dir(self):
        dir = QFileDialog.getExistingDirectory(self, 'Open dir', '..')
        self.ui.lineEdit_dir.setText(dir)
