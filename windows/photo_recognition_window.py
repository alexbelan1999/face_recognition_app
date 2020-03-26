import glob
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import windows.recognition_window as recognition
from ui.photo_recognition import Ui_Photo_recognition


class Photo_recognition(QtWidgets.QMainWindow):
    file1 = ""
    file2 = ""
    dir = ""
    filesdict = {}
    photo_recognition_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Photo_recognition, self).__init__()
        self.ui = Ui_Photo_recognition()
        self.ui.setupUi(self)
        Photo_recognition.photo_recognition_info = info
        filesdict = {}
        path = "../pickle/encodings/*"
        for file in glob.glob(path):
            item = os.path.splitext(os.path.basename(file))[0]
            self.ui.comboBox.addItem(item)
            Photo_recognition.filesdict[item] = file

        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_next.clicked.connect(self.next)
        self.ui.pushButton_dir.clicked.connect(self.open_dir)

    def back(self):
        self.open_recognition = recognition.Recognition(Photo_recognition.photo_recognition_info)
        self.open_recognition.show()
        self.close()

    def next(self):
        file = self.ui.comboBox.currentText()
        Photo_recognition.file1 = Photo_recognition.filesdict.get(file)
        Photo_recognition.file2 = "../pickle/names/" + file + "names.pickle"
        Photo_recognition.dir = self.ui.lineEdit_dir.text()
        print(Photo_recognition.file1, "  ",Photo_recognition.file2 ,"  ", Photo_recognition.dir)
        # self.open_progressrec = test7.Progress_recognition(Photo_recognition.photo_recognition_info, Photo_recognition.file, Photo_recognition.dir)
        # self.open_progressrec.show()
        # self.close()

    def open_dir(self):
        dir = QFileDialog.getExistingDirectory(self, 'Open dir', '..')
        self.ui.lineEdit_dir.setText(dir)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Photo_recognition()
    application.show()

    sys.exit(app.exec())
