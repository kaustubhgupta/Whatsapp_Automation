# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Basic UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 90, 721, 400))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameval = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.nameval.setObjectName("nameval")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameval)
        self.messageval = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.messageval.setObjectName("messageval")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.messageval)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.countval = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.countval.setObjectName("countval")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.countval)
        self.sendbtn = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sendbtn.setFont(font)
        self.sendbtn.setObjectName("sendbtn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sendbtn)
        self.resetbtn = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.resetbtn.setFont(font)
        self.resetbtn.setObjectName("resetbtn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.resetbtn)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, -5, 731, 91))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(26)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.resetbtn.clicked.connect(self.countval.clear)
        self.resetbtn.clicked.connect(self.messageval.clear)
        self.resetbtn.clicked.connect(self.nameval.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Name of user"))
        self.label_3.setText(_translate("MainWindow", "Enter count of messages"))
        self.sendbtn.setText(_translate("MainWindow", "Send"))
        self.resetbtn.setText(_translate("MainWindow", "Reset"))
        self.label_2.setText(_translate("MainWindow", "Enter your message"))
        self.label_4.setText(_translate("MainWindow", "WhatsApp Automated message sender"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

