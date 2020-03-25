from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.setFixedSize(390, 150)
        ico = QtGui.QIcon("mylogo.png")
        Menu.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_training = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_training.setGeometry(QtCore.QRect(50, 20, 140, 30))
        self.pushButton_training.setFont(font)
        self.pushButton_training.setObjectName("pushButton_training")

        self.pushButton_recognition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_recognition.setGeometry(QtCore.QRect(200, 20, 140, 30))
        self.pushButton_recognition.setFont(font)
        self.pushButton_recognition.setObjectName("pushButton_recognition")

        self.pushButton_db = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_db.setGeometry(QtCore.QRect(50, 60, 140, 30))
        self.pushButton_db.setFont(font)
        self.pushButton_db.setObjectName("pushButton_db")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(200, 100, 140, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 100, 140, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_info = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_info.setGeometry(QtCore.QRect(200, 60, 140, 30))
        self.pushButton_info.setFont(font)
        self.pushButton_info.setObjectName("pushButton_info")

        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Menu.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.pushButton_training.setText(_translate("Menu", "Подготовка"))
        self.pushButton_recognition.setText(_translate("Menu", "Распознавание"))
        self.pushButton_db.setText(_translate("Menu", "Работа с БД"))
        self.pushButton_exit.setText(_translate("Menu", "Выход"))
        self.pushButton_back.setText(_translate("Menu", "Назад"))
        self.pushButton_info.setText(_translate("Menu", "Инфо"))
