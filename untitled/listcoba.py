# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list coba.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.lstTest = QtWidgets.QListView(Dialog)
        self.lstTest.setGeometry(QtCore.QRect(80, 40, 256, 192))
        self.lstTest.setObjectName("lstTest")
        self.btnProcess = QtWidgets.QPushButton(Dialog)
        self.btnProcess.setGeometry(QtCore.QRect(170, 250, 75, 23))
        self.btnProcess.setObjectName("btnProcess")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnProcess.clicked.connect(self.showList)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnProcess.setText(_translate("Dialog", "PushButton"))

    def showList(self):
        konek=sqlite3.connect('financial.db')
        a=konek.cursor()

        a.execute("SELECT * FROM PEMASUKAN")
        b=str(a.fetchall())


        self.lstTest.setTextElideMode(b)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

