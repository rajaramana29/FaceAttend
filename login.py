import hashlib
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from error_message import ErrorMessage
from signup import Signup
from dashboard import Dashboard
from admin_panel import AdminPanel
from info import Info


class Login(object):
    def setup_ui(self, login_object):
        self.from_login = login_object
        login_object.setObjectName("login_object")
        login_object.setWindowModality(QtCore.Qt.ApplicationModal)
        login_object.setEnabled(True)
        login_object.resize(380, 420)
        login_object.setFixedSize(380, 420)
        login_object.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_object.setWindowIcon(icon)
        login_object.setLayoutDirection(QtCore.Qt.LeftToRight)
        login_object.setAutoFillBackground(False)
        login_object.setTabShape(QtWidgets.QTabWidget.Rounded)
        login_object.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        login_object.setUnifiedTitleAndToolBarOnMac(False)
        self.central_widget = QtWidgets.QWidget(login_object)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.label_spacer_top = QtWidgets.QLabel(self.central_widget)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.grid_layout.addWidget(self.label_spacer_top, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.grid_layout, 0, 0, 1, 1)
        self.button_signup = QtWidgets.QPushButton(self.central_widget)
        self.button_signup.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_signup.setIcon(icon1)
        self.button_signup.setObjectName("button_signup")
        self.gridLayout.addWidget(self.button_signup, 9, 0, 1, 1)
        self.line_edit_password = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_password.setClearButtonEnabled(True)
        self.line_edit_password.setObjectName("line_edit_password")
        self.gridLayout.addWidget(self.line_edit_password, 4, 0, 1, 1)
        self.label_placeholder = QtWidgets.QLabel(self.central_widget)
        self.label_placeholder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_placeholder.setAlignment(QtCore.Qt.AlignCenter)
        self.label_placeholder.setObjectName("label_placeholder")
        self.gridLayout.addWidget(self.label_placeholder, 8, 0, 1, 1)
        self.label_faceattend_icon = QtWidgets.QLabel(self.central_widget)
        self.label_faceattend_icon.setText("")
        self.label_faceattend_icon.setPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"))
        self.label_faceattend_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_faceattend_icon.setObjectName("label_faceattend_icon")
        self.gridLayout.addWidget(self.label_faceattend_icon, 1, 0, 1, 1,
                                  QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_spacer_bottom = QtWidgets.QLabel(self.central_widget)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.gridLayout.addWidget(self.label_spacer_bottom, 10, 0, 1, 1)
        self.label_spacer_middle_2 = QtWidgets.QLabel(self.central_widget)
        self.label_spacer_middle_2.setText("")
        self.label_spacer_middle_2.setObjectName("label_spacer_middle_2")
        self.gridLayout.addWidget(self.label_spacer_middle_2, 7, 0, 1, 1)
        self.line_edit_username = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_username.setMouseTracking(True)
        self.line_edit_username.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_edit_username.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_username.setClearButtonEnabled(True)
        self.line_edit_username.setObjectName("line_edit_username")
        self.gridLayout.addWidget(self.line_edit_username, 3, 0, 1, 1)
        self.button_login = QtWidgets.QPushButton(self.central_widget)
        self.button_login.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_login.setIcon(icon2)
        self.button_login.setObjectName("button_login")
        self.gridLayout.addWidget(self.button_login, 6, 0, 1, 1)
        self.label_spacer_middle_1 = QtWidgets.QLabel(self.central_widget)
        self.label_spacer_middle_1.setText("")
        self.label_spacer_middle_1.setObjectName("label_spacer_middle_1")
        self.gridLayout.addWidget(self.label_spacer_middle_1, 2, 0, 1, 1)
        login_object.setCentralWidget(self.central_widget)

        login_object.setWindowTitle("Login")
        self.button_signup.setToolTip("Click to get yourself signed up!")
        self.button_signup.setText("Signup")
        self.line_edit_password.setToolTip("Enter your password.")
        self.line_edit_password.setPlaceholderText("Password")
        self.label_placeholder.setText("Don\'t have access to username/password?\n""Contact Computer Centre or Signup "
                                       "to gain access.")
        self.line_edit_username.setToolTip("Enter your username.")
        self.line_edit_username.setPlaceholderText("Username")
        self.button_login.setToolTip("Click to Login!")
        self.button_login.setText("Login")

        QtCore.QMetaObject.connectSlotsByName(login_object)
        login_object.setTabOrder(self.line_edit_username, self.line_edit_password)
        login_object.setTabOrder(self.line_edit_password, self.button_login)
        login_object.setTabOrder(self.button_login, self.button_signup)
        self.button_login.clicked.connect(lambda: self.validate_and_login(login_object))
        self.line_edit_password.returnPressed.connect(lambda: self.validate_and_login(login_object))
        self.button_signup.clicked.connect(lambda: self.signup(login_object))

    def validate_and_login(self, login_object):
        user_name = self.line_edit_username.text()
        password = self.line_edit_password.text()
        secure_password = hashlib.sha1(str(password).encode())
        password = secure_password.hexdigest()
        if user_name == "" and self.line_edit_password.text() == "":
            self.error_report(str("Please enter your username and password!"))
        elif user_name == "":
            self.error_report(str("Please enter your username!"))
        elif self.line_edit_password.text() == "":
            self.error_report(str("Please enter your password!"))
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            user_id_query = "SELECT userid FROM userdatabase where userid = " + user_name + " and pass = " + password
            db_cursor.execute(user_id_query)
            user_id_result = db_cursor.fetchone()
            if user_id_result is None:
                self.error_report(str("Username or password does not match!"))
            elif user_id_result[0] == "Admin":
                self.info_report(str("admin account"))
                self.win_admin_panel = QtWidgets.QWidget()
                self.ui = AdminPanel(login_object)
                self.ui.setup_ui(self.win_admin_panel)
                login_object.hide()
                self.line_edit_username.clear()
                self.line_edit_password.clear()
                self.win_admin_panel.show()
            else:
                self.info_report(str("Teacher account"))
                self.win_dashboard = QtWidgets.QWidget()
                self.ui = Dashboard(user_name, login_object)
                self.ui.setup_ui(self.win_dashboard)
                login_object.hide()
                self.line_edit_username.clear()
                self.line_edit_password.clear()
                self.win_dashboard.show()

        except mysql.connector.Error as e:
            self.error_report(str("Server not responding! Please make sure college database server is working."))
            print(e.errno)
            print(e.sqlstate)
            print("Failed to insert into MySQL table {}".format(e))

    def signup(self, login_object):
        self.win_signup = QtWidgets.QWidget()
        self.ui = Signup(login_object)
        self.ui.setup_ui(self.win_signup)
        login_object.hide()
        self.win_signup.show()

    @staticmethod
    def error_report(message):
        message_box = QtWidgets.QMessageBox()
        ui = ErrorMessage(message)
        ui.setup_ui(message_box)

    @staticmethod
    def info_report(message):
        message_box = QtWidgets.QMessageBox()
        ui = Info(message)
        ui.setup_ui(message_box)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_object = QtWidgets.QMainWindow()
    login = Login()
    login.setup_ui(login_object)
    login_object.show()
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
