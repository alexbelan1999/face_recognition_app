from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Progress_video_recognition(object):
    def setupUi(self, Progress_video_recognition):
        Progress_video_recognition.setObjectName("Progress_video_recognition")
        Progress_video_recognition.setFixedSize(350, 470)
        ico = QtGui.QIcon("mylogo.png")
        Progress_video_recognition.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Progress_video_recognition)
        self.centralwidget.setObjectName("centralwidget")

        self.label_progress = QtWidgets.QLabel(self.centralwidget)
        self.label_progress.setGeometry(QtCore.QRect(50, 20, 170, 30))
        self.label_progress.setFont(font)
        self.label_progress.setObjectName("label_progress")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(50, 60, 250, 30))
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 100, 250, 30))
        self.progressBar.setFont(font)
        self.progressBar.setObjectName("progressBar")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 140, 250, 150))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 300, 250, 30))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(50, 340, 250, 30))
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")

        self.pushButton_report = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_report.setGeometry(QtCore.QRect(50, 380, 250, 30))
        self.pushButton_report.setFont(font)
        self.pushButton_report.setObjectName("pushButton_report")

        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setGeometry(QtCore.QRect(50, 420, 140, 30))
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(200, 420, 100, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Progress_video_recognition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Progress_video_recognition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Progress_video_recognition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Progress_video_recognition)
        self.statusbar.setObjectName("statusbar")
        Progress_video_recognition.setStatusBar(self.statusbar)

        self.retranslateUi(Progress_video_recognition)
        QtCore.QMetaObject.connectSlotsByName(Progress_video_recognition)

    def retranslateUi(self, Progress_video_recognition):
        _translate = QtCore.QCoreApplication.translate
        Progress_video_recognition.setWindowTitle(
            _translate("Progress_video_recognition", "Progress_video_recognition"))
        self.label_progress.setText(_translate("Progress_video_recognition", "Обработка видео"))
        self.pushButton_menu.setText(_translate("Progress_video_recognition", "В главное меню"))
        self.pushButton_exit.setText(_translate("Progress_video_recognition", "Выход"))
        self.pushButton_start.setText(_translate("Progress_video_recognition", "Начало распознавания"))
        self.pushButton_report.setText(_translate("Progress_video_recognition", "Отправить отчет"))
        self.pushButton_add.setText(_translate("Progress_video_recognition", "Добавить студента"))
