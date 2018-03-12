# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layouts/main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 640)
        MainWindow.setStyleSheet("#centralwidget {\n"
"    border-top: 6px solid #5dcd11;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget {\n"
"    border: 0px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    border-right: 1px solid #DDD;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("padding-top: 6px;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setStyleSheet("")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setStyleSheet("margin: 10px;\n"
"background-color: rgb(242, 242, 242);\n"
"padding: 4px;\n"
"border-radius: 6px;")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.users = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.users.setEnabled(True)
        self.users.setObjectName("users")
        self.verticalLayout.addWidget(self.users)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.userLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.userLabel.setStyleSheet("font-weight: bold;\n"
"margin: 10px;")
        self.userLabel.setScaledContents(False)
        self.userLabel.setObjectName("userLabel")
        self.verticalLayout_2.addWidget(self.userLabel)
        self.messages = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.messages.setStyleSheet("#messages {\n"
"    background-color: rgb(223, 229, 219);\n"
"}\n"
"\n"
"QWidget#message {\n"
"    background-color: white;\n"
"    border: 1px solid #DDD;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QWidget#ownMessage {\n"
"    background-color: #59c817;\n"
"    color: white;\n"
"    border: 1px solid #DDD;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QWidget#message QLabel {\n"
"    font: 12px;\n"
"}\n"
"\n"
"QWidget#ownMessage QLabel {\n"
"    color: white;\n"
"    font: 12px;\n"
"}\n"
"\n"
"QLabel#nameLabel {\n"
"    font: bold;\n"
"}\n"
"")
        self.messages.setObjectName("messages")
        self.verticalLayout_2.addWidget(self.messages)
        self.messageEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.messageEdit.setStyleSheet("padding: 8px;\n"
"font-size: 14px;")
        self.messageEdit.setObjectName("messageEdit")
        self.verticalLayout_2.addWidget(self.messageEdit)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Search"))
        self.userLabel.setText(_translate("MainWindow", "Username"))
        self.messageEdit.setPlaceholderText(_translate("MainWindow", "Write a message..."))
