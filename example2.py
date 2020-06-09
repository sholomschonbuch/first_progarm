# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from classes import categorie
import pickle 
import os.path
from os import path

class Ui_MainWindow(object):#c
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(130, 260, 600, 192))
        self.listWidget.setObjectName("listWidget")

        self.addCategory = QtWidgets.QPushButton(self.centralwidget)
        self.addCategory.setGeometry(QtCore.QRect(450, 175, 75, 23))
        self.addCategory.setObjectName("addCategory")
        
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(310, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.doubleCost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleCost.setGeometry(QtCore.QRect(220, 190, 62, 22))
        self.doubleCost.setMaximum(1000000.0)
        self.doubleCost.setObjectName("doubleCost")
        
        self.lineCategoryName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCategoryName.setGeometry(QtCore.QRect(310, 120, 113, 20))
        self.lineCategoryName.setObjectName("lineCategoryName")

        self.createCategory = QtWidgets.QPushButton(self.centralwidget)
        self.createCategory.setGeometry(QtCore.QRect(430, 120, 91, 23))
        self.createCategory.setObjectName("createCategory")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 190, 131, 22))
        self.comboBox.setObjectName("comboBox")

        self.projectValue = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.projectValue.setGeometry(QtCore.QRect(300, 40, 151, 22))
        self.projectValue.setMaximum(1000000.0)
        self.projectValue.setObjectName("projectValue")

        self.profit = QtWidgets.QLabel(self.centralwidget)
        self.profit.setGeometry(QtCore.QRect(240, 490, 261, 16))
        self.profit.setObjectName("profit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #self made:
        self.addPayment = QtWidgets.QPushButton(self.centralwidget)
        self.addPayment.setGeometry(QtCore.QRect(450, 200, 75, 23))
        self.addPayment.setObjectName("addPayment")

        #added Itmes
        if os.path.isfile("catagories.data"):
            with open("catagories.data", "rb") as load:
                self.category_list = pickle.load(load)
                self.update_list()
                #load combo box
                for combo in self.category_list:
                    self.comboBox.addItem(combo.name)
        else:
            self.category_list = []
        self.createCategory.clicked.connect(self.add_category)
        self.addCategory.clicked.connect(self.add_cost)
        self.addPayment.clicked.connect(self.add_payment)
        self.profit.setText("0")
        self.comboBox.addItem(self.lineCategoryName.text())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addCategory.setText(_translate("MainWindow", "Add Cost"))
        self.addPayment.setText(_translate("MainWindow", "Add Payment"))
        self.createCategory.setText(_translate("MainWindow", "Create Category"))
        self.profit.setText(_translate("MainWindow", "0"))

    def add_category(self):
        print("Adding Category")
        if self.lineCategoryName.text() != "":
            self.category_list.append(categorie(self.lineCategoryName.text()))
            self.comboBox.addItem(self.lineCategoryName.text())
            self.lineCategoryName.setText("")
            print(self.category_list)
            self.update_list()

    def add_cost(self):
        print("add cost")
        for item in self.category_list:
            if item.name == self.comboBox.currentText():
                item.add(self.doubleCost.value(), str(self.dateEdit.date()))
                self.update_list()


    def add_payment(self):
        print("add paid")
        for item in self.category_list:
            if item.name == self.comboBox.currentText():
                item.add_paid(self.doubleCost.value(), str(self.dateEdit.date()))
                self.update_list()


    
    def update_list(self):
        self.listWidget.clear()
        for item in self.category_list:
            name = item.name
            self.listWidget.addItem(f"{name}\tCost: {item.total()}\tPaid: {item.total_paid()}\tOwe: {item.total() - item.total_paid()}")
        self.update_profit()
        self.update_data()

    def update_data(self):
        with open("catagories.data", "wb") as data_update:
            pickle.dump(self.category_list, data_update)


    def update_profit(self):
        total_cost = 0
        for item in self.category_list:
            total_cost += item.total()

        self.profit.setText(f"{self.projectValue.value() - total_cost} ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
