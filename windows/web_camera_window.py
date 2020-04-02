import glob
import os

import cv2
import face_recognition
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage

import dump_and_load_pickle as dalp
import windows.menu_window as menu
import windows.report_window as reportw
from ui.web_camera import Ui_Web_camera


class Web_camera(QtWidgets.QMainWindow):
    stop = False
    web_camera_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Web_camera, self).__init__()
        self.ui = Ui_Web_camera()
        self.ui.setupUi(self)

        Web_camera.web_camera_info = info
        path = "../pickle/encodings/*"
        for file in glob.glob(path):
            item = os.path.splitext(os.path.basename(file))[0]
            self.ui.comboBox.addItem(item)

        self.ui.radioButton1.setChecked(True)
        self.ui.radioButton3.setChecked(True)
        self.ui.lineEdit_tolerance.setText("0.6")

        self.ui.pushButton_start.clicked.connect(self.camera)
        self.ui.pushButton_stop.clicked.connect(self.stop_rec)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_report.clicked.connect(self.report)

    def camera(self):
        self.ui.pushButton_exit.setDisabled(True)
        self.ui.pushButton_menu.setDisabled(True)
        self.ui.pushButton_report.setDisabled(True)

        file = self.ui.comboBox.currentText()

        tolerance = float(self.ui.lineEdit_tolerance.text())

        model = ""
        if self.ui.radioButton3.isChecked():
            model = "hog"
        else:
            model = "cnn"

        known_face_encodings = dalp.load(file, 0)
        known_face_names = dalp.load(file + "names", 1)
        video_capture_number = 0

        # if self.ui.radioButton1.isChecked():
        #     video_capture_number = 0
        # else:
        #     video_capture_number = 2
        # print(video_capture_number)
        # print(model)
        # video_capture = cv2.VideoCapture(video_capture_number)
        # print(video_capture.isOpened())
        Web_camera.stop = False
        names = set()
        frame_number = 0
        while True:
            if Web_camera.stop:
                print("Stop")
                break
            frame_number += 1
            print(frame_number)
            #self.ui.label_video.setText(str(frame_number))

    def stop_rec(self):
        Web_camera.stop = True
        self.ui.pushButton_exit.setDisabled(False)
        self.ui.pushButton_menu.setDisabled(False)
        self.ui.pushButton_report.setDisabled(False)

    def back_menu(self):
        self.open_menu = menu.Menu(Web_camera.web_camera_info)
        self.open_menu.show()
        self.close()

    def report(self):
        report = self.ui.textEdit.toPlainText()
        report = list(report.split('\n'))
        file = self.ui.comboBox.currentText()
        self.open_report = reportw.Report(Web_camera.web_camera_info, report, file)
        self.open_report.show()
        self.close()
