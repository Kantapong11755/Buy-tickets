from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 895)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/python/pic/Football_(soccer_ball).svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(213, 219, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1080, 20, 351, 101))
        self.label.setStyleSheet("font: 50pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255,0);")
        self.label.setObjectName("label")
        self.zonecbb = QtWidgets.QComboBox(self.centralwidget)
        self.zonecbb.setGeometry(QtCore.QRect(1140, 420, 141, 51))
        self.zonecbb.setStyleSheet("font: 20pt \"2005_iannnnnGMO\";\n"
"background-color: rgb(255, 255, 255);")
        self.zonecbb.setObjectName("zonecbb")
        self.zonecbb.addItem("")
        self.zonecbb.setItemText(0, "")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.zonecbb.addItem("")
        self.totalfix = QtWidgets.QLabel(self.centralwidget)
        self.totalfix.setGeometry(QtCore.QRect(1000, 640, 461, 81))
        self.totalfix.setStyleSheet("font: 30pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.totalfix.setObjectName("totalfix")
        self.Confirmbtm = QtWidgets.QPushButton(self.centralwidget)
        self.Confirmbtm.setGeometry(QtCore.QRect(1130, 740, 193, 48))
        self.Confirmbtm.setStyleSheet("font: 22pt \"OCR A Extended\";\n"
"background-color: rgb(67, 255, 34);")
        self.Confirmbtm.setObjectName("Confirmbtm")
        self.seatimg = QtWidgets.QLabel(self.centralwidget)
        self.seatimg.setGeometry(QtCore.QRect(20, 110, 891, 621))
        self.seatimg.setStyleSheet("background-color: rgb(0, 115, 255);")
        self.seatimg.setText("")
        self.seatimg.setPixmap(QtGui.QPixmap("image\Football_(soccer_ball).svg.png"))
        self.seatimg.setScaledContents(True)
        self.seatimg.setObjectName("seatimg")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(930, 240, 182, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Nameclm = QtWidgets.QLabel(self.layoutWidget)
        self.Nameclm.setStyleSheet("font: 20pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255,0);")
        self.Nameclm.setObjectName("Nameclm")
        self.verticalLayout.addWidget(self.Nameclm)
        self.Telclm = QtWidgets.QLabel(self.layoutWidget)
        self.Telclm.setStyleSheet("font: 20pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255,0);")
        self.Telclm.setObjectName("Telclm")
        self.verticalLayout.addWidget(self.Telclm)
        self.Zoneclm = QtWidgets.QLabel(self.layoutWidget)
        self.Zoneclm.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255,0);")
        self.Zoneclm.setObjectName("Zoneclm")
        self.verticalLayout.addWidget(self.Zoneclm)
        self.Quanclm = QtWidgets.QLabel(self.layoutWidget)
        self.Quanclm.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255,0);")
        self.Quanclm.setObjectName("Quanclm")
        self.verticalLayout.addWidget(self.Quanclm)
        self.quantitycbb = QtWidgets.QComboBox(self.centralwidget)
        self.quantitycbb.setGeometry(QtCore.QRect(1140, 510, 141, 51))
        self.quantitycbb.setStyleSheet("font: 20pt \"2005_iannnnnGMO\";\n"
"background-color: rgb(255, 255, 255);")
        self.quantitycbb.setObjectName("quantitycbb")
        self.quantitycbb.addItem("")
        self.quantitycbb.setItemText(0, "")
        self.quantitycbb.addItem("")
        self.quantitycbb.addItem("")
        self.quantitycbb.addItem("")
        self.quantitycbb.addItem("")
        self.calculatebtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculatebtn.setGeometry(QtCore.QRect(1140, 600, 171, 31))
        self.calculatebtn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.calculatebtn.setObjectName("calculatebtn")
        self.NameTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.NameTextbox.setGeometry(QtCore.QRect(1140, 240, 371, 61))
        self.NameTextbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"OCR A Extended\";")
        self.NameTextbox.setObjectName("NameTextbox")
        self.TelTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.TelTextbox.setGeometry(QtCore.QRect(1140, 330, 371, 61))
        self.TelTextbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 22pt \"2005_iannnnnGMO\";")
        self.TelTextbox.setObjectName("TelTextbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1550, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tickets"))
        self.label.setText(_translate("MainWindow", "TICKETS"))
        self.zonecbb.setItemText(1, _translate("MainWindow", "N1/1000"))
        self.zonecbb.setItemText(2, _translate("MainWindow", "N2/1000"))
        self.zonecbb.setItemText(3, _translate("MainWindow", "N3/1000"))
        self.zonecbb.setItemText(4, _translate("MainWindow", "N4/1000"))
        self.zonecbb.setItemText(5, _translate("MainWindow", "S1/1000"))
        self.zonecbb.setItemText(6, _translate("MainWindow", "S2/1000"))
        self.zonecbb.setItemText(7, _translate("MainWindow", "S3/1000"))
        self.zonecbb.setItemText(8, _translate("MainWindow", "S4/1000"))
        self.zonecbb.setItemText(9, _translate("MainWindow", "E1/500"))
        self.zonecbb.setItemText(10, _translate("MainWindow", "E2/500"))
        self.zonecbb.setItemText(11, _translate("MainWindow", "E3/500"))
        self.zonecbb.setItemText(12, _translate("MainWindow", "E4/500"))
        self.zonecbb.setItemText(13, _translate("MainWindow", "W1/500"))
        self.zonecbb.setItemText(14, _translate("MainWindow", "W2/500"))
        self.zonecbb.setItemText(15, _translate("MainWindow", "W3/500"))
        self.zonecbb.setItemText(16, _translate("MainWindow", "W4/500"))
        self.zonecbb.setItemText(17, _translate("MainWindow", "NE/250"))
        self.zonecbb.setItemText(18, _translate("MainWindow", "NW/250"))
        self.zonecbb.setItemText(19, _translate("MainWindow", "SW/250"))
        self.zonecbb.setItemText(20, _translate("MainWindow", "SE/250"))
        self.totalfix.setText(_translate("MainWindow", "TOTAL 0.00 BAHT"))
        self.Confirmbtm.setText(_translate("MainWindow", "CONFIRM"))
        self.Nameclm.setText(_translate("MainWindow", "NAME :"))
        self.Telclm.setText(_translate("MainWindow", "TEL :"))
        self.Zoneclm.setText(_translate("MainWindow", "Zone :"))
        self.Quanclm.setText(_translate("MainWindow", "Quantity :"))
        self.quantitycbb.setItemText(1, _translate("MainWindow", "1"))
        self.quantitycbb.setItemText(2, _translate("MainWindow", "2"))
        self.quantitycbb.setItemText(3, _translate("MainWindow", "3"))
        self.quantitycbb.setItemText(4, _translate("MainWindow", "4"))
        self.calculatebtn.setText(_translate("MainWindow", "CALCULATE"))
        self.calculatebtn.clicked.connect(self.addprice)
        self.Confirmbtm.clicked.connect(self.insertDatabase)
        self.Confirmbtm.clicked.connect(self.goMain)


    def addprice(self) :
        price=int(self.zonecbb.currentText().split("/")[1].strip())
        quantity=int(self.quantitycbb.currentText())
        total=price*quantity
        self.totalfix.setText("TOTAL "+str(total)+" BAHT")
    
    def goMain(self) :
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def insertDatabase(self):
        Name = self.NameTextbox.text()
        Tel = self.TelTextbox.text()
        Zone = self.zonecbb.currentText().split("/")[0].strip()
        Quantity = self.quantitycbb.currentText()
        price=int(self.zonecbb.currentText().split("/")[1].strip())
        quantity=int(self.quantitycbb.currentText())
        total=price*quantity

        if (Name == '' or Tel == ''):
            print("Please fill all data")
        else:
            con = pymysql.connect(host="localhost", database="cslproject",user="root", password="")
            cursor = con.cursor()
            cursor.execute("INSERT INTO customer (Name, Tel, Zone, Quantity, Price) VALUES (%s, %s, %s, %s,%s)",
                           (Name, Tel, Zone, Quantity, total))
            con.commit()
            self.NameTextbox.setText("")
            self.TelTextbox.setText("")
            self.zonecbb.setCurrentText("")
            self.quantitycbb.setCurrentText("")
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())