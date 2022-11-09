from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import main
import dbms

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 579)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logintxt = QtWidgets.QLabel(self.centralwidget)
        self.logintxt.setGeometry(QtCore.QRect(240, 10, 251, 141))
        self.logintxt.setStyleSheet("font: 48pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.logintxt.setObjectName("logintxt")
        self.userbox = QtWidgets.QLineEdit(self.centralwidget)
        self.userbox.setGeometry(QtCore.QRect(280, 200, 311, 71))
        self.userbox.setStyleSheet("font: 30pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.userbox.setObjectName("userbox")
        self.usertxt = QtWidgets.QLabel(self.centralwidget)
        self.usertxt.setGeometry(QtCore.QRect(30, 200, 201, 71))
        self.usertxt.setStyleSheet("font: 20pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.usertxt.setObjectName("usertxt")
        self.passtext = QtWidgets.QLabel(self.centralwidget)
        self.passtext.setGeometry(QtCore.QRect(30, 330, 201, 71))
        self.passtext.setStyleSheet("font: 20pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.passtext.setObjectName("passtext")
        self.passbox = QtWidgets.QLineEdit(self.centralwidget)
        self.passbox.setGeometry(QtCore.QRect(280, 330, 311, 71))
        self.passbox.setStyleSheet("font: 30pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.passbox.setObjectName("passbox")
        self.loginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(250, 450, 201, 41))
        self.loginbtn.setStyleSheet("font: 20pt \"OCR A Extended\";\n"
"background-color: rgb(85, 255, 127);")
        self.loginbtn.setObjectName("loginbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logintxt.setText(_translate("MainWindow", "Login"))
        self.usertxt.setText(_translate("MainWindow", "Username :"))
        self.passtext.setText(_translate("MainWindow", "Password :"))
        self.loginbtn.setText(_translate("MainWindow", "Login"))
        self.loginbtn.clicked.connect(self.callDatabase)


    def callDatabase(self):
        
        username = self.userbox.text()
        passsword = self.passbox.text()
        try:
          sqlConnection = pymysql.connect(host="localhost", database="cslproject", user=username, password=passsword)
        
        except pymysql.err.OperationalError as e:
                print("Error %d: %s" % (e.args[0], e.args[1]))
                if(e.args[0]==1045):
                    print("Invalid username or password")
                elif(e.args[0]==1049):
                    print("Database not found")
                elif(e.args[0]==2003):
                    print("Server not found")
                elif(e.args[0]==2005):
                    print("Unknown host")
                elif(e.args[0]==2006):
                    print("Server has gone away")
                elif(e.args[0]==2013):
                    print("Lost connection to MySQL server during query")
                elif(e.args[0]==2019):
                    print("Access denied for user")
                elif(e.args[0]==2026):
                    print("Too many connections")
        else:
            print("Connection successful")
            self.openHomepage()
            sqlConnection.close()

    def openHomepage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        closeWindows()

def closeWindows():
    MainWindow.close()

def openHomepage2():
    Dialog2 = QtWidgets.QDialog()
    ui = main.Ui_uiHomePage()
    ui.setupUi(Dialog2)
    Dialog2.show()
    Dialog2.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
