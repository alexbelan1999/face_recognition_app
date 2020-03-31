from PyQt5 import QtWidgets

import windows.db_menu_window as db
import windows.info_window as info
import windows.login_window as login
import windows.recognition_window as recognition
import windows.training_window as training
from ui.menu import Ui_Menu


class Menu(QtWidgets.QMainWindow):
    menu_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Menu, self).__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        Menu.menu_info = info

        self.ui.pushButton_info.clicked.connect(self.start_info)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_training.clicked.connect(self.start_training)
        self.ui.pushButton_recognition.clicked.connect(self.start_recognition)
        self.ui.pushButton_db.clicked.connect(self.start_db)

    def back(self):
        self.open_login = login.Login()
        self.open_login.show()
        self.close()

    def start_info(self):
        self.open_info = info.Info(Menu.menu_info)
        self.open_info.show()
        self.close()

    def start_training(self):
        self.open_training = training.Training(Menu.menu_info)
        self.open_training.show()
        self.close()

    def start_recognition(self):
        self.open_recognition = recognition.Recognition(Menu.menu_info)
        self.open_recognition.show()
        self.close()

    def start_db(self):
        self.open_db = db.DB_menu(Menu.menu_info)
        self.open_db.show()
        self.close()
