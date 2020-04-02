from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.setFixedSize(300, 390)
        ico = QtGui.QIcon("../python_icon.ico")
        Info.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Info)
        self.centralwidget.setObjectName("centralwidget")

        self.label_db = QtWidgets.QLabel(self.centralwidget)
        self.label_db.setGeometry(QtCore.QRect(50, 20, 200, 30))
        self.label_db.setFont(font)
        self.label_db.setObjectName("label_db")

        self.label_db1 = QtWidgets.QLabel(self.centralwidget)
        self.label_db1.setGeometry(QtCore.QRect(50, 60, 200, 30))
        self.label_db1.setFont(font)
        self.label_db1.setObjectName("label_db1")

        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(50, 100, 200, 30))
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")

        self.label_user1 = QtWidgets.QLabel(self.centralwidget)
        self.label_user1.setGeometry(QtCore.QRect(50, 140, 200, 30))
        self.label_user1.setFont(font)
        self.label_user1.setObjectName("label_user1")

        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(50, 180, 200, 30))
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")

        self.label_password1 = QtWidgets.QLabel(self.centralwidget)
        self.label_password1.setGeometry(QtCore.QRect(50, 220, 200, 30))
        self.label_password1.setFont(font)
        self.label_password1.setObjectName("label_password1")

        self.label_host = QtWidgets.QLabel(self.centralwidget)
        self.label_host.setGeometry(QtCore.QRect(50, 260, 200, 30))
        self.label_host.setFont(font)
        self.label_host.setObjectName("label_host")

        self.label_host1 = QtWidgets.QLabel(self.centralwidget)
        self.label_host1.setGeometry(QtCore.QRect(50, 300, 200, 30))
        self.label_host1.setFont(font)
        self.label_host1.setObjectName("label_host1")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 340, 95, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(155, 340, 95, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")

        Info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Info)
        self.statusbar.setObjectName("statusbar")
        Info.setStatusBar(self.statusbar)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Info"))
        self.label_db.setText(_translate("Info", "База данных:"))
        self.label_user.setText(_translate("Info", "Пользователь:"))
        self.label_password.setText(_translate("Info", "Пароль:"))
        self.label_host.setText(_translate("Info", "Host:"))
        self.pushButton_back.setText(_translate("Info", "Назад"))
        self.pushButton_exit.setText(_translate("Info", "Выход"))
