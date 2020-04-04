from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DB_report(object):
    def setupUi(self, DB_report):
        DB_report.setObjectName("Camera")
        DB_report.setFixedSize(800, 650)
        ico = QtGui.QIcon("mylogo.png")
        DB_report.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(DB_report)
        self.centralwidget.setObjectName("centralwidget")

        self.label_instructor1 = QtWidgets.QLabel(self.centralwidget)
        self.label_instructor1.setGeometry(QtCore.QRect(50, 20, 130, 30))
        self.label_instructor1.setFont(font)
        self.label_instructor1.setObjectName("label_instructor1")

        self.label_instructor2 = QtWidgets.QLabel(self.centralwidget)
        self.label_instructor2.setGeometry(QtCore.QRect(190, 20, 130, 30))
        self.label_instructor2.setFont(font)
        self.label_instructor2.setObjectName("label_instructor2")

        self.label_group1 = QtWidgets.QLabel(self.centralwidget)
        self.label_group1.setGeometry(QtCore.QRect(50, 60, 130, 30))
        self.label_group1.setFont(font)
        self.label_group1.setObjectName("label_group1")

        self.label_group2 = QtWidgets.QLabel(self.centralwidget)
        self.label_group2.setGeometry(QtCore.QRect(190, 60, 130, 30))
        self.label_group2.setFont(font)
        self.label_group2.setObjectName("label_group2")

        self.label_subject1 = QtWidgets.QLabel(self.centralwidget)
        self.label_subject1.setGeometry(QtCore.QRect(50, 100, 130, 30))
        self.label_subject1.setFont(font)
        self.label_subject1.setObjectName("label_subject1")

        self.label_subject2 = QtWidgets.QLabel(self.centralwidget)
        self.label_subject2.setGeometry(QtCore.QRect(190, 100, 130, 30))
        self.label_subject2.setFont(font)
        self.label_subject2.setObjectName("label_subject2")

        self.label_class_type1 = QtWidgets.QLabel(self.centralwidget)
        self.label_class_type1.setGeometry(QtCore.QRect(50, 140, 130, 30))
        self.label_class_type1.setFont(font)
        self.label_class_type1.setObjectName("label_class_type1")

        self.label_class_type2 = QtWidgets.QLabel(self.centralwidget)
        self.label_class_type2.setGeometry(QtCore.QRect(190, 140, 130, 30))
        self.label_class_type2.setFont(font)
        self.label_class_type2.setObjectName("label_class_type2")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 180, 700, 400))
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 590, 140, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(200, 590, 170, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        DB_report.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DB_report)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        DB_report.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DB_report)
        self.statusbar.setObjectName("statusbar")
        DB_report.setStatusBar(self.statusbar)

        self.retranslateUi(DB_report)
        QtCore.QMetaObject.connectSlotsByName(DB_report)

    def retranslateUi(self, DB_report):
        _translate = QtCore.QCoreApplication.translate
        DB_report.setWindowTitle(_translate("DB_report", "DB_report"))
        self.label_instructor1.setText(_translate("DB_report", "Преподователь:"))
        self.label_group1.setText(_translate("DB_report", "Группа:"))
        self.label_subject1.setText(_translate("DB_report", "Предмет:"))
        self.label_class_type1.setText(_translate("DB_report", "Вид занятия:"))
        self.pushButton_back.setText(_translate("DB_report", "Назад"))
        self.pushButton_exit.setText(_translate("DB_report", "Выход"))
