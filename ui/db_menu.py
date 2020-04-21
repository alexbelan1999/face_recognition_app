from PyQt5 import QtCore, QtGui, QtWidgets

import ui.load_icon as li


class Ui_DB_menu(object):
    def setupUi(self, DB_menu):
        DB_menu.setObjectName("DB_menu")
        DB_menu.setFixedSize(450, 230)
        ico = li.load()
        DB_menu.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(DB_menu)
        self.centralwidget.setObjectName("centralwidget")

        self.label_instructor1 = QtWidgets.QLabel(self.centralwidget)
        self.label_instructor1.setGeometry(QtCore.QRect(50, 20, 150, 30))
        self.label_instructor1.setFont(font)
        self.label_instructor1.setObjectName("label_instructor1")

        self.label_instructor2 = QtWidgets.QLabel(self.centralwidget)
        self.label_instructor2.setGeometry(QtCore.QRect(210, 20, 190, 30))
        self.label_instructor2.setFont(font)
        self.label_instructor2.setObjectName("label_instructor2")

        self.label_group = QtWidgets.QLabel(self.centralwidget)
        self.label_group.setGeometry(QtCore.QRect(50, 60, 150, 30))
        self.label_group.setFont(font)
        self.label_group.setObjectName("label_group")

        self.comboBox_group = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_group.setGeometry(QtCore.QRect(210, 60, 190, 30))
        self.comboBox_group.setFont(font)
        self.comboBox_group.setObjectName("comboBox_group")

        self.label_subject = QtWidgets.QLabel(self.centralwidget)
        self.label_subject.setGeometry(QtCore.QRect(50, 100, 150, 30))
        self.label_subject.setFont(font)
        self.label_subject.setObjectName("label_subject")

        self.comboBox_subject = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_subject.setGeometry(QtCore.QRect(210, 100, 190, 30))
        self.comboBox_subject.setFont(font)
        self.comboBox_subject.setObjectName("comboBox_subject")

        self.label_class_type = QtWidgets.QLabel(self.centralwidget)
        self.label_class_type.setGeometry(QtCore.QRect(50, 140, 150, 30))
        self.label_class_type.setFont(font)
        self.label_class_type.setObjectName("label_class_type")

        self.comboBox_class_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_class_type.setGeometry(QtCore.QRect(210, 140, 190, 30))
        self.comboBox_class_type.setFont(font)
        self.comboBox_class_type.setObjectName("comboBox_class_type")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 180, 80, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(135, 180, 80, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_report = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_report.setGeometry(QtCore.QRect(220, 180, 180, 30))
        self.pushButton_report.setFont(font)
        self.pushButton_report.setObjectName("pushButton_report")

        DB_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DB_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        DB_menu.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(DB_menu)
        self.statusbar.setObjectName("statusbar")
        DB_menu.setStatusBar(self.statusbar)

        self.retranslateUi(DB_menu)
        QtCore.QMetaObject.connectSlotsByName(DB_menu)

    def retranslateUi(self, DB_menu):
        _translate = QtCore.QCoreApplication.translate
        DB_menu.setWindowTitle(_translate("DB_menu", "DB"))
        self.label_instructor1.setText(_translate("DB_menu", "Преподаватель:"))
        self.label_instructor2.setText(_translate("DB_menu", ""))
        self.label_subject.setText(_translate("DB_menu", "Предмет:"))
        self.label_class_type.setText(_translate("DB_menu", "Вид занятия:"))
        self.pushButton_back.setText(_translate("DB_menu", "Назад"))
        self.pushButton_exit.setText(_translate("DB_menu", "Выход"))
        self.pushButton_report.setText(_translate("DB_menu", "Сформировать отчет"))
        self.label_group.setText(_translate("DB_menu", "Группа:"))
