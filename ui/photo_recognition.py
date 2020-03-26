from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Photo_recognition(object):
    def setupUi(self, Photo_recognition):
        Photo_recognition.setObjectName("Photo_recognition")
        Photo_recognition.setFixedSize(520, 270)
        ico = QtGui.QIcon("mylogo.png")
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

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 220, 130, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(190, 220, 130, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(330, 220, 130, 30))
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
        self.label_combo.setText(_translate("Photo_recognition", "Выберете подготовленный файл для распознавания"))
        self.pushButton_dir.setText(_translate("Photo_recognition", "Выберите католог с файлами для распознавания"))
        self.label_dir.setText(_translate("Photo_recognition", "Каталог:"))
        self.pushButton_back.setText(_translate("Photo_recognition", "Назад"))
        self.pushButton_exit.setText(_translate("Photo_recognition", "Выход"))
        self.pushButton_next.setText(_translate("Photo_recognition", "Далее"))
