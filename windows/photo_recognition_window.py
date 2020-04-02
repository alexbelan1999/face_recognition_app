import glob
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import windows.progress_photo_recognition_window as progress
import windows.recognition_window as recognition
from ui.photo_recognition import Ui_Photo_recognition


class Photo_recognition(QtWidgets.QMainWindow):
    file1 = ""
    file2 = ""
    dir = ""
    photo_recognition_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Photo_recognition, self).__init__()
        self.ui = Ui_Photo_recognition()
        self.ui.setupUi(self)
        Photo_recognition.photo_recognition_info = info

        path = "../pickle/encodings/*"
        for file in glob.glob(path):
            item = os.path.splitext(os.path.basename(file))[0]
            self.ui.comboBox.addItem(item)

        self.ui.radioButton1.setChecked(True)
        self.ui.lineEdit_tolerance.setText("0.6")
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_next.clicked.connect(self.next)
        self.ui.pushButton_dir.clicked.connect(self.open_dir)
        self.ui.pushButton_next.setDisabled(True)
        self.ui.lineEdit_tolerance.textChanged.connect(self.disableButton)
        self.ui.lineEdit_dir.textChanged.connect(self.disableButton)

    def disableButton(self):
        if len(self.ui.lineEdit_tolerance.text()) > 0 and len(self.ui.lineEdit_dir.text()) > 0:
            self.ui.pushButton_next.setDisabled(False)

    def back(self):
        self.open_recognition = recognition.Recognition(Photo_recognition.photo_recognition_info)
        self.open_recognition.show()
        self.close()

    def next(self):
        Photo_recognition.file1 = self.ui.comboBox.currentText()
        Photo_recognition.file2 = Photo_recognition.file1 + "names"
        Photo_recognition.dir = self.ui.lineEdit_dir.text()
        tolerance = float(self.ui.lineEdit_tolerance.text())

        model = ""
        if self.ui.radioButton1.isChecked():
            model = "hog"
        else:
            model = "cnn"
        self.open_progressrec = progress.Progress_photo_recognition(Photo_recognition.photo_recognition_info,
                                                                    Photo_recognition.file1, Photo_recognition.file2,
                                                                    Photo_recognition.dir, model, tolerance)
        self.open_progressrec.show()
        self.close()

    def open_dir(self):
        dir = QFileDialog.getExistingDirectory(self, 'Open dir', '.')
        self.ui.lineEdit_dir.setText(dir)
