# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coba.ui'
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
        self.txtHasil = QtWidgets.QLineEdit(Dialog)
        self.txtHasil.setGeometry(QtCore.QRect(72, 80, 251, 151))
        self.txtHasil.setObjectName("txtHasil")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tampilkanHasil)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))

    def tampilkanHasil(self):
        koneksi=sqlite3.connect('financial.db')
        a=koneksi.cursor()
        b=koneksi.cursor()

        a.execute("SELECT Jumlah_Pemasukkan FROM PEMASUKAN WHERE _rowid_='1'")
        d=int(a.fetchone()[0])
        
        b.execute("SELECT Jumlah_Pengeluaran FROM PENGELUARAN WHERE _rowid_='1'")
        c=int(b.fetchone()[0])

        hasil=str(d-c)        
        

        self.txtHasil.setText(hasil)

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

