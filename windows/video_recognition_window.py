import glob
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import windows.progress_video_recognition_window as progressv
import windows.recognition_window as recognition
from ui.video_recognition import Ui_Video_recognition


class Video_recognition(QtWidgets.QMainWindow):
    file = ""
    video = ""
    video_recognition_info = []
    seconds = 0.0

    def __init__(self, info=["", "", "", ""]):
        super(Video_recognition, self).__init__()
        self.ui = Ui_Video_recognition()
        self.ui.setupUi(self)
        Video_recognition.video_recognition_info = info
        path = "../pickle/encodings/*"
        for file in glob.glob(path):
            item = os.path.splitext(os.path.basename(file))[0]
            self.ui.comboBox.addItem(item)

        self.ui.radioButton1.setChecked(True)
        self.ui.lineEdit_tolerance.setText("0.6")
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_next.clicked.connect(self.next)
        self.ui.pushButton_file.clicked.connect(self.open_file)
        self.ui.pushButton_next.setDisabled(True)
        self.ui.lineEdit_tolerance.textChanged.connect(self.disableButton)
        self.ui.lineEdit_file.textChanged.connect(self.disableButton)
        self.ui.lineEdit_seconds.textChanged.connect(self.disableButton)

    def disableButton(self):
        if len(self.ui.lineEdit_tolerance.text()) > 0 and len(self.ui.lineEdit_file.text()) > 0 and len(self.ui.lineEdit_seconds.text()) > 0:
            self.ui.pushButton_next.setDisabled(False)

    def back(self):
        self.open_recognition = recognition.Recognition(Video_recognition.video_recognition_info)
        self.open_recognition.show()
        self.close()

    def next(self):
        Video_recognition.file = self.ui.comboBox.currentText()
        Video_recognition.video = self.ui.lineEdit_file.text()
        Video_recognition.seconds = float(self.ui.lineEdit_seconds.text())
        tolerance = float(self.ui.lineEdit_tolerance.text())

        model = ""
        if self.ui.radioButton1.isChecked():
            model = "hog"
        else:
            model = "cnn"
        self.open_progressrec1 = progressv.Progress_video_recognition(Video_recognition.video_recognition_info,
                                                                      Video_recognition.file, Video_recognition.video,
                                                                      Video_recognition.seconds, model, tolerance)
        self.open_progressrec1.show()
        self.close()

    def open_file(self):
        video = QFileDialog.getOpenFileName(self, 'Open file', "..", "*mp4 *avi")[0]
        self.ui.lineEdit_file.setText(video)
