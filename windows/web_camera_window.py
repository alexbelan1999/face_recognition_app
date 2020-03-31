import glob
import os
import sys

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
        if self.ui.radioButton1.isChecked():
            model = "hog"
        else:
            model = "cnn"

        known_face_encodings = dalp.load(file, 0)
        known_face_names = dalp.load(file + "names", 1)
        video_capture_number = 0
        if self.ui.radioButton1.isChecked():
            video_capture_number = 0
        else:
            video_capture_number = 1
        video_capture = cv2.VideoCapture(video_capture_number)
        Web_camera.stop = False
        names = set()
        while True:

            ret, frame = video_capture.read()
            frame = cv2.flip(frame, 1)

            rgb_frame = frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_frame, model=model)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                if (name not in names) and (name != "Unknown"):
                    self.ui.textEdit.append(name)
                    names.add(name)

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)

            cvtFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(cvtFrame, cvtFrame.shape[1], cvtFrame.shape[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)
            self.ui.label_video.setPixmap(pix)

            key = cv2.waitKey(100)
            if Web_camera.stop:
                break

        video_capture.release()

    def stop_rec(self):
        self.ui.pushButton_exit.setDisabled(False)
        self.ui.pushButton_menu.setDisabled(False)
        self.ui.pushButton_report.setDisabled(False)
        Web_camera.stop = True

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


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Web_camera()
    application.show()

    sys.exit(app.exec())
