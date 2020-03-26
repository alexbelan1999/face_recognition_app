import glob
import sys

import face_recognition
import numpy as np
from PyQt5 import QtWidgets

import dump_and_load_pickle as dalp
import postgresql as pg
import windows.menu_window as menu
from ui.progress_photo_recognition import Ui_Progress_photo_recognition


class Progress_photo_recognition(QtWidgets.QMainWindow):
    file1 = ""
    file2 = ""
    dir = ""
    progress_recognition_info = []

    def __init__(self, info=["", "", "", ""], file1="", file2="", dir=""):
        super(Progress_photo_recognition, self).__init__()
        self.ui = Ui_Progress_photo_recognition()
        self.ui.setupUi(self)
        Progress_photo_recognition.progress_recognition_info = info
        Progress_photo_recognition.file1 = file1
        Progress_photo_recognition.file2 = file2
        Progress_photo_recognition.dir = dir
        self.ui.progressBar.setValue(0)
        sql = "SELECT full_name FROM public.students WHERE group_id = (SELECT id FROM public.groups WHERE name = '" + file1 + "');"
        names = pg.select(info, sql)
        for name in names:
            self.ui.comboBox.addItem(name[0])

        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_start.clicked.connect(self.start_progress)
        self.ui.pushButton_report.clicked.connect(self.report)
        self.ui.pushButton_add.clicked.connect(self.add)

    def back_menu(self):
        self.open_menu = menu.Menu(Progress_photo_recognition.progress_recognition_info)
        self.open_menu.show()
        self.close()

    def start_progress(self):
        self.ui.pushButton_exit.setDisabled(True)
        self.ui.pushButton_menu.setDisabled(True)
        self.ui.pushButton_report.setDisabled(True)
        self.ui.pushButton_add.setDisabled(True)
        self.progress()

    def progress(self):
        path = Progress_photo_recognition.dir + "/*"
        print(path)
        print(Progress_photo_recognition.file1, " ", Progress_photo_recognition.file2)
        known_face_encodings = dalp.load(Progress_photo_recognition.file1, 0)
        known_face_names = dalp.load(Progress_photo_recognition.file2, 1)
        files = len(glob.glob(path))
        number = 0
        names = set()
        for file in glob.glob(path):
            print(file)
            number += 1
            unknown_image = face_recognition.load_image_file(file)

            face_locations = face_recognition.face_locations(unknown_image)
            face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                if (name not in names) and (name != "Unknown"):
                    self.ui.textEdit.append(name)
                    names.add(name)

            self.ui.progressBar.setValue(round(number / files, 2) * 100)

        if number == files:
            self.ui.pushButton_exit.setDisabled(False)
            self.ui.pushButton_menu.setDisabled(False)
            self.ui.pushButton_report.setDisabled(False)
            self.ui.pushButton_add.setDisabled(False)

    def report(self):
        report = self.ui.textEdit.toPlainText()
        report = list(report.split('\n'))
        print(report)
        # person = ["Alex","Dima","Vitaly","Ivan","Petr","Artem","Andrey","Alex","Dima","Vitaly","Ivan","Petr","Artem","Andrey","Alex","Dima","Vitaly","Ivan","Petr","Artem","Andrey","Alex","Dima","Vitaly","Ivan","Petr","Artem","Andrey"]
        # self.open_report = test11.Report(Progress_photo_recognition.progress_recognition_info,person)
        # self.open_report.show()
        # self.close()
    def add(self):
        person = self.ui.comboBox.currentText()
        self.ui.textEdit.append(person)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Progress_photo_recognition()
    application.show()

    sys.exit(app.exec())
