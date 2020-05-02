from PyQt5 import QtCore, QtGui, QtWidgets

import ui.load_icon as li


class Ui_Photo_recognition(object):
    def setupUi(self, Photo_recognition):
        Photo_recognition.setObjectName("Photo_recognition")
        Photo_recognition.setFixedSize(520, 430)
        ico = li.load()
        Photo_recognition.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Photo_recognition)
        self.centralwidget.setObjectName("centralwidget")

        self.label_combo = QtWidgets.QLabel(self.centralwidget)
        self.label_combo.setGeometry(QtCore.QRect(50, 20, 420, 30))
        self.label_combo.setFont(font)
        self.label_combo.setObjectName("label_combo")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 60, 420, 30))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.pushButton_dir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dir.setGeometry(QtCore.QRect(50, 100, 420, 30))
        self.pushButton_dir.setFont(font)
        self.pushButton_dir.setObjectName("pushButton_dir")

        self.label_dir = QtWidgets.QLabel(self.centralwidget)
        self.label_dir.setGeometry(QtCore.QRect(50, 140, 420, 30))
        self.label_dir.setFont(font)
        self.label_dir.setObjectName("label_dir")

        self.lineEdit_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dir.setGeometry(QtCore.QRect(50, 180, 420, 30))
        self.lineEdit_dir.setFont(font)
        self.lineEdit_dir.setObjectName("lineEdit_dir")

        self.label_tolerance = QtWidgets.QLabel(self.centralwidget)
        self.label_tolerance.setGeometry(QtCore.QRect(50, 220, 160, 30))
        self.label_tolerance.setFont(font)
        self.label_tolerance.setObjectName("label_tolerance")

        self.lineEdit_tolerance = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tolerance.setGeometry(QtCore.QRect(50, 260, 420, 30))
        self.lineEdit_tolerance.setFont(font)
        self.lineEdit_tolerance.setObjectName("lineEdit_tolerance")

        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setGeometry(QtCore.QRect(50, 300, 320, 30))
        self.label_model.setFont(font)
        self.label_model.setObjectName("label_model")

        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(50, 340, 200, 30))
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")

        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(QtCore.QRect(260, 340, 200, 30))
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 380, 130, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(195, 380, 130, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(340, 380, 130, 30))
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")

        Photo_recognition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Photo_recognition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Photo_recognition.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Photo_recognition)
        self.statusbar.setObjectName("statusbar")
        Photo_recognition.setStatusBar(self.statusbar)

        self.retranslateUi(Photo_recognition)
        QtCore.QMetaObject.connectSlotsByName(Photo_recognition)

    def retranslateUi(self, Photo_recognition):
        _translate = QtCore.QCoreApplication.translate
        Photo_recognition.setWindowTitle(_translate("Photo_recognition", "Recognition"))
        self.label_combo.setText(_translate("Photo_recognition", "Выберите подготовленный файл для распознавания:"))
        self.pushButton_dir.setText(_translate("Photo_recognition", "Выберите католог с файлами для распознавания"))
        self.label_dir.setText(_translate("Photo_recognition", "Каталог:"))
        self.pushButton_back.setText(_translate("Photo_recognition", "Назад"))
        self.pushButton_exit.setText(_translate("Photo_recognition", "Выход"))
        self.pushButton_next.setText(_translate("Photo_recognition", "Далее"))
        self.label_tolerance.setText(_translate("Photo_recognition", "Погрешность:"))
        self.label_model.setText(_translate("Photo_recognition", "Модель для распознавания:"))
        self.radioButton1.setText(_translate("Photo_recognition", "hog (CPU)"))
        self.radioButton2.setText(_translate("Photo_recognition", "cnn (GPU/CUDA)"))
