from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 680)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 110, 181, 181))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/arsenal-logo-32046.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 300, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 120, 181, 181))
        self.label_3.setStyleSheet("image: url(:/newPrefix/pngwing.com (7).png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 310, 291, 41))
        self.comboBox.setStyleSheet("background-color: rgb(255, 170, 127,100);")
        self.comboBox.setEditable(True)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-30, 250, 691, 411))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:25;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(350, 480, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setAutoFillBackground(False)
        self.dateTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setCalendarPopup(False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 430, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 170, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 460, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:25;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 540, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:25;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.dateTimeEdit.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.openMain)
        # self.pushButton_2.clicked.connect(self.addRival)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Arsenal"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Astan Villa"))
        self.label_5.setText(_translate("MainWindow", "Kick off"))
        self.label_6.setText(_translate("MainWindow", "VS"))
        self.label_7.setText(_translate("MainWindow", "ADD Match"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton_2.setText(_translate("MainWindow", "CANCEL"))


    def openMain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

#     def addRival(self):
#         rival=self.comboBox.currentText()
#         self.pushButton_2.setText(str(rival))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
