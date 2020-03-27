from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Video_recognition(object):
    def setupUi(self, Video_recognition):
        Video_recognition.setObjectName("Video_recognition")
        Video_recognition.setFixedSize(520, 350)
        ico = QtGui.QIcon("mylogo.png")
        Video_recognition.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Video_recognition)
        self.centralwidget.setObjectName("centralwidget")

        self.label_combo = QtWidgets.QLabel(self.centralwidget)
        self.label_combo.setGeometry(QtCore.QRect(50, 20, 420, 30))
        self.label_combo.setFont(font)
        self.label_combo.setObjectName("label_combo")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 60, 420, 30))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setGeometry(QtCore.QRect(50, 100, 420, 30))
        self.pushButton_file.setFont(font)
        self.pushButton_file.setObjectName("pushButton_file")

        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(50, 140, 420, 30))
        self.label_file.setFont(font)
        self.label_file.setObjectName("label_file")

        self.lineEdit_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file.setGeometry(QtCore.QRect(50, 180, 420, 30))
        self.lineEdit_file.setFont(font)
        self.lineEdit_file.setObjectName("lineEdit_file")

        self.label_seconds = QtWidgets.QLabel(self.centralwidget)
        self.label_seconds.setGeometry(QtCore.QRect(50, 220, 420, 30))
        self.label_seconds.setFont(font)
        self.label_seconds.setObjectName("label_seconds")

        self.lineEdit_seconds = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_seconds.setGeometry(QtCore.QRect(50, 260, 420, 30))
        self.lineEdit_seconds.setFont(font)
        self.lineEdit_seconds.setObjectName("lineEdit_seconds")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 300, 130, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(190, 300, 130, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(330, 300, 130, 30))
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")

        Video_recognition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Video_recognition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Video_recognition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Video_recognition)
        self.statusbar.setObjectName("statusbar")
        Video_recognition.setStatusBar(self.statusbar)

        self.retranslateUi(Video_recognition)
        QtCore.QMetaObject.connectSlotsByName(Video_recognition)

    def retranslateUi(self, Video_recognition):
        _translate = QtCore.QCoreApplication.translate
        Video_recognition.setWindowTitle(_translate("Video_recognition", "Recognition"))
        self.label_combo.setText(_translate("Video_recognition", "Выберете подготовленный файл для распознавания"))
        self.pushButton_file.setText(_translate("Video_recognition", "Выберите видео файл для распознавания"))
        self.label_file.setText(_translate("Video_recognition", "Файл:"))
        self.label_seconds.setText(_translate("Video_recognition", "Частота обработки кадров (в секундах):"))
        self.pushButton_back.setText(_translate("Video_recognition", "Назад"))
        self.pushButton_exit.setText(_translate("Video_recognition", "Выход"))
        self.pushButton_next.setText(_translate("Video_recognition", "Далее"))
