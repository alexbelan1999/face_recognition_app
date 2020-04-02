import datetime

from PyQt5 import QtWidgets

import postgresql as pg
import windows.menu_window as menu
from ui.report import Ui_Report


class Report(QtWidgets.QMainWindow):
    report = []
    report_info = []
    file = ""
    students1 = {}
    subject1 = {}
    class_type1 = {}
    instructor = []
    number_class = 0
    date1 = None

    def __init__(self, info=["", "", "", ""], report=[], file=""):
        super(Report, self).__init__()
        self.ui = Ui_Report()
        self.ui.setupUi(self)
        Report.report_info = info
        Report.report = report
        Report.file = file

        sql1 = "SELECT id, full_name FROM public.instructor where login = '" + Report.report_info[1] + "';"
        Report.instructor = pg.select(info, sql1)

        self.ui.label_instructor2.setText(Report.instructor[0][1])

        for person in report:
            self.ui.textEdit.append(person)
        self.ui.textEdit.setReadOnly(True)

        sql2 = "SELECT id, full_name FROM public.students where group_id = (SELECT id FROM public.groups WHERE name = '" + Report.file + "');"
        students2 = pg.select(info, sql2)
        for student in students2:
            Report.students1[student[1]] = student[0]

        sql3 = "SELECT id, name FROM public.subject;"
        subject2 = pg.select(info, sql3)
        for subject in subject2:
            self.ui.comboBox_subject.addItem(subject[1])
            Report.subject1[subject[1]] = subject[0]

        sql4 = "SELECT id, name FROM public.class_type;"
        class_type2 = pg.select(info, sql4)
        for class_type in class_type2:
            self.ui.comboBox_type.addItem(class_type[1])
            Report.class_type1[class_type[1]] = class_type[0]

        sql5 = "SELECT id, start_time, end_time FROM public.classes;"
        time_class = pg.select(info, sql5)
        time1 = datetime.datetime.now().strftime("%H:%M:%S")

        for time_c in time_class:
            if str(time_c[1]) < time1 and time1 < str(time_c[2]):
                Report.number_class = time_c[0]
        self.ui.label_class2.setText(str(Report.number_class))

        Report.date1 = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.label_date2.setText(Report.date1)

        self.ui.pushButton_back.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_send.clicked.connect(self.send)

    def back_menu(self):
        self.open_menu = menu.Menu(Report.report_info)
        self.open_menu.show()
        self.close()

    def send(self):
        report = self.ui.textEdit.toPlainText()
        report = list(report.split('\n'))
        student_id = []
        for rep in report:
            student_id.append(Report.students1.get(rep))

        instructor_id = Report.instructor[0][0]
        subject_id = Report.subject1.get(self.ui.comboBox_subject.currentText())
        type_id = Report.class_type1.get(self.ui.comboBox_type.currentText())

        class_id = Report.number_class
        class_date = Report.date1

        students = []
        for i in student_id:
            students.append([i, instructor_id, subject_id, type_id, class_id, class_date])

        check = pg.insert(Report.report_info, students)

        if check:
            self.ui.label_check.setText("OK!")
        else:
            self.ui.label_check.setText("ERROR!")
