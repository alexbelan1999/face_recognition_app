from PyQt5 import QtWidgets

import windows.menu_window as menu
from ui.info import Ui_Info


class Info(QtWidgets.QMainWindow):
    info_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Info, self).__init__()
        self.ui = Ui_Info()
        self.ui.setupUi(self)
        Info.info_info = info

        self.ui.label_db1.setText(info[0])
        self.ui.label_user1.setText(info[1])
        self.ui.label_password1.setText(info[2])
        self.ui.label_host1.setText(info[3])

        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def back(self):
        self.open_menu = menu.Menu(Info.info_info)
        self.open_menu.show()
        self.close()
