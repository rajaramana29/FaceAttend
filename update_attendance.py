# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_attendance.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_performance_analysis(object):
    def setupUi(self, performance_analysis):
        performance_analysis.setObjectName("performance_analysis")
        performance_analysis.resize(905, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        performance_analysis.setWindowIcon(icon)
        self.grid_layout = QtWidgets.QGridLayout(performance_analysis)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout_1 = QtWidgets.QGridLayout()
        self.grid_layout_1.setObjectName("grid_layout_1")
        self.button_back = QtWidgets.QPushButton(performance_analysis)
        self.button_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon1)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.grid_layout_1.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_update_attendance = QtWidgets.QLabel(performance_analysis)
        self.label_update_attendance.setObjectName("label_update_attendance")
        self.grid_layout_1.addWidget(self.label_update_attendance, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_spacer = QtWidgets.QLabel(performance_analysis)
        self.label_spacer.setText("")
        self.label_spacer.setObjectName("label_spacer")
        self.grid_layout_1.addWidget(self.label_spacer, 0, 2, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_1, 0, 0, 1, 3)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.vertical_layout_3.setObjectName("vertical_layout_3")
        self.checkbox_3 = QtWidgets.QCheckBox(performance_analysis)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkbox_3.setIcon(icon2)
        self.checkbox_3.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_3.setObjectName("checkbox_3")
        self.vertical_layout_3.addWidget(self.checkbox_3)
        self.label_3 = QtWidgets.QLabel(performance_analysis)
        self.label_3.setObjectName("label_3")
        self.vertical_layout_3.addWidget(self.label_3)
        self.grid_layout_2.addLayout(self.vertical_layout_3, 0, 4, 1, 1)
        self.vertical_layout_8 = QtWidgets.QVBoxLayout()
        self.vertical_layout_8.setObjectName("vertical_layout_8")
        self.checkbox_8 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_8.setIcon(icon2)
        self.checkbox_8.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_8.setObjectName("checkbox_8")
        self.vertical_layout_8.addWidget(self.checkbox_8)
        self.label_8 = QtWidgets.QLabel(performance_analysis)
        self.label_8.setObjectName("label_8")
        self.vertical_layout_8.addWidget(self.label_8)
        self.grid_layout_2.addLayout(self.vertical_layout_8, 2, 4, 1, 1)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.checkbox_2 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_2.setIcon(icon2)
        self.checkbox_2.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_2.setObjectName("checkbox_2")
        self.vertical_layout_2.addWidget(self.checkbox_2)
        self.label_2 = QtWidgets.QLabel(performance_analysis)
        self.label_2.setObjectName("label_2")
        self.vertical_layout_2.addWidget(self.label_2)
        self.grid_layout_2.addLayout(self.vertical_layout_2, 0, 2, 1, 1)
        self.vertical_layout_7 = QtWidgets.QVBoxLayout()
        self.vertical_layout_7.setObjectName("vertical_layout_7")
        self.checkbox_7 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_7.setIcon(icon2)
        self.checkbox_7.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_7.setObjectName("checkbox_7")
        self.vertical_layout_7.addWidget(self.checkbox_7)
        self.label_7 = QtWidgets.QLabel(performance_analysis)
        self.label_7.setObjectName("label_7")
        self.vertical_layout_7.addWidget(self.label_7)
        self.grid_layout_2.addLayout(self.vertical_layout_7, 2, 2, 1, 1)
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.checkbox_1 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_1.setIcon(icon2)
        self.checkbox_1.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_1.setObjectName("checkbox_1")
        self.vertical_layout_1.addWidget(self.checkbox_1)
        self.label_1 = QtWidgets.QLabel(performance_analysis)
        self.label_1.setObjectName("label_1")
        self.vertical_layout_1.addWidget(self.label_1)
        self.grid_layout_2.addLayout(self.vertical_layout_1, 0, 0, 1, 1)
        self.vertical_layout_5 = QtWidgets.QVBoxLayout()
        self.vertical_layout_5.setObjectName("vertical_layout_5")
        self.checkbox_5 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_5.setIcon(icon2)
        self.checkbox_5.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_5.setObjectName("checkbox_5")
        self.vertical_layout_5.addWidget(self.checkbox_5)
        self.label_5 = QtWidgets.QLabel(performance_analysis)
        self.label_5.setObjectName("label_5")
        self.vertical_layout_5.addWidget(self.label_5)
        self.grid_layout_2.addLayout(self.vertical_layout_5, 0, 8, 1, 1)
        self.v_line_4 = QtWidgets.QFrame(performance_analysis)
        self.v_line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_4.setObjectName("v_line_4")
        self.grid_layout_2.addWidget(self.v_line_4, 0, 7, 1, 1)
        self.h_line_1 = QtWidgets.QFrame(performance_analysis)
        self.h_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_1.setObjectName("h_line_1")
        self.grid_layout_2.addWidget(self.h_line_1, 1, 0, 1, 1)
        self.vertical_layout_10 = QtWidgets.QVBoxLayout()
        self.vertical_layout_10.setObjectName("vertical_layout_10")
        self.checkbox_10 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_10.setIcon(icon2)
        self.checkbox_10.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_10.setObjectName("checkbox_10")
        self.vertical_layout_10.addWidget(self.checkbox_10)
        self.label_10 = QtWidgets.QLabel(performance_analysis)
        self.label_10.setObjectName("label_10")
        self.vertical_layout_10.addWidget(self.label_10)
        self.grid_layout_2.addLayout(self.vertical_layout_10, 2, 8, 1, 1)
        self.vertical_layout_4 = QtWidgets.QVBoxLayout()
        self.vertical_layout_4.setObjectName("vertical_layout_4")
        self.checkbox_4 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_4.setIcon(icon2)
        self.checkbox_4.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_4.setObjectName("checkbox_4")
        self.vertical_layout_4.addWidget(self.checkbox_4)
        self.label_4 = QtWidgets.QLabel(performance_analysis)
        self.label_4.setObjectName("label_4")
        self.vertical_layout_4.addWidget(self.label_4)
        self.grid_layout_2.addLayout(self.vertical_layout_4, 0, 6, 1, 1)
        self.v_line_1 = QtWidgets.QFrame(performance_analysis)
        self.v_line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_1.setObjectName("v_line_1")
        self.grid_layout_2.addWidget(self.v_line_1, 0, 1, 1, 1)
        self.vertical_layout_9 = QtWidgets.QVBoxLayout()
        self.vertical_layout_9.setObjectName("vertical_layout_9")
        self.checkbox_9 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_9.setIcon(icon2)
        self.checkbox_9.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_9.setObjectName("checkbox_9")
        self.vertical_layout_9.addWidget(self.checkbox_9)
        self.label_9 = QtWidgets.QLabel(performance_analysis)
        self.label_9.setObjectName("label_9")
        self.vertical_layout_9.addWidget(self.label_9)
        self.grid_layout_2.addLayout(self.vertical_layout_9, 2, 6, 1, 1)
        self.v_line_5 = QtWidgets.QFrame(performance_analysis)
        self.v_line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_5.setObjectName("v_line_5")
        self.grid_layout_2.addWidget(self.v_line_5, 2, 1, 1, 1)
        self.vertical_layout_6 = QtWidgets.QVBoxLayout()
        self.vertical_layout_6.setObjectName("vertical_layout_6")
        self.checkbox_6 = QtWidgets.QCheckBox(performance_analysis)
        self.checkbox_6.setIcon(icon2)
        self.checkbox_6.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_6.setObjectName("checkbox_6")
        self.vertical_layout_6.addWidget(self.checkbox_6)
        self.label_6 = QtWidgets.QLabel(performance_analysis)
        self.label_6.setObjectName("label_6")
        self.vertical_layout_6.addWidget(self.label_6)
        self.grid_layout_2.addLayout(self.vertical_layout_6, 2, 0, 1, 1)
        self.v_line_7 = QtWidgets.QFrame(performance_analysis)
        self.v_line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_7.setObjectName("v_line_7")
        self.grid_layout_2.addWidget(self.v_line_7, 2, 5, 1, 1)
        self.v_line_3 = QtWidgets.QFrame(performance_analysis)
        self.v_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_3.setObjectName("v_line_3")
        self.grid_layout_2.addWidget(self.v_line_3, 0, 5, 1, 1)
        self.v_line_6 = QtWidgets.QFrame(performance_analysis)
        self.v_line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_6.setObjectName("v_line_6")
        self.grid_layout_2.addWidget(self.v_line_6, 2, 3, 1, 1)
        self.v_line_2 = QtWidgets.QFrame(performance_analysis)
        self.v_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_2.setObjectName("v_line_2")
        self.grid_layout_2.addWidget(self.v_line_2, 0, 3, 1, 1)
        self.v_line_8 = QtWidgets.QFrame(performance_analysis)
        self.v_line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_8.setObjectName("v_line_8")
        self.grid_layout_2.addWidget(self.v_line_8, 2, 7, 1, 1)
        self.h_line_2 = QtWidgets.QFrame(performance_analysis)
        self.h_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_2.setObjectName("h_line_2")
        self.grid_layout_2.addWidget(self.h_line_2, 1, 2, 1, 1)
        self.h_line_3 = QtWidgets.QFrame(performance_analysis)
        self.h_line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_3.setObjectName("h_line_3")
        self.grid_layout_2.addWidget(self.h_line_3, 1, 4, 1, 1)
        self.h_line_4 = QtWidgets.QFrame(performance_analysis)
        self.h_line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_4.setObjectName("h_line_4")
        self.grid_layout_2.addWidget(self.h_line_4, 1, 6, 1, 1)
        self.h_line_5 = QtWidgets.QFrame(performance_analysis)
        self.h_line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_5.setObjectName("h_line_5")
        self.grid_layout_2.addWidget(self.h_line_5, 1, 8, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_2, 10, 0, 2, 3)
        self.button_update = QtWidgets.QPushButton(performance_analysis)
        self.button_update.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon3)
        self.button_update.setIconSize(QtCore.QSize(32, 32))
        self.button_update.setFlat(False)
        self.button_update.setObjectName("button_update")
        self.grid_layout.addWidget(self.button_update, 13, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_update_icon = QtWidgets.QLabel(performance_analysis)
        self.label_update_icon.setText("")
        self.label_update_icon.setPixmap(QtGui.QPixmap("assets/reload.png"))
        self.label_update_icon.setScaledContents(True)
        self.label_update_icon.setObjectName("label_update_icon")
        self.grid_layout.addWidget(self.label_update_icon, 8, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_placeholder = QtWidgets.QLabel(performance_analysis)
        self.label_placeholder.setObjectName("label_placeholder")
        self.grid_layout.addWidget(self.label_placeholder, 9, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(performance_analysis)
        QtCore.QMetaObject.connectSlotsByName(performance_analysis)
        performance_analysis.setTabOrder(self.checkbox_1, self.checkbox_2)
        performance_analysis.setTabOrder(self.checkbox_2, self.checkbox_3)
        performance_analysis.setTabOrder(self.checkbox_3, self.checkbox_4)
        performance_analysis.setTabOrder(self.checkbox_4, self.checkbox_5)
        performance_analysis.setTabOrder(self.checkbox_5, self.checkbox_6)
        performance_analysis.setTabOrder(self.checkbox_6, self.checkbox_7)
        performance_analysis.setTabOrder(self.checkbox_7, self.checkbox_8)
        performance_analysis.setTabOrder(self.checkbox_8, self.checkbox_9)
        performance_analysis.setTabOrder(self.checkbox_9, self.checkbox_10)
        performance_analysis.setTabOrder(self.checkbox_10, self.button_update)
        performance_analysis.setTabOrder(self.button_update, self.button_back)

    def retranslateUi(self, performance_analysis):
        _translate = QtCore.QCoreApplication.translate
        performance_analysis.setWindowTitle(_translate("performance_analysis", "Performance Analysis"))
        self.label_update_attendance.setText(_translate("performance_analysis", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#888a85;\">UPDATE ATTENDANCE</span></p></body></html>"))
        self.checkbox_3.setText(_translate("performance_analysis", "CheckBox"))
        self.label_3.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_8.setText(_translate("performance_analysis", "CheckBox"))
        self.label_8.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_2.setText(_translate("performance_analysis", "CheckBox"))
        self.label_2.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_7.setText(_translate("performance_analysis", "CheckBox"))
        self.label_7.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_1.setText(_translate("performance_analysis", "CheckBox"))
        self.label_1.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_5.setText(_translate("performance_analysis", "CheckBox"))
        self.label_5.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_10.setText(_translate("performance_analysis", "CheckBox"))
        self.label_10.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_4.setText(_translate("performance_analysis", "CheckBox"))
        self.label_4.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_9.setText(_translate("performance_analysis", "CheckBox"))
        self.label_9.setText(_translate("performance_analysis", "TextLabel"))
        self.checkbox_6.setText(_translate("performance_analysis", "CheckBox"))
        self.label_6.setText(_translate("performance_analysis", "TextLabel"))
        self.label_placeholder.setText(_translate("performance_analysis", "Check or uncheck the boxes to change the status of the attendance record of the student:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    performance_analysis = QtWidgets.QWidget()
    ui = Ui_performance_analysis()
    ui.setupUi(performance_analysis)
    performance_analysis.show()
    sys.exit(app.exec_())
