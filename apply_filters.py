from PyQt5 import QtCore, QtGui, QtWidgets
import  mysql.connector

from update_attendance import Ui_Update_Attendance


class Ui_apply_filters(object):
    def __init__(self,UserName):
        self.UserName = UserName
        self.combo_box_date = QtWidgets.QComboBox()
        self.combo_box_subject = QtWidgets.QComboBox()
        
    def setupUi(self, apply_filters):
        apply_filters.setObjectName("apply_filters")
        apply_filters.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        apply_filters.setWindowIcon(icon)
        self.grid_layout = QtWidgets.QGridLayout(apply_filters)
        self.grid_layout.setObjectName("grid_layout")
        self.label_filter_icon = QtWidgets.QLabel(apply_filters)
        self.label_filter_icon.setText("")
        self.label_filter_icon.setPixmap(QtGui.QPixmap("assets/filter.png"))
        self.label_filter_icon.setScaledContents(True)
        self.label_filter_icon.setObjectName("label_filter_icon")
        self.grid_layout.addWidget(self.label_filter_icon, 8, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.button_select = QtWidgets.QPushButton(apply_filters)
        self.button_select.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_select.setIcon(icon1)
        self.button_select.setIconSize(QtCore.QSize(32, 32))
        self.button_select.setFlat(False)
        self.button_select.setObjectName("button_select")
        self.grid_layout.addWidget(self.button_select, 13, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_spacer_bottom = QtWidgets.QLabel(apply_filters)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.grid_layout.addWidget(self.label_spacer_bottom, 12, 1, 1, 1)
        self.grid_layout_1 = QtWidgets.QGridLayout()
        self.grid_layout_1.setObjectName("grid_layout_1")
        self.button_back = QtWidgets.QPushButton(apply_filters)
        self.button_back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon2)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.grid_layout_1.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_update_attendance = QtWidgets.QLabel(apply_filters)
        self.label_update_attendance.setObjectName("label_update_attendance")
        self.grid_layout_1.addWidget(self.label_update_attendance, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_spacer = QtWidgets.QLabel(apply_filters)
        self.label_spacer.setText("")
        self.label_spacer.setObjectName("label_spacer")
        self.grid_layout_1.addWidget(self.label_spacer, 0, 2, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_1, 0, 0, 1, 3)
        self.label_placeholder = QtWidgets.QLabel(apply_filters)
        self.label_placeholder.setObjectName("label_placeholder")
        self.grid_layout.addWidget(self.label_placeholder, 9, 1, 1, 1)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.combo_box_date = QtWidgets.QComboBox(apply_filters)
        self.combo_box_date.setObjectName("combo_box_date")
        self.grid_layout_2.addWidget(self.combo_box_date, 1, 2, 1, 1)
        self.label_subject = QtWidgets.QLabel(apply_filters)
        self.label_subject.setObjectName("label_subject")
        self.grid_layout_2.addWidget(self.label_subject, 0, 1, 1, 1)
        self.label_date = QtWidgets.QLabel(apply_filters)
        self.label_date.setObjectName("label_date")
        self.grid_layout_2.addWidget(self.label_date, 0, 2, 1, 1)
        self.combo_box_subject = QtWidgets.QComboBox(apply_filters)
        self.combo_box_subject.setObjectName("combo_box_subject")
        self.grid_layout_2.addWidget(self.combo_box_subject, 1, 1, 1, 1)
        self.label_spacer_right = QtWidgets.QLabel(apply_filters)
        self.label_spacer_right.setText("")
        self.label_spacer_right.setObjectName("label_spacer_right")
        self.grid_layout_2.addWidget(self.label_spacer_right, 0, 3, 1, 1)
        self.label_spacer_left = QtWidgets.QLabel(apply_filters)
        self.label_spacer_left.setText("")
        self.label_spacer_left.setObjectName("label_spacer_left")
        self.grid_layout_2.addWidget(self.label_spacer_left, 0, 0, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_2, 10, 0, 1, 3)
        self.label_spacer_top = QtWidgets.QLabel(apply_filters)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.grid_layout.addWidget(self.label_spacer_top, 1, 1, 1, 1)

        self.retranslateUi(apply_filters)
        self.FuncUpdateSubject()
        self.button_back.clicked.connect(lambda :self.FuncBack(apply_filters))
        self.combo_box_subject.currentTextChanged.connect(self.FuncDateUpdate)
        self.button_select.clicked.connect(self.FuncButtonUpdate)
        QtCore.QMetaObject.connectSlotsByName(apply_filters)
        apply_filters.setTabOrder(self.button_select, self.button_back)

    def retranslateUi(self, apply_filters):
        _translate = QtCore.QCoreApplication.translate
        apply_filters.setWindowTitle(_translate("apply_filters", "Apply Filters"))
        self.label_update_attendance.setText(_translate("apply_filters", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#888a85;\">APPLY FILTERS</span></p></body></html>"))
        self.label_placeholder.setText(_translate("apply_filters", "Select the subject and the corresponding date for which you want to update the record:"))
        self.label_subject.setText(_translate("apply_filters", "Subject:"))
        self.label_date.setText(_translate("apply_filters", "Date:"))

    def FuncUpdateSubject(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("""SELECT * FROM subjectteacher where teacherid = %s""", (self.UserName,))
            myresult = mycursor.fetchone()
            if myresult is None:
                print("error")
            else:
                for row in myresult:
                    if row != self.UserName:
                        if row:
                            self.combo_box_subject.addItem(row)
        except mysql.connector.Error as er:
            print(er)


    def FuncDateUpdate(self,newValue):
        print(newValue)
        self.newValue = newValue
        try:
            connection  = mysql.connector.connect(
                host="localhost",
                database="collegeattend",
                user="root",
                passwd=""
            )
            cursor = connection.cursor()
            sql = "SELECT classdate FROM `"+str(newValue)+"` ORDER BY classdate ASC"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            if result is None:
                print("error")
            else:
                self.combo_box_date.clear()
                for i in result:
                    print(i[0])
                    self.combo_box_date.addItem(str(i[0]))
        except mysql.connector.Error as er:
            print(er)

    def FuncButtonUpdate(self):
        ClassDate = self.combo_box_date.currentText()
        print(str(ClassDate))
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("""SELECT semestername FROM collegeattend.collgdatatable WHERE %s IN(subject1,subject2,
                            subject3,subject4,subject5,subject6,subject7)""", (self.newValue,))
            myresult = mycursor.fetchone()
            if myresult is None:
                print("error")
            else:
                for row in myresult:
                    Semester = row
        except mysql.connector.Error as er:
            print(er)
        self.WinUpdateAttend = QtWidgets.QWidget()
        self.ui = Ui_Update_Attendance(self.UserName, Semester, self.newValue,ClassDate,)
        self.ui.setupUi(self.WinUpdateAttend)
        self.WinUpdateAttend.show()

    def FuncBack(self,apply_filters):
        apply_filters.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    apply_filters = QtWidgets.QWidget()
    ui = Ui_apply_filters()
    ui.setupUi(apply_filters)
    apply_filters.show()
    sys._excepthook = sys.excepthook


    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook
    sys.exit(app.exec_())
