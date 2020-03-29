import sys

from PyQt5 import QtWidgets

import windows.menu_window as menu
from ui.db_menu import Ui_DB_menu
import postgresql as pg

class DB_menu(QtWidgets.QMainWindow):
    DB_menu_info = []
    instructor = []
    group1 = {}
    subject1 = {}
    class_type1 = {}

    def __init__(self, info=["", "", "", ""]):
        super(DB_menu, self).__init__()
        self.ui = Ui_DB_menu()
        self.ui.setupUi(self)
        DB_menu.DB_menu_info = info

        sql1 = "SELECT id, full_name FROM public.instructor where login = '" + DB_menu.DB_menu_info[1] + "';"
        DB_menu.instructor = pg.select(info, sql1)

        self.ui.label_instructor2.setText(DB_menu.instructor[0][1])

        sql2 = "SELECT id, name FROM public.groups;"
        group2 = pg.select(info, sql2)
        for group in group2:
            self.ui.comboBox_group.addItem(group[1])
            DB_menu.group1[group[1]] = group[0]

        sql3 = "SELECT id, name FROM public.subject;"
        subject2 = pg.select(info, sql3)
        for subject in subject2:
            self.ui.comboBox_subject.addItem(subject[1])
            DB_menu.subject1[subject[1]] = subject[0]

        sql4 = "SELECT id, name FROM public.class_type;"
        class_type2 = pg.select(info, sql4)
        for class_type in class_type2:
            self.ui.comboBox_class_type.addItem(class_type[1])
            DB_menu.class_type1[class_type[1]] = class_type[0]

        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_report.clicked.connect(self.report)

    def back(self):
        self.open_menu = menu.Menu(DB_menu.DB_menu_info)
        self.open_menu.show()
        self.close()

    def report(self):
        instructor_id = DB_menu.instructor[0][0]
        group_id = DB_menu.group1.get(self.ui.comboBox_group.currentText())
        subject_id = DB_menu.subject1.get(self.ui.comboBox_subject.currentText())
        type_id = DB_menu.class_type1.get(self.ui.comboBox_class_type.currentText())
        print(instructor_id," ",group_id," ",subject_id," ",type_id)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = DB_menu()
    application.show()

    sys.exit(app.exec())
