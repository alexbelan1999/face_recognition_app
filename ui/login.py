from PyQt5 import QtCore, QtGui, QtWidgets

import postgresql as pg


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setFixedSize(300, 480)
        ico = QtGui.QIcon("mylogo.png")
        Login.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")

        self.label_db = QtWidgets.QLabel(self.centralwidget)
        self.label_db.setGeometry(QtCore.QRect(50, 20, 200, 30))
        self.label_db.setFont(font)
        self.label_db.setObjectName("label_db")

        self.lineEdit_db = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_db.setGeometry(QtCore.QRect(50, 60, 200, 30))
        self.lineEdit_db.setFont(font)
        self.lineEdit_db.setObjectName("lineEdit_db")

        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(50, 100, 200, 30))
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")

        self.lineEdit_user = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_user.setGeometry(QtCore.QRect(50, 140, 200, 30))
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setObjectName("lineEdit_user")

        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(50, 180, 200, 30))
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")

        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(50, 220, 200, 30))
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.label_host = QtWidgets.QLabel(self.centralwidget)
        self.label_host.setGeometry(QtCore.QRect(50, 260, 200, 30))
        self.label_host.setFont(font)
        self.label_host.setObjectName("label_host")

        self.lineEdit_host = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_host.setGeometry(QtCore.QRect(50, 300, 200, 30))
        self.lineEdit_host.setFont(font)
        self.lineEdit_host.setInputMask("000.000.000.000;_")
        self.lineEdit_host.setObjectName("lineEdit_host")

        self.pushButton_test = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_test.setGeometry(QtCore.QRect(50, 340, 95, 30))
        self.pushButton_test.setFont(font)
        self.pushButton_test.clicked.connect(self.test)
        self.pushButton_test.setObjectName("pushButton_test")

        self.label_check = QtWidgets.QLabel(self.centralwidget)
        self.label_check.setGeometry(QtCore.QRect(50, 380, 95, 30))
        self.label_check.setFont(font)
        self.label_check.setObjectName("label_check")

        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setGeometry(QtCore.QRect(155, 340, 95, 30))
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(50, 420, 95, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_test.setObjectName("pushButton_exit")

        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")

        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_db.setText(_translate("Login", "Введите базу данных:"))
        self.label_user.setText(_translate("Login", "Пользователь:"))
        self.label_password.setText(_translate("Login", "Пароль:"))
        self.label_host.setText(_translate("Login", "Host:"))
        self.pushButton_test.setText(_translate("Login", "Тест"))
        self.pushButton_menu.setText(_translate("Login", "Меню"))
        self.pushButton_exit.setText(_translate("Login", "Выход"))

    def test(self):
        dbname = self.lineEdit_db.text()
        user = self.lineEdit_user.text()
        password = self.lineEdit_password.text()
        host = self.lineEdit_host.text()
        test = pg.test_connection(dbname, user, password, host)

        if test:
            self.label_check.setText("OK!")
            self.pushButton_menu.setDisabled(False)
        else:
            self.label_check.setText("ERROR!")
            self.pushButton_menu.setDisabled(True)
