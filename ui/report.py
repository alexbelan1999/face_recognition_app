from PyQt5 import QtCore, QtGui, QtWidgets
import ui.load_icon as li


class Ui_Report(object):
    def setupUi(self, Report):
        Report.setObjectName("Report")
        Report.setFixedSize(500, 640)
        ico = li.load()
        Report.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Report)
        self.centralwidget.setObjectName("centralwidget")

        self.label_instructor1 = QtWidgets.QLabel(self.centralwidget)
        self.label_instructor1.setGeometry(QtCore.QRect(50, 20, 140, 30))
        self.label_instructor1.setFont(font)
        self.label_instructor1.setObjectName("label_instructor1")

        self.label_instructor2 = QtWidgets.QLabel(self.centralwidget)
        self.label_instructor2.setGeometry(QtCore.QRect(190, 20, 140, 30))
        self.label_instructor2.setFont(font)
        self.label_instructor2.setObjectName("label_instructor2")

        self.label_students = QtWidgets.QLabel(self.centralwidget)
        self.label_students.setGeometry(QtCore.QRect(50, 60, 140, 30))
        self.label_students.setFont(font)
        self.label_students.setObjectName("label_students")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 100, 400, 260))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.comboBox_subject = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_subject.setGeometry(QtCore.QRect(50, 370, 200, 30))
        self.comboBox_subject.setFont(font)
        self.comboBox_subject.setObjectName("comboBox_subject")

        self.comboBox_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type.setGeometry(QtCore.QRect(50, 410, 200, 30))
        self.comboBox_type.setFont(font)
        self.comboBox_type.setObjectName("comboBox_type")

        self.label_class1 = QtWidgets.QLabel(self.centralwidget)
        self.label_class1.setGeometry(QtCore.QRect(50, 450, 80, 30))
        self.label_class1.setFont(font)
        self.label_class1.setObjectName("label_class1")

        self.label_class2 = QtWidgets.QLabel(self.centralwidget)
        self.label_class2.setGeometry(QtCore.QRect(140, 450, 100, 30))
        self.label_class2.setFont(font)
        self.label_class2.setObjectName("label_class2")

        self.label_date1 = QtWidgets.QLabel(self.centralwidget)
        self.label_date1.setGeometry(QtCore.QRect(50, 490, 80, 30))
        self.label_date1.setFont(font)
        self.label_date1.setObjectName("label_date1")

        self.label_date2 = QtWidgets.QLabel(self.centralwidget)
        self.label_date2.setGeometry(QtCore.QRect(140, 490, 100, 30))
        self.label_date2.setFont(font)
        self.label_date2.setObjectName("label_date2")

        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(50, 540, 120, 30))
        self.pushButton_send.setFont(font)
        self.pushButton_send.setObjectName("pushButton_send")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(180, 540, 140, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(330, 540, 120, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.label_check = QtWidgets.QLabel(self.centralwidget)
        self.label_check.setGeometry(QtCore.QRect(50, 580, 120, 30))
        self.label_check.setFont(font)
        self.label_check.setObjectName("label_check")

        Report.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Report)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Report.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Report)
        self.statusbar.setObjectName("statusbar")
        Report.setStatusBar(self.statusbar)

        self.retranslateUi(Report)
        QtCore.QMetaObject.connectSlotsByName(Report)

    def retranslateUi(self, Report):
        _translate = QtCore.QCoreApplication.translate
        Report.setWindowTitle(_translate("Report", "Report"))
        self.label_instructor1.setText(_translate("Report", "Преподаватель:"))
        self.label_instructor2.setText(_translate("Report", ""))
        self.label_students.setText(_translate("Report", "Студенты:"))
        self.label_class1.setText(_translate("Report", "Пара:"))
        self.label_class2.setText(_translate("Report", ""))
        self.label_date1.setText(_translate("Report", "Дата:"))
        self.label_date2.setText(_translate("Report", ""))
        self.pushButton_send.setText(_translate("Report", "Отправить"))
        self.pushButton_back.setText(_translate("Report", "Назад в меню"))
        self.pushButton_exit.setText(_translate("Report", "Выход"))
