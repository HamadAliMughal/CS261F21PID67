#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import pandas as pd
class MyThread(QThread):
    change_val = pyqtSignal(int)
    def run(self):
        count = 0
        while count<101:
            count+=1
            time.sleep(0.3)
            self.change_val.emit(count)
class Ui_MainWindow(object): 
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 648)
        MainWindow.setStyleSheet("background-color: rgb(242, 200, 17);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(290, -10, 841, 691))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(242, 200, 17);\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(30, 100, 771, 81))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 30px;")
        self.widget.setObjectName("widget")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(70, 20, 501, 41))
        self.progressBar.setStyleSheet("background-color: rgb(171, 171, 171);\n"
"border-radius: 30px;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setProperty("format","DataScraped %p%")
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(590, 20, 41, 41))
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(640, 20, 41, 41))
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(690, 20, 41, 41))
        self.label_11.setObjectName("label_11")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(30, 210, 771, 371))
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 30px;")
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 551, 41))
        self.lineEdit.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 251, 233);\n"
"border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(540, 10, 21, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 251, 233);")
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 731, 281))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(999584)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_3.setGeometry(QtCore.QRect(580, 10, 171, 41))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 251, 233);\n"
"font: 10pt \"Arial\";\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 291, 711))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.0227273, y2:0.017, stop:0 rgba(209, 209, 0, 255), stop:0.954545 rgba(0, 0, 0, 254));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 30, 191, 81))
        self.label.setStyleSheet("color: rgb(255, 251, 233);\n"
"font: 87 48pt \"Arial Black\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(-10, 130, 271, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 251, 233);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(60, 370, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(-20, 190, 281, 191))
        self.label_7.setStyleSheet("background-color: rgb(255, 251, 233);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(-20, 390, 281, 191))
        self.label_8.setStyleSheet("background-color: rgb(255, 251, 233);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(-10, 210, 131, 131))
        self.label_9.setStyleSheet("border-radius: 10px;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(-10, 410, 131, 131))
        self.label_10.setStyleSheet("border-radius: 10px;")
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(140, 240, 91, 31))
        self.label_13.setStyleSheet("\n"
"background-color: rgb(255, 251, 233);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(140, 270, 91, 31))
        self.label_14.setStyleSheet("\n"
"background-color: rgb(255, 251, 233);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(150, 440, 91, 31))
        self.label_15.setStyleSheet("\n"
"background-color: rgb(255, 251, 233);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(140, 470, 91, 21))
        self.label_16.setStyleSheet("\n"
"background-color: rgb(255, 251, 233);")
        self.label_16.setObjectName("label_16")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(0, 350, 121, 22))
        self.comboBox.setStyleSheet("color :rgb(242, 200, 17)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(0, 550, 121, 22))
        self.comboBox_2.setStyleSheet("color: rgb(242, 200, 17);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #self.loadDatatoTable()
        #self.label_9.clicked.connect(self.sorting)
        self.label_9.mousePressEvent = self.sortSelect
        self.label_10.mousePressEvent = self.sortAttribute
        self.label_5.mousePressEvent = self.searchTable
        self.label_6.mousePressEvent = self.startProgressBar
    def setProgressBar(self,var):
        self.progressBar.setValue(var)
    def startProgressBar(self,event):
        self.loadData()
        self.thread = MyThread()
        self.thread.change_val.connect(self.setProgressBar)
        self.thread.start()
        
    def loadData(self):
        row = 0
        Rating=[]
        Cast=[]
        Director=[]
        Title=[]
        Year=[]
        Type=[]
        Duration=[]
        print("clicked done")
        listt = pd.read_csv('C:\\MoviesAndMunchingg.csv')
        print("Data load in variavle from csv")
        for i in range(len(listt)):
            Title.append(str(listt["Title"][i]))
            Rating.append(str(listt["Rating"][i]))
            Type.append(str(listt["Type"][i]))
            Duration.append(str(listt["Duration"][i]))
            Year.append(str(listt["Release Year"][i]))
            Director.append(str(listt["Director"][i]))
            Cast.append(str(listt["Cast/Star"][i]))
        
        print("Data stored in array now going to print in table")
        for i in range(len(Title)):
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(Title[i]))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(Rating[i]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(Type[i]))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(Duration[i]))
            self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(Year[i]))
            self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(Director[i]))
            self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(Cast[i]))
            row= row+1
    def sortSelect(self,event):
        algo=self.comboBox.currentText()
        if(algo=="Selection Sort"):
            self.selectionSort()
        elif(algo=="Merge Sort"):
            self.mergeSort()
            
    def sortAttribute(self,event):
        attr=self.comboBox_2.currentText()
        print(attr)
        
    def searchTable(self,event):
        entity=self.comboBox_3.currentText()  
        key=self.lineEdit.text()
        print(entity)
        print(key)
        
        
    def mergeSort(self):
        print("Merge")
        
    def selectionSort(self):
        print("Select")
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/Progr.png\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/start.png\"/></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/pause.png\"/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/stop.png\"/></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "   Search"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/icons8_search_24px.png\"/></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Movie Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Movie Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Release Year"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Director"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cast/Actor"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Movie Title"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Rating"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>M&amp;M</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Movies and Munching</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/Algo.png\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/front_sorting_120px.png\"/></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Selecting</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Algorithm</span></p><p><br/></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Sorting</span></p><p><br/></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Attributes</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Selection Sort"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Merge Sort"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Alphabetically Ascending"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Alphabetically Descending"))
        
import logos

        
if __name__ == "__main__":
    import sys
    import pandas as pd
    import csv
    #Lists for containing data 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    


# In[ ]:





# In[ ]:



