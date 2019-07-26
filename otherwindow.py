# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\Desktop\otherwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db import readdbEntity


class Ui_otherwindow(object):

    def setupUi(self, otherwindow):
        otherwindow.setObjectName("otherwindow")
        otherwindow.resize(665, 394)
        self.centralwidget = QtWidgets.QWidget(otherwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 645, 354))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 625, 254))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(otherwindow.close)

        self.verticalLayout_2.addWidget(self.pushButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        otherwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(otherwindow)
        self.statusbar.setObjectName("statusbar")
        otherwindow.setStatusBar(self.statusbar)

        self.retranslateUi(otherwindow)
        QtCore.QMetaObject.connectSlotsByName(otherwindow)

    def retranslateUi(self, otherwindow):
        _translate = QtCore.QCoreApplication.translate
        otherwindow.setWindowTitle(_translate("otherwindow", "MainWindow"))
        self.label_3.setText(_translate("otherwindow", "ENTITY    RELATION    ENTITY"))
        self.label.setText(_translate("otherwindow", readdbEntity()))
        self.pushButton.setText(_translate("otherwindow", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otherwindow = QtWidgets.QMainWindow()
    ui = Ui_otherwindow()
    ui.setupUi(otherwindow)
    otherwindow.show()
    sys.exit(app.exec_())

