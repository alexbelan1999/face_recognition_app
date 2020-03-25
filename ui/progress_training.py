from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Progress_training(object):
    def setupUi(self, Progress_training):
        Progress_training.setObjectName("Progress_training")
        Progress_training.setFixedSize(360, 190)
        ico = QtGui.QIcon("mylogo.png")
        Progress_training.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Progress_training)
        self.centralwidget.setObjectName("centralwidget")

        self.label_progress = QtWidgets.QLabel(self.centralwidget)
        self.label_progress.setGeometry(QtCore.QRect(50, 20, 180, 30))
        self.label_progress.setFont(font)
        self.label_progress.setObjectName("label_progress")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(50, 60, 260, 30))
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 100, 260, 30))
        self.progressBar.setFont(font)
        self.progressBar.setObjectName("progressBar")

        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setGeometry(QtCore.QRect(50, 140, 140, 30))
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(200, 140, 110, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Progress_training.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Progress_training)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Progress_training.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Progress_training)
        self.statusbar.setObjectName("statusbar")
        Progress_training.setStatusBar(self.statusbar)

        self.retranslateUi(Progress_training)
        QtCore.QMetaObject.connectSlotsByName(Progress_training)

    def retranslateUi(self, Progress_training):
        _translate = QtCore.QCoreApplication.translate
        Progress_training.setWindowTitle(_translate("Progress_training", "Progress_training"))
        self.label_progress.setText(_translate("Progress_training", "Обработка файлов"))
        self.pushButton_menu.setText(_translate("Progress_training", "В главное меню"))
        self.pushButton_exit.setText(_translate("Progress_training", "Выход"))
        self.pushButton_start.setText(_translate("Progress_training", "Начало обработки"))
