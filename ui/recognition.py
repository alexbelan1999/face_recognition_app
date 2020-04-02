from PyQt5 import QtCore, QtGui, QtWidgets
import ui.load_icon as li

class Ui_Recognition(object):
    def setupUi(self, Recognition):
        Recognition.setObjectName("Recognition")
        Recognition.setFixedSize(450, 200)
        ico = li.load()
        Recognition.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Recognition)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_photo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_photo.setGeometry(QtCore.QRect(50, 20, 350, 30))
        self.pushButton_photo.setFont(font)
        self.pushButton_photo.setObjectName("pushButton_photo")

        self.pushButton_video = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_video.setGeometry(QtCore.QRect(50, 60, 350, 30))
        self.pushButton_video.setFont(font)
        self.pushButton_video.setObjectName("pushButton_video")

        self.pushButton_camera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_camera.setGeometry(QtCore.QRect(50, 100, 350, 30))
        self.pushButton_camera.setFont(font)
        self.pushButton_camera.setObjectName("pushButton_camera")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 140, 170, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(230, 140, 170, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Recognition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Recognition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Recognition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Recognition)
        self.statusbar.setObjectName("statusbar")
        Recognition.setStatusBar(self.statusbar)

        self.retranslateUi(Recognition)
        QtCore.QMetaObject.connectSlotsByName(Recognition)

    def retranslateUi(self, Recognition):
        _translate = QtCore.QCoreApplication.translate
        Recognition.setWindowTitle(_translate("Recognition", "Recognition"))
        self.pushButton_photo.setText(_translate("Recognition", "Распознавание по фото"))
        self.pushButton_video.setText(_translate("Recognition", "Распознавиние по видео"))
        self.pushButton_camera.setText(_translate("Recognition", "Распознавание с помощью веб-камеры"))
        self.pushButton_back.setText(_translate("Recognition", "Назад"))
        self.pushButton_exit.setText(_translate("Recognition", "Выход"))
