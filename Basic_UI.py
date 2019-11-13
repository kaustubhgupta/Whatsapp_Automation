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
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 90, 721, 372))
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
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
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
        self.pushButton_2.clicked.connect(self.plainTextEdit_3.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_2.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Name of user"))
        self.label_2.setText(_translate("MainWindow", "Enter your message"))
        self.label_3.setText(_translate("MainWindow", "Enter count of messages"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.label_4.setText(_translate("MainWindow", "WhatsApp Automated message sender"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

