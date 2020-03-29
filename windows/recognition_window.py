import sys

from PyQt5 import QtWidgets

import windows.menu_window as menu
import windows.photo_recognition_window as photo
import windows.video_recognition_window as video
import windows.web_camera_window as web_camera
from ui.recognition import Ui_Recognition

class Recognition(QtWidgets.QMainWindow):
    recognition_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Recognition, self).__init__()
        self.ui = Ui_Recognition()
        self.ui.setupUi(self)
        Recognition.recognition_info = info
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_photo.clicked.connect(self.start_photo)
        self.ui.pushButton_video.clicked.connect(self.start_video)
        self.ui.pushButton_camera.clicked.connect(self.start_camera)

    def back(self):
        self.open_menu = menu.Menu(Recognition.recognition_info)
        self.open_menu.show()
        self.close()

    def start_photo(self):
        self.open_photo = photo.Photo_recognition(Recognition.recognition_info)
        self.open_photo.show()
        self.close()

    def start_video(self):
        self.open_video = video.Video_recognition(Recognition.recognition_info)
        self.open_video.show()
        self.close()

    def start_camera(self):
        self.open_camera = web_camera.Web_camera(Recognition.recognition_info)
        self.open_camera.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Recognition()
    application.show()

    sys.exit(app.exec())
