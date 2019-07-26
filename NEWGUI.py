# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\Desktop\NEWGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from error import Ui_Dialog
from otherwindow import Ui_otherwindow
from db import addEntity, deleteEntity, readdbEntity, search

class Ui_MainWindow(object):
    def opendialog(self):
        self.dialog = QtWidgets.QDialog()
        self.uid = Ui_Dialog()
        self.uid.setupUi(self.dialog)
        self.dialog.show()


    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_otherwindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 600, 282))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 4, 2, 2, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 4, 3, 2, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 4, 4, 2, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)

        self.pushButton_3.setObjectName("pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 6, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)

        self.pushButton.setObjectName("pushButton")



        self.pushButton.clicked.connect(self.openwindow)

        self.gridLayout_2.addWidget(self.pushButton, 6, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("ADD")



        self.gridLayout_2.addWidget(self.pushButton_2, 6, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_2.clicked.connect(self.btnadd)

        self.pushButton_3.clicked.connect(self.btndel)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Main Window"))
        self.label_3.setText(_translate("MainWindow", "WHAT??"))
        self.label.setText(_translate("MainWindow", "HOW??"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "ENTITY1"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "RELATION"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "ENTITY2"))
        self.pushButton_3.setText(_translate("MainWindow", "DELETE"))
        self.pushButton.setText(_translate("MainWindow", "VIEW"))
        self.pushButton_2.setText(_translate("MainWindow", "ADD"))
        self.label_4.setText(_translate("MainWindow", "WHO??"))

    def btnadd(self):
        relation = self.lineEdit.text()
        entity1 = self.lineEdit_2.text()
        entity2 = self.lineEdit_3.text()
        if(len(relation)>0 and len(entity1)>0 and len(entity2)>0):
            self.lineEdit_3.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            print(entity1, relation, entity2)
            addEntity(entity1,entity2,relation)
        else:
            self.lineEdit_3.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.opendialog()



    def btndel(self):
        relation = self.lineEdit.text()
        entity1 = self.lineEdit_2.text()
        entity2 = self.lineEdit_3.text()
        if (len(relation) > 0 and len(entity1) > 0 and len(entity2) > 0):
            self.lineEdit_3.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            print(entity1, relation, entity2)
            deleteEntity(entity1,entity2,relation)
        else:
            self.lineEdit_3.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.opendialog()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

