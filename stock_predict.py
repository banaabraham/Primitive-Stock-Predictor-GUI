# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock_predict.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from stock_learn import stock_machine


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 2, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.PE = QtWidgets.QLineEdit(self.centralwidget)
        self.PE.setObjectName("PE")
        self.gridLayout_2.addWidget(self.PE, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 2, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 2, 3, 6, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        self.PSales = QtWidgets.QLineEdit(self.centralwidget)
        self.PSales.setObjectName("PSales")
        self.gridLayout_2.addWidget(self.PSales, 3, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.gridLayout_2.addWidget(self.radioButton, 3, 4, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2.addLayout(self.verticalLayout_3, 4, 0, 2, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 1, 1, 1)
        self.Pbook = QtWidgets.QLineEdit(self.centralwidget)
        self.Pbook.setObjectName("Pbook")
        self.gridLayout_2.addWidget(self.Pbook, 5, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 5, 4, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2.addLayout(self.verticalLayout_4, 6, 0, 2, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 1, 1, 1)
        self.divy = QtWidgets.QLineEdit(self.centralwidget)
        self.divy.setObjectName("divy")
        self.gridLayout_2.addWidget(self.divy, 7, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_2.addLayout(self.verticalLayout_5, 8, 0, 2, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 9, 1, 1, 1)
        self.Result = QtWidgets.QLineEdit(self.centralwidget)
        self.Result.setObjectName("Result")
        self.Result.setReadOnly(True)
        self.gridLayout_2.addWidget(self.Result, 9, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 8, 3, 1, 2)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setObjectName("clear")
        self.gridLayout_2.addWidget(self.clear, 9, 3, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.calculate)
        self.clear.clicked.connect(self.hapus)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "P/E"))
        self.label_2.setText(_translate("MainWindow", "P/Sales"))
        self.radioButton.setText(_translate("MainWindow", "Random Forest"))
        self.label_3.setText(_translate("MainWindow", "P/Book"))
        self.radioButton_2.setText(_translate("MainWindow", "KNN"))
        self.label_4.setText(_translate("MainWindow", "Div Yield"))
        self.label_5.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "Predict!"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        
    def calculate(self):
        s=stock_machine()
        s.fitting_frt() 
        s.fitting_knn()
        psales = float(self.PSales.text())
        pbook = float(self.Pbook.text())
        divy = float(self.divy.text())
        pe = float(self.PE.text())
        if self.radioButton.isChecked():            
            if s.predict_frt(psales,pbook,divy,pe)==[1]: 
                self.Result.setStyleSheet("color: rgb(0.255.0);")
                self.Result.setText("It'll go up 10%+ ")
            else:
                self.Result.setStyleSheet("color: rgb(255,0,0);")
                self.Result.setText("It's a loser ")
        else:
            if s.predict_knn(psales,pbook,divy,pe)==[1]:
                self.Result.setStyleSheet("color: rgb(0.255.0);")
                self.Result.setText(">It'll go up 10%+ ")
            else:
                self.Result.setStyleSheet("color: rgb(255,0,0);")
                self.Result.setText("It's a loser")

    def hapus(self):
        self.PSales.clear()
        self.Pbook.clear()
        self.divy.clear()
        self.PE.clear()
        self.Result.clear()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

