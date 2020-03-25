import sys

from PyQt5 import QtWidgets

from ui.login import Ui_Login
import windows.menu_window as menu

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton_menu.setDisabled(True)
        self.ui.pushButton_menu.clicked.connect(self.start_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.lineEdit_db.setText("face_rec_app")
        self.ui.lineEdit_user.setText("postgres")
        self.ui.lineEdit_password.setText("1234")
        self.ui.lineEdit_host.setText("127.0.0.1")

    def start_menu(self):
        info = []
        info.append(self.ui.lineEdit_db.text())
        info.append(self.ui.lineEdit_user.text())
        info.append(self.ui.lineEdit_password.text())
        info.append(self.ui.lineEdit_host.text())
        self.open_menu = menu.Menu(info)
        self.open_menu.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Login()
    application.show()

    sys.exit(app.exec())
