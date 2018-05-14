# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pengeluaran.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 140, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnProcess = QtWidgets.QPushButton(self.centralwidget)
        self.btnProcess.setGeometry(QtCore.QRect(270, 280, 181, 91))
        self.btnProcess.setObjectName("btnProcess")
        self.txtPengeluaran = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPengeluaran.setGeometry(QtCore.QRect(230, 220, 271, 20))
        self.txtPengeluaran.setObjectName("txtPengeluaran")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 250, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #####################################
        self.btnProcess.clicked.connect(self.inputPengeluaran)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Form Pengeluaran"))
        self.btnProcess.setText(_translate("MainWindow", "Process"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Category"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Makan"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Transportasi"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Belanja"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Fun"))
        

    def inputPengeluaran(self):

        print("Clicked")

        Pengeluaran=self.txtPengeluaran.text()

        konek=sqlite3.connect("financial.db")
        a=konek.cursor()
        a.execute("INSERT INTO PENGELUARAN VALUES(?)",[Pengeluaran],self.comboBox.itemText(1))
        konek.commit()
        konek.close()

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

