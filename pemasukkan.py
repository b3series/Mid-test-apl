# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pemasukkan.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from laporan import Ui_Laporan
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 110, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.txtPemasukkan = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPemasukkan.setGeometry(QtCore.QRect(220, 190, 271, 20))
        self.txtPemasukkan.setObjectName("txtPemasukkan")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 181, 91))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ###
        self.pushButton.clicked.connect(self.ProcessPemasukkan)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Form Pemasukkan"))
        self.pushButton.setText(_translate("MainWindow", "Process"))
    
    def ShowWindowLaporan(self):
        self.Laporan=QtWidgets.QMainWindow()
        self.ui= Ui_Laporan()
        self.ui.setupUi(self.Laporan)
        self.Laporan.show()

        

    def ProcessPemasukkan(self):
        print("Button Process Clicked !")
        Pemasukkan=self.txtPemasukkan.text()

        konek=sqlite3.connect('financial.db')
        c=konek.cursor()
        c.execute("UPDATE PEMASUKAN SET Jumlah_Pemasukkan=(?) WHERE _rowid_='1'",[Pemasukkan])
        konek.commit()
        konek.close()

        self.ShowWindowLaporan()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

