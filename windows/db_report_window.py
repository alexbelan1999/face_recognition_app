import sys

from PyQt5 import QtWidgets, QtGui

import postgresql as pg
import windows.menu_window as menu
from ui.db_report import Ui_DB_report


class DB_report(QtWidgets.QMainWindow):
    DB_report_info = []

    def __init__(self, info=["", "", "", ""], instructor_id=0, group_id=0, subject_id=0, type_id=0):
        super(DB_report, self).__init__()
        self.ui = Ui_DB_report()
        self.ui.setupUi(self)
        DB_report.DB_report_info = info

        sql1 = "SELECT id, full_name FROM public.instructor where login = '" + info[1] + "';"
        instructor = pg.select(info, sql1)

        self.ui.label_instructor2.setText(instructor[0][1])

        sql2 = "SELECT id, name FROM public.groups where id = " + str(group_id) + ";"
        group = pg.select(info, sql2)

        self.ui.label_group2.setText(group[0][1])

        sql3 = "SELECT id, full_name FROM public.students where group_id = " + str(group_id) + "ORDER BY full_name;"
        students1 = pg.select(info, sql3)
        print(students1)
        names = []
        for st in students1:
            names.append(st[1])
        print(names)
        sql4 = "SELECT student_id, classes_id, class_date FROM public.attendance where instructor_id = " + str(
            instructor_id) + " and subject_id = " + str(subject_id) + " and class_type_id = " + str(type_id) + ";"
        attendance = pg.select(info, sql4)
        print(attendance)

        sql5 = "SELECT classes_id, class_date FROM public.attendance where instructor_id = " + str(
            instructor_id) + " and subject_id = " + str(subject_id) + " and class_type_id = " + str(type_id) + ";"
        date_class = pg.select(info, sql5)
        date_class1 = []
        date_class2 = []
        for date in date_class:
            date_class1.append([date[0], str(date[1])])
        print(date_class1[0])
        for date1 in date_class1:
            if date1 not in date_class2:
                date_class2.append(date1)
        print(date_class2)

        date_class3 = []
        for date_c in date_class2:
            date_class3.append(date_c[1] + " пара "+ str(date_c[0]))

        print(date_class3)

        model = QtGui.QStandardItemModel()
        result = []
        for stud in students1:
            res = []
            for date in date_class2:
                for i in attendance:
                    if stud[0] == i[0] and date == [i[1], str(i[2])]:
                        item = QtGui.QStandardItem("+")
                        res.append(item)
            result.append(res)
        print(result)

        for row in result:
            model.appendRow(row)

        model.setHorizontalHeaderLabels(date_class3)
        model.setVerticalHeaderLabels(names)

        self.ui.tableView.setModel(model)
        for i in range(0,model.columnCount()):
            self.ui.tableView.setColumnWidth(i, 150)

        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_back.clicked.connect(self.back_menu)

    def back_menu(self):
        self.open_menu = menu.Menu(DB_report.DB_report_info)
        self.open_menu.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = DB_report()
    application.show()

    sys.exit(app.exec())
