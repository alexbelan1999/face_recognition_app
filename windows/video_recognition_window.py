import glob
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import windows.recognition_window as recognition
import windows.progress_video_recognition_window as progressv
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

        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_next.clicked.connect(self.next)
        self.ui.pushButton_file.clicked.connect(self.open_file)

    def back(self):
        self.open_recognition = recognition.Recognition(Video_recognition.video_recognition_info)
        self.open_recognition.show()
        self.close()

    def next(self):
        Video_recognition.file = self.ui.comboBox.currentText()
        Video_recognition.video = self.ui.lineEdit_file.text()
        Video_recognition.seconds = float(self.ui.lineEdit_seconds.text())
        print(Video_recognition.video," ",Video_recognition.file, " ", Video_recognition.seconds)
        self.open_progressrec1 = progressv.Progress_video_recognition(Video_recognition.video_recognition_info, Video_recognition.file, Video_recognition.video, Video_recognition.seconds)
        self.open_progressrec1.show()
        self.close()

    def open_file(self):
        video = QFileDialog.getOpenFileName(self, 'Open file', "..", "*mp4 *avi")[0]
        self.ui.lineEdit_file.setText(video)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Video_recognition()
    application.show()

    sys.exit(app.exec())
