from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Training(object):
    def setupUi(self, Training):
        Training.setObjectName("Training")
        Training.setFixedSize(420, 270)
        ico = QtGui.QIcon("mylogo.png")
        Training.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Training)
        self.centralwidget.setObjectName("centralwidget")

        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(50, 20, 160, 30))
        self.label_file.setFont(font)
        self.label_file.setObjectName("label_file")

        self.lineEdit_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file.setGeometry(QtCore.QRect(50, 60, 320, 30))
        self.lineEdit_file.setFont(font)
        self.lineEdit_file.setObjectName("lineEdit_file")

        self.pushButton_dir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dir.setGeometry(QtCore.QRect(50, 100, 320, 30))
        self.pushButton_dir.setFont(font)
        self.pushButton_dir.setObjectName("pushButton_dir")

        self.label_dir = QtWidgets.QLabel(self.centralwidget)
        self.label_dir.setGeometry(QtCore.QRect(50, 140, 160, 30))
        self.label_dir.setFont(font)
        self.label_dir.setObjectName("label_dir")

        self.lineEdit_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dir.setGeometry(QtCore.QRect(50, 180, 320, 30))
        self.lineEdit_dir.setFont(font)
        self.lineEdit_dir.setObjectName("lineEdit_dir")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 220, 100, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(160, 220, 100, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(270, 220, 100, 30))
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")

        Training.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Training)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Training.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Training)
        self.statusbar.setObjectName("statusbar")
        Training.setStatusBar(self.statusbar)

        self.retranslateUi(Training)
        QtCore.QMetaObject.connectSlotsByName(Training)

    def retranslateUi(self, Training):
        _translate = QtCore.QCoreApplication.translate
        Training.setWindowTitle(_translate("Training", "Training"))
        self.label_file.setText(_translate("Training", "Введите имя файла:"))
        self.pushButton_dir.setText(_translate("Training", "Выберите каталог для подготовки:"))
        self.pushButton_back.setText(_translate("Training", "Назад"))
        self.pushButton_exit.setText(_translate("Training", "Выход"))
        self.pushButton_next.setText(_translate("Training", "Далее"))
        self.label_dir.setText(_translate("Training", "Каталог:"))
