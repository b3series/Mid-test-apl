# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report tes.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pengeluarantes import Ui_Pengeluaran
import sqlite3


class Ui_Laporan(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtLaporan1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLaporan1.setGeometry(QtCore.QRect(160, 90, 381, 91))
        self.txtLaporan1.setText("")
        self.txtLaporan1.setObjectName("txtLaporan1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 60, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.txtLaporan2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLaporan2.setGeometry(QtCore.QRect(160, 190, 381, 91))
        self.txtLaporan2.setObjectName("txtLaporan2")
        self.txtLaporan3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLaporan3.setGeometry(QtCore.QRect(160, 290, 381, 91))
        self.txtLaporan3.setObjectName("txtLaporan3")
        self.txtLaporan4 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLaporan4.setGeometry(QtCore.QRect(160, 390, 381, 91))
        self.txtLaporan4.setObjectName("txtLaporan4")
        self.btnReport = QtWidgets.QPushButton(self.centralwidget)
        self.btnReport.setGeometry(QtCore.QRect(40, 250, 75, 61))
        self.btnReport.setObjectName("btnReport")
        self.btnPemasukan = QtWidgets.QPushButton(self.centralwidget)
        self.btnPemasukan.setGeometry(QtCore.QRect(570, 210, 101, 51))
        self.btnPemasukan.setObjectName("btnPemasukan")
        self.btnPengeluaran = QtWidgets.QPushButton(self.centralwidget)
        self.btnPengeluaran.setGeometry(QtCore.QRect(570, 280, 101, 51))
        self.btnPengeluaran.setObjectName("btnPengeluaran")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.btnPemasukan.clicked.connect(self.ShowWindowPemasukan)
        self.btnPengeluaran.clicked.connect(self.ShowWindowPengeluaran)
        self.btnReport.clicked.connect(self.reportResult)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LAPORAN"))
        self.btnReport.setText(_translate("MainWindow", "Report"))
        self.btnPemasukan.setText(_translate("MainWindow", "Menu Pemasukan"))
        self.btnPengeluaran.setText(_translate("MainWindow", "Menu Pengeluaran"))

    #def ShowWindowPemasukan(self):
       # self.WindowPemasukan=QtWidgets.QMainWindow()
       # self.ui=Ui_MainWindow()
       # self.ui.setupUi(self.WindowPemasukan)
       # self.WindowPemasukan.show()
        

    def ShowWindowPengeluaran(self):
        self.windowPengeluaran=QtWidgets.QMainWindow()
        self.ui=Ui_Pengeluaran()
        self.ui.setupUi(self.windowPengeluaran)
        self.windowPengeluaran.show()
        
    def reportResult(self):
        konek=sqlite3.connect("financial.db")
        a=konek.cursor()
        c=konek.cursor()
        e=konek.cursor()
        g=konek.cursor()
        i=konek.cursor()
        k=konek.cursor()
        a.execute("SELECT * FROM PEMASUKAN")
        b=str(a.fetchone()[0])
        self.txtLaporan1.setText("Uang anda:"+b)

        c.execute("SELECT * FROM PENGELUARAN")
        d=str(c.fetchone()[0])
        e.execute("SELECT * FROM CATEGORY")
        f=str(e.fetchall()[0])
        
        g.execute("SELECT Jumlah_Pemasukkan FROM PEMASUKAN WHERE _rowid_='1'")
        h=int(g.fetchone()[0])

        i.execute("SELECT Jumlah_Pengeluaran FROM PENGELUARAN WHERE _rowid_='1'")
        j=int(i.fetchone()[0])

        hasil=str(h-j)

        k.execute("UPDATE HASIL SET Total=(?) WHERE _rowid_='1'",[hasil])
        konek.commit()
        k.execute("SELECT * FROM HASIL")
        l=str(k.fetchone()[0])

        self.txtLaporan2.setText("Pengeluaran Anda:"+d)
        self.txtLaporan3.setText("Untuk :"+f)
        self.txtLaporan4.setText("Sisa :"+l)

        konek.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Laporan()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

