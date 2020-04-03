import glob
import os

import face_recognition
from PyQt5 import QtWidgets

import dump_and_load_pickle as dalp
import windows.menu_window as menu
from ui.progress_training import Ui_Progress_training
from PyQt5.QtCore import QThread

class Progress_training_thread(QThread):
    def __init__(self, mainwindow, parent=None):
        super(Progress_training_thread, self).__init__()
        self.mainwindow = mainwindow

    def run(self):
        known_face_encodings = []
        known_face_names = []
        path = Progress_training.dir + "/*"
        files = len(glob.glob(path))
        number = 0
        for file in glob.glob(path):
            number += 1
            image = face_recognition.load_image_file(file)
            known_face_encodings.append(face_recognition.face_encodings(image)[0])
            known_face_names.append(os.path.splitext(os.path.basename(file))[0])
            self.mainwindow.ui.progressBar.setValue(round(number / files, 2) * 100)

        dalp.dump(known_face_encodings, Progress_training.file, 0)
        dalp.dump(known_face_names, Progress_training.file + "names", 1)
        if number == files:
            self.mainwindow.ui.pushButton_exit.setDisabled(False)
            self.mainwindow.ui.pushButton_menu.setDisabled(False)


class Progress_training(QtWidgets.QMainWindow):
    file = ""
    dir = ""
    progress_training_info = []

    def __init__(self, info=["", "", "", ""], file="", dir=""):
        super(Progress_training, self).__init__()
        self.ui = Ui_Progress_training()
        self.ui.setupUi(self)
        Progress_training.progress_training_info = info
        Progress_training.file = file
        Progress_training.dir = dir
        self.ui.progressBar.setValue(0)
        self.progress_training_thread = Progress_training_thread(mainwindow=self)

        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_start.clicked.connect(self.start_progress)

    def back_menu(self):
        self.open_menu = menu.Menu(Progress_training.progress_training_info)
        self.open_menu.show()
        self.close()

    def start_progress(self):
        self.ui.pushButton_exit.setDisabled(True)
        self.ui.pushButton_menu.setDisabled(True)
        self.progress_training_thread.start()


