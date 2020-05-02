from PyQt5 import QtCore, QtGui, QtWidgets

import ui.load_icon as li


class Ui_Web_camera(object):
    def setupUi(self, Web_camera):
        Web_camera.setObjectName("Web_camera")
        Web_camera.setFixedSize(1155, 700)
        ico = li.load()
        Web_camera.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Web_camera)
        self.centralwidget.setObjectName("centralwidget")

        self.label_combo = QtWidgets.QLabel(self.centralwidget)
        self.label_combo.setGeometry(QtCore.QRect(50, 20, 450, 30))
        self.label_combo.setFont(font)
        self.label_combo.setObjectName("label_combo")

        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setGeometry(QtCore.QRect(510, 20, 200, 30))
        self.label_camera.setFont(font)
        self.label_camera.setObjectName("label_camera")

        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setGeometry(QtCore.QRect(825, 20, 250, 30))
        self.label_model.setFont(font)
        self.label_model.setObjectName("label_model")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 60, 450, 30))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(509, 59, 307, 38))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.radioButton1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton1.setGeometry(QtCore.QRect(510, 60, 95, 30))
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")
        self.horizontalLayout.addWidget(self.radioButton1)

        self.radioButton2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton2.setGeometry(QtCore.QRect(615, 60, 95, 30))
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout.addWidget(self.radioButton2)

        self.radioButton3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton3.setGeometry(QtCore.QRect(720, 60, 95, 30))
        self.radioButton3.setFont(font)
        self.radioButton3.setObjectName("radioButton3")
        self.horizontalLayout.addWidget(self.radioButton3)

        self.horizontalLayoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget1.setObjectName("horizontalLayoutWidget1")
        self.horizontalLayoutWidget1.setGeometry(QtCore.QRect(824, 59, 290, 38))
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget1)
        self.horizontalLayout1.setObjectName("horizontalLayout1")

        self.radioButton4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget1)
        self.radioButton4.setGeometry(QtCore.QRect(825, 60, 95, 30))
        self.radioButton4.setFont(font)
        self.radioButton4.setObjectName("radioButton4")
        self.horizontalLayout1.addWidget(self.radioButton4)

        self.radioButton5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget1)
        self.radioButton5.setGeometry(QtCore.QRect(930, 60, 175, 30))
        self.radioButton5.setFont(font)
        self.radioButton5.setObjectName("radioButton5")
        self.horizontalLayout1.addWidget(self.radioButton5)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 100, 130, 30))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton_test = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_test.setGeometry(QtCore.QRect(510, 100, 130, 30))
        self.pushButton_test.setFont(font)
        self.pushButton_test.setObjectName("pushButton_start")

        self.label_test = QtWidgets.QLabel(self.centralwidget)
        self.label_test.setGeometry(QtCore.QRect(650, 100, 100, 30))
        self.label_test.setFont(font)
        self.label_test.setObjectName("label_test")

        self.label_tolerance = QtWidgets.QLabel(self.centralwidget)
        self.label_tolerance.setGeometry(QtCore.QRect(760, 100, 130, 30))
        self.label_tolerance.setFont(font)
        self.label_tolerance.setObjectName("label_tolerance")

        self.lineEdit_tolerance = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tolerance.setGeometry(QtCore.QRect(900, 100, 50, 30))
        self.lineEdit_tolerance.setFont(font)
        self.lineEdit_tolerance.setObjectName("lineEdit_tolerance")

        self.label_video = QtWidgets.QLabel(self.centralwidget)
        self.label_video.setGeometry(QtCore.QRect(50, 140, 640, 480))
        self.label_video.setObjectName("label_video")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(700, 140, 405, 480))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(50, 650, 130, 30))
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(190, 650, 130, 30))
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")

        self.pushButton_report = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_report.setGeometry(QtCore.QRect(330, 650, 150, 30))
        self.pushButton_report.setFont(font)
        self.pushButton_report.setObjectName("pushButton_report")

        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setGeometry(QtCore.QRect(490, 650, 150, 30))
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(650, 650, 130, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Web_camera.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Web_camera)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Web_camera.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Web_camera)
        self.statusbar.setObjectName("statusbar")
        Web_camera.setStatusBar(self.statusbar)

        self.retranslateUi(Web_camera)
        QtCore.QMetaObject.connectSlotsByName(Web_camera)

    def retranslateUi(self, Web_camera):
        _translate = QtCore.QCoreApplication.translate
        Web_camera.setWindowTitle(_translate("Web_camera", "Web_camera"))
        self.label.setText(_translate("Web_camera", "Видео"))
        self.label_video.setText(_translate("Web_camera", ""))
        self.pushButton_start.setText(_translate("Web_camera", "Старт"))
        self.pushButton_stop.setText(_translate("Web_camera", "Стоп"))
        self.pushButton_menu.setText(_translate("Web_camera", "В главное меню"))
        self.pushButton_exit.setText(_translate("Web_camera", "Выход"))
        self.pushButton_report.setText(_translate("Web_camera", "Отправить отчёт"))
        self.label_combo.setText(_translate("Web_camera", "Выберите подготовленный файл для распознавания:"))
        self.label_camera.setText(_translate("Web_camera", "Выберите камеру:"))
        self.radioButton1.setText(_translate("Web_camera", "Camera1"))
        self.radioButton2.setText(_translate("Web_camera", "Camera2"))
        self.radioButton3.setText(_translate("Web_camera", "Camera3"))
        self.label_tolerance.setText(_translate("Web_camera", "Погрешность:"))
        self.label_model.setText(_translate("Web_camera", "Модель для распознавания:"))
        self.radioButton4.setText(_translate("Web_camera", "hog (CPU)"))
        self.radioButton5.setText(_translate("Web_camera", "cnn (GPU/CUDA)"))
        self.pushButton_test.setText(_translate("Web_camera", "Тест камеры"))
