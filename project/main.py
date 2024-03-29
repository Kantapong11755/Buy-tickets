from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import ticket
import addmatch
import aboutus

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 895)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setBaseSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 127);")
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 501, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 200);\n"
"border-radius:20;\n"
"\n"
"\n"
"")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(0)
        self.label_2.setMidLineWidth(0)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 160, 501, 301))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 200);\n"
"border-radius:5;\n"
"border-color: beige;\n"
"border-style: outset;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 510, 501, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        #self.label_5.setFont(font)
        #self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        #self.label_5.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        #self.label_5.setAutoFillBackground(False)
        #self.label_5.setStyleSheet("background-color: rgb(255, 170, 127,250);\n"
#"border-radius:15;\n"
#"\n"
#"\n"
#"")
        #self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
       #self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        #self.label_5.setLineWidth(0)
        #self.label_5.setMidLineWidth(0)
        #self.label_5.setTextFormat(QtCore.Qt.PlainText)
        #self.label_5.setScaledContents(True)
       #self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
       #self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 500, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127,250);\n"
"border-style: outset;\n"
"border-radius: 20;\n"
"border-shadow: 2;")
        self.pushButton.setShortcut("")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 750, 200, 65))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setTabletTracking(False)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-style: outset;\n"
"border-radius: 15;\n"
"border-width: 5;\n"
"border-color: beige;")
        self.pushButton_2.setShortcut("")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 200, 181, 161))
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/newPrefix/arsenal-logo-32046.png);\n"
"border-radius:5;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("image/1.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(420, 220, 191, 181))
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/newPrefix/logo-manchester-united-png-13500.png);\n"
"border-radius:5;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(90, 420, 601, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_23.setFont(font)
        self.label_23.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_23.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_23.setAutoFillBackground(False)
        self.label_23.setStyleSheet("background-color: rgba(255, 255, 255, 250);\n"
"border-radius:70;\n"
"\n"
"\n"
"")
        self.label_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_23.setLineWidth(0)
        self.label_23.setMidLineWidth(0)
        self.label_23.setText("")
        self.label_23.setTextFormat(QtCore.Qt.PlainText)
        self.label_23.setScaledContents(False)
        self.label_23.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(690, 80, 851, 791))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_25.setFont(font)
        self.label_25.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_25.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet("background-color: rgba(255, 255, 255, 250);\n"
"border-radius:70;\n"
"\n"
"\n"
"")
        self.label_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_25.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_25.setLineWidth(0)
        self.label_25.setMidLineWidth(0)
        self.label_25.setText("")
        self.label_25.setTextFormat(QtCore.Qt.PlainText)
        self.label_25.setScaledContents(False)
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_25.setObjectName("label_25")
        self.deletebtn = QtWidgets.QPushButton(self.centralwidget)
        self.deletebtn.setGeometry(QtCore.QRect(820, 770, 161, 41))
        self.deletebtn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(255, 0, 0);")
        self.deletebtn.setObjectName("deletebtn")
        self.refreshbtn = QtWidgets.QPushButton(self.centralwidget)
        self.refreshbtn.setGeometry(QtCore.QRect(1260, 770, 151, 41))
        self.refreshbtn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(195, 195, 195);")
        self.refreshbtn.setObjectName("refreshbtn")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1020, 10, 341, 61))
        self.label_13.setStyleSheet("font: 40pt \"OCR A Extended\";")
        self.label_13.setObjectName("label_13")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(710, 360, 811, 381))
        self.tableWidget.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.idtxt = QtWidgets.QLabel(self.centralwidget)
        self.idtxt.setGeometry(QtCore.QRect(770, 120, 91, 31))
        self.idtxt.setStyleSheet("font: 20pt \"OCR A Extended\";")
        self.idtxt.setObjectName("idtxt")
        self.searchbtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchbtn.setGeometry(QtCore.QRect(1020, 120, 101, 31))
        self.searchbtn.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.searchbtn.setObjectName("searchbtn")
        self.nametxt = QtWidgets.QLabel(self.centralwidget)
        self.nametxt.setGeometry(QtCore.QRect(770, 200, 121, 31))
        self.nametxt.setStyleSheet("font: 20pt \"OCR A Extended\";")
        self.nametxt.setObjectName("nametxt")
        self.teltxt = QtWidgets.QLabel(self.centralwidget)
        self.teltxt.setGeometry(QtCore.QRect(770, 270, 111, 31))
        self.teltxt.setStyleSheet("font: 20pt \"OCR A Extended\";")
        self.teltxt.setObjectName("teltxt")
        self.zonetxt = QtWidgets.QLabel(self.centralwidget)
        self.zonetxt.setGeometry(QtCore.QRect(1210, 130, 121, 31))
        self.zonetxt.setStyleSheet("font: 20pt \"OCR A Extended\";")
        self.zonetxt.setObjectName("zonetxt")
        self.quantitytxt = QtWidgets.QLabel(self.centralwidget)
        self.quantitytxt.setGeometry(QtCore.QRect(1210, 200, 121, 31))
        self.quantitytxt.setStyleSheet("font: 12pt \"OCR A Extended\";")
        self.quantitytxt.setObjectName("quantitytxt")
        self.pricetxt = QtWidgets.QLabel(self.centralwidget)
        self.pricetxt.setGeometry(QtCore.QRect(1210, 270, 111, 31))
        self.pricetxt.setStyleSheet("font: 15pt \"OCR A Extended\";")
        self.pricetxt.setObjectName("pricetxt")
        self.editbtn = QtWidgets.QPushButton(self.centralwidget)
        self.editbtn.setGeometry(QtCore.QRect(1040, 770, 161, 41))
        self.editbtn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(255,221,51);")
        self.editbtn.setObjectName("editbtn")
        self.idbox = QtWidgets.QLineEdit(self.centralwidget)
        self.idbox.setGeometry(QtCore.QRect(880, 110, 113, 51))
        self.idbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idbox.setObjectName("idbox")
        self.namebox = QtWidgets.QLineEdit(self.centralwidget)
        self.namebox.setGeometry(QtCore.QRect(910, 190, 251, 51))
        self.namebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.namebox.setObjectName("namebox")
        self.telbox = QtWidgets.QLineEdit(self.centralwidget)
        self.telbox.setGeometry(QtCore.QRect(910, 260, 251, 51))
        self.telbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.telbox.setObjectName("telbox")
        self.zonebox = QtWidgets.QLineEdit(self.centralwidget)
        self.zonebox.setGeometry(QtCore.QRect(1350, 120, 131, 51))
        self.zonebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.zonebox.setObjectName("zonebox")
        self.quantitybox = QtWidgets.QLineEdit(self.centralwidget)
        self.quantitybox.setGeometry(QtCore.QRect(1350, 190, 131, 51))
        self.quantitybox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quantitybox.setObjectName("quantitybox")
        self.pricebox = QtWidgets.QLineEdit(self.centralwidget)
        self.pricebox.setGeometry(QtCore.QRect(1350, 260, 131, 51))
        self.pricebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pricebox.setObjectName("pricebox")
        self.label_25.raise_()
        self.label_23.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        #self.label_5.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        #self.comboBox.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.deletebtn.raise_()
        self.refreshbtn.raise_()
        self.label_13.raise_()
        self.tableWidget.raise_()
        self.idtxt.raise_()
        self.searchbtn.raise_()
        self.nametxt.raise_()
        self.teltxt.raise_()
        self.zonetxt.raise_()
        self.quantitytxt.raise_()
        self.pricetxt.raise_()
        self.editbtn.raise_()
        self.idbox.raise_()
        self.namebox.raise_()
        self.telbox.raise_()
        self.zonebox.raise_()
        self.quantitybox.raise_()
        self.pricebox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
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
        self.label_2.setText(_translate("MainWindow", "MATCH DAY"))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        #self.label_5.setText(_translate("MainWindow", "Choose match"))
        self.pushButton.setText(_translate("MainWindow", "Buy Tickets"))
        self.pushButton_2.setText(_translate("MainWindow", "About Us"))
        self.label_23.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_25.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.deletebtn.setText(_translate("MainWindow", "DELETE"))
        self.refreshbtn.setText(_translate("MainWindow", "REFRESH"))
        self.label_13.setText(_translate("MainWindow", "CUSTOMER"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tel"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Zone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Price"))
        self.idtxt.setText(_translate("MainWindow", "ID :"))
        self.searchbtn.setText(_translate("MainWindow", "SEARCH"))
        self.nametxt.setText(_translate("MainWindow", "Name :"))
        self.teltxt.setText(_translate("MainWindow", "Tel :"))
        self.zonetxt.setText(_translate("MainWindow", "Zone :"))
        self.quantitytxt.setText(_translate("MainWindow", "Quantity :"))
        self.pricetxt.setText(_translate("MainWindow", "Price :"))
        self.editbtn.setText(_translate("MainWindow", "EDIT"))
        self.refreshbtn.clicked.connect(self.refresh)
        self.pushButton.clicked.connect(self.openTicket)
        self.pushButton_2.clicked.connect(self.openAddMatch)
        self.deletebtn.clicked.connect(self.removeDatabase)
        self.editbtn.clicked.connect(self.editDatabase)
        self.searchbtn.clicked.connect(self.fecthID)


    def fecthID(self):
        global ID
        ID = self.idbox.text()
        if ID == "":
            print("กรุณาใส่ไอดี") 
        else:
            self.checkID()
    
    def checkID(self):
        global ID
        con = pymysql.connect(host="localhost", database="cslproject",
                              user="root", password="")
        cursor = con.cursor()
        cursor.execute(
            "SELECT Name FROM customer WHERE ID = %s", ID)
        Name = cursor.fetchone()
        if Name == None:
            self.idbox.setText("ไม่พบชื่อเมนู")
            self.namebox.setText("ไม่พบชื่อเมนู")
            self.telbox.setText("ไม่พบชื่อเมนู")
            self.zonebox.setText("ไม่พบชื่อเมนู")
            self.quantitybox.setText("ไม่พบชื่อเมนู")
            print("ไม่พบไอดีเมนู")
        else:
            self.fetchDatabase()
    
    def fetchDatabase(self):                                             
        print('fetching database')
        con = pymysql.connect(host="localhost", database="cslproject",
                              user='root', password='')
        cursor = con.cursor()
        cursor.execute("SELECT Name FROM customer WHERE ID = %s", ID)
        Name = cursor.fetchone()
        cursor.execute("SELECT Tel FROM customer WHERE ID = %s", ID)
        Tel = cursor.fetchone()
        cursor.execute("SELECT Zone FROM customer WHERE ID = %s", ID)
        Zone = cursor.fetchone()
        cursor.execute("SELECT Quantity FROM customer WHERE ID = %s", ID)
        Quantity = cursor.fetchone()
        cursor.execute("SELECT Price FROM customer WHERE ID = %s", ID)
        Price = cursor.fetchone()
        self.namebox.setText(Name[0])
        self.telbox.setText(Tel[0])
        self.zonebox.setText(Zone[0])
        self.quantitybox.setText(str(Quantity[0]))
        self.pricebox.setText(str(Price[0]))
        con.close()
    
    def editDatabase(self):        
         name = self.namebox.text()
         tel = self.telbox.text()
         zone = self.zonebox.text()
         quantity = self.quantitybox.text()
         price = self.pricebox.text()

         if (name == '' or tel == '' or zone == '' or quantity == '' or price == ''):
            print("Please fill all data")
         else:
            con = pymysql.connect(host="localhost", database="cslproject",
                                  user='root', password='')
            cursor = con.cursor()
            cursor.execute("UPDATE customer SET Name=%s, Tel=%s, Zone=%s, Quantity=%s, Price=%s WHERE ID = %s" ,
                           (name, tel, zone,quantity,price,ID))
            print("Edit data successfully")
            con.commit()

    def refresh(self):
        print('refresh data')
        self.tableWidget.setRowCount(0)
        con = pymysql.connect(host="localhost", database="cslproject",
                                  user="root", password="")
        cursor = con.cursor()
        cursor.execute("SELECT ID,Name,Tel,Zone,Quantity,Price FROM customer")
        data = list(cursor.fetchall())
        tablerow = 0
        for i in data:
            self.tableWidget.insertRow(tablerow)
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(i[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(i[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(i[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(i[5]))
            tablerow += 1
    
    def removeDatabase(self):                                            #ลบตาราง
        global ID
        ID = self.idbox.text()
        if (ID == ''):
            print("Please fill ID")
        else:
            con = pymysql.connect(host="localhost", database="cslproject",
                                  user='root', password='')
            cursor = con.cursor()
            check = cursor.execute("SELECT ID FROM customer WHERE ID  = %s", ID )
            if check == 0:
                print('ไม่พบข้อมูล')
            else:
                cursor.execute("DELETE FROM customer WHERE ID  = %s", ID )
                con.commit()
                self.idbox.setText("")
                self.namebox.setText("")
                self.telbox.setText("")
                self.zonebox.setText("")
                self.quantitybox.setText("")
                self.pricebox.setText("")
                con.close()

    def openTicket(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ticket.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        self.window = QtWidgets.QMainWindow()
        self.ui = ticket.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAddMatch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = aboutus.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
