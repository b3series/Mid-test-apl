# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report tes.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
#changes

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtLaporan1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLaporan1.setGeometry(QtCore.QRect(160, 90, 381, 91))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnReport.clicked.connect(self.reportResult)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "REPORT"))
        self.btnReport.setText(_translate("MainWindow", "PushButton"))

    def reportResult(self):
        konek=sqlite3.connect("financial.db")
        
        result= str(konek.execute("SELECT * FROM PEMASUKAN"))
        konek.close()
        self.txtLaporan1.setText(result)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

