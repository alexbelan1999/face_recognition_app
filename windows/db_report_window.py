from PyQt5 import QtWidgets, QtGui

import postgresql as pg
import windows.db_menu_window as menu
from ui.db_report import Ui_DB_report


class DB_report(QtWidgets.QMainWindow):
    DB_report_info = []

    def __init__(self, info=["", "", "", ""], report_ids=[], report_names=[]):
        super(DB_report, self).__init__()
        self.ui = Ui_DB_report()
        self.ui.setupUi(self)
        DB_report.DB_report_info = info

        self.ui.label_instructor2.setText(report_names[0])
        self.ui.label_group2.setText(report_names[1])
        self.ui.label_subject2.setText(report_names[2])
        self.ui.label_class_type2.setText(report_names[3])

        sql1 = "SELECT id, full_name FROM public.students where group_id = " + str(
            report_ids[1]) + "ORDER BY full_name;"
        students = pg.select(info, sql1)

        names = []

        for st in students:
            names.append(st[1])

        sql2 = "SELECT id, classes_id, class_date FROM public.event WHERE instructor_id = " + str(
            report_ids[0]) + " AND group_id = " + str(report_ids[1]) + " AND subject_id = " + str(
            report_ids[2]) + "AND class_type_id = " + str(report_ids[3]) + ";"
        events = pg.select(info, sql2)

        sql3 = "SELECT id, event_id, student_id FROM public.attendance WHERE student_id IN (SELECT id FROM public.students WHERE group_id = " + str(
            report_ids[1]) + ");"
        attendance = pg.select(info, sql3)

        date_class = []

        if len(events[0]) != 0:
            for date_c in events:
                date_class.append(str(date_c[2]) + " пара " + str(date_c[1]))

            model = QtGui.QStandardItemModel()
            result = []

            for stud in students:
                res = []

                for event in events:
                    for att in attendance:
                        if stud[0] == att[2] and event[0] == att[1]:
                            item = QtGui.QStandardItem("+")
                            res.append(item)
                            break
                    else:
                        item = QtGui.QStandardItem("--")
                        res.append(item)

                result.append(res)

            for row in result:
                model.appendRow(row)

            model.setHorizontalHeaderLabels(date_class)
            model.setVerticalHeaderLabels(names)

            self.ui.tableView.setModel(model)

            for i in range(0, model.columnCount()):
                self.ui.tableView.setColumnWidth(i, 150)

        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_back.clicked.connect(self.back_menu)

    def back_menu(self):
        self.open_menu = menu.DB_menu(DB_report.DB_report_info)
        self.open_menu.show()
        self.close()
