import cv2
import face_recognition
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

import dump_and_load_pickle as dalp
import postgresql as pg
import windows.menu_window as menu
import windows.report_window as reportw
from ui.progress_video_recognition import Ui_Progress_video_recognition


class Progress_video_recognition_thread(QThread):
    set_signal = pyqtSignal(set)

    def __init__(self, mainwindow, parent=None):
        super(Progress_video_recognition_thread, self).__init__()
        self.mainwindow = mainwindow

    def run(self):
        input_movie = cv2.VideoCapture(Progress_video_recognition.video)
        length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
        known_face_encodings = dalp.load(Progress_video_recognition.file, 0)
        known_face_names = dalp.load(Progress_video_recognition.file + "names", 1)

        frame_number = 0
        seconds = Progress_video_recognition.seconds
        fps = input_movie.get(cv2.CAP_PROP_FPS)
        multiplier = round(fps * seconds)
        names = set()

        while True:
            ret, frame = input_movie.read()
            frame_number += 1
            self.mainwindow.ui.progressBar.setValue(round(frame_number / length, 2) * 100)

            if not ret:
                self.mainwindow.ui.pushButton_exit.setDisabled(False)
                self.mainwindow.ui.pushButton_menu.setDisabled(False)
                self.mainwindow.ui.pushButton_report.setDisabled(False)
                self.mainwindow.ui.pushButton_add.setDisabled(False)
                break

            if frame_number % multiplier == 0:
                rgb_frame = frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_frame, model=Progress_video_recognition.model)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding,
                                                             tolerance=Progress_video_recognition.tolerance)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                    if (name not in names) and (name != "Unknown"):
                        names.add(name)

        input_movie.release()
        self.set_signal.emit(names)


class Progress_video_recognition(QtWidgets.QMainWindow):
    file = ""
    video = ""
    progress_video_info = []
    seconds = 1.0
    model = ""
    tolerance = 0.6

    def __init__(self, info=["", "", "", ""], file="", video="", seconds=1.0, model="", tolerance=0.6):
        super(Progress_video_recognition, self).__init__()
        self.ui = Ui_Progress_video_recognition()
        self.ui.setupUi(self)

        Progress_video_recognition.progress_video_info = info
        Progress_video_recognition.file = file
        Progress_video_recognition.video = video
        Progress_video_recognition.seconds = seconds
        Progress_video_recognition.model = model
        Progress_video_recognition.tolerance = tolerance

        self.ui.progressBar.setValue(0)
        sql = "SELECT full_name FROM public.students WHERE group_id = (SELECT id FROM public.groups WHERE name = '" + file + "');"
        names = pg.select(info, sql)

        for name in names:
            self.ui.comboBox.addItem(name[0])

        self.progress_video_recognition_thread = Progress_video_recognition_thread(mainwindow=self)
        self.progress_video_recognition_thread.set_signal.connect(self.add_text)

        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_start.clicked.connect(self.start_progress)
        self.ui.pushButton_report.clicked.connect(self.report)
        self.ui.pushButton_add.clicked.connect(self.add)

    def back_menu(self):
        self.open_menu = menu.Menu(Progress_video_recognition.progress_video_info)
        self.open_menu.show()
        self.close()

    def start_progress(self):
        self.ui.pushButton_exit.setDisabled(True)
        self.ui.pushButton_menu.setDisabled(True)
        self.ui.pushButton_report.setDisabled(True)
        self.ui.pushButton_add.setDisabled(True)
        self.progress_video_recognition_thread.start()

    def report(self):
        report = self.ui.textEdit.toPlainText()
        report = list(report.split('\n'))
        self.open_report = reportw.Report(Progress_video_recognition.progress_video_info, report,
                                          Progress_video_recognition.file)
        self.open_report.show()
        self.close()

    def add(self):
        person = self.ui.comboBox.currentText()
        persons = self.ui.textEdit.toPlainText()
        if person not in persons:
            self.ui.textEdit.append(person)

    def add_text(self, names):
        for name in names:
            self.ui.textEdit.append(name)
