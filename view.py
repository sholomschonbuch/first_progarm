# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from classes import categorie, job

import pickle 
import os.path
from os import path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.view = {
            "main": [],
            "detail": []
        }
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(130, 260, 600, 192))
        self.listWidget.setObjectName("listWidget")
        self.view["detail"].append(self.listWidget)

        self.addCategory = QtWidgets.QPushButton(self.centralwidget)
        self.addCategory.setGeometry(QtCore.QRect(450, 175, 75, 23))
        self.addCategory.setObjectName("addCategory")
        self.view["main"].append(self.addCategory)
        
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(310, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.doubleCost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleCost.setGeometry(QtCore.QRect(220, 190, 62, 22))
        self.doubleCost.setMaximum(1000000.0)
        self.doubleCost.setObjectName("doubleCost")
        #project value: spin and label
        paidx = 10
        paidy = 500
        self.projectValue = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.projectValue.setGeometry(QtCore.QRect(paidy, paidx, 130, 25))
        self.projectValue.setMaximum(1000000.0)
        self.projectValue.setObjectName("projectValue")

        self.paid_amount_to_you = QtWidgets.QLabel(self.centralwidget)
        self.paid_amount_to_you.setGeometry(QtCore.QRect(paidy + 200, paidx, 261, 16))
        self.paid_amount_to_you.setObjectName("paid_amount_to_you")
        
    #/
        #job: combo, name and button
        jobx = 50
        joby = 230

        self.comboBoxJob = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxJob.setGeometry(QtCore.QRect(joby, jobx, 130, 25))
        self.comboBoxJob.setObjectName("comboBoxJob")

        self.lineJobName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineJobName.setGeometry(QtCore.QRect(joby + 130, jobx, 130, 25))
        self.lineJobName.setObjectName("lineJobName")

        self.createjob = QtWidgets.QPushButton(self.centralwidget)
        self.createjob.setGeometry(QtCore.QRect(joby + 260, jobx, 130, 25))
        self.createjob.setObjectName("createjob")
        #/

        # Remove buttons
        self.removecatagory = QtWidgets.QPushButton(self.centralwidget)
        self.removecatagory.setGeometry(QtCore.QRect(joby + 260 + 150, jobx + 50, 130, 25))
        self.removecatagory.setObjectName("removecatagory")   

        self.removejob = QtWidgets.QPushButton(self.centralwidget)
        self.removejob.setGeometry(QtCore.QRect(joby + 260 + 150, jobx, 130, 25))
        self.removejob.setObjectName("removejob")   
        #/

        #catagory: combo, name and button
        catagoryy = 230
        catagoryx = 100

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(catagoryy, catagoryx, 130, 25))
        self.comboBox.setObjectName("comboBox")

        self.lineCategoryName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCategoryName.setGeometry(QtCore.QRect(catagoryy + 130, catagoryx, 130, 25))
        self.lineCategoryName.setObjectName("lineCategoryName")

        self.createCategory = QtWidgets.QPushButton(self.centralwidget)
        self.createCategory.setGeometry(QtCore.QRect(catagoryy + 260, catagoryx, 130, 25))
        self.createCategory.setObjectName("createCategory")
        #/

        
        
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
        self.addPayment.setGeometry(QtCore.QRect(450, 200, 100, 23))
        self.addPayment.setObjectName("addPayment")


        #added Itmes
        
        if os.path.isfile("catagories.data"):
            with open("catagories.data", "rb") as load:
                self.job_list = pickle.load(load)
                print(self.job_list)
                #load combo box
                for combo in self.job_list:
                    self.comboBoxJob.addItem(combo.name)
                for job in self.job_list:
                    if job.name == self.comboBoxJob.currentText():
                        for item in job.categorie_list:
                            self.comboBox.addItem(item.name)
                self.update_list()
        else: 
            self.job_list = []

        self.createCategory.clicked.connect(self.hide_main)
        self.createjob.clicked.connect(self.hide_detail)
        self.removejob.clicked.connect(self.remove_job)
        self.removecatagory.clicked.connect(self.remove_catagory)
        self.addCategory.clicked.connect(self.add_cost)
        self.addPayment.clicked.connect(self.add_payment)
        self.projectValue.valueChanged.connect(self.valuechange)
        self.profit.setText("0")
        self.paid_amount_to_you.setText("0")
        self.comboBoxJob.currentTextChanged.connect(self.changed_job)
        self.projectValue.setValue(0)
        self.comboBox.addItem(self.lineCategoryName.text())
        self.comboBoxJob.addItem(self.lineJobName.text())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addCategory.setText(_translate("MainWindow", "Add Cost"))
        self.addPayment.setText(_translate("MainWindow", "Add Payment"))
        self.createCategory.setText(_translate("MainWindow", "Create Category"))
        self.createjob.setText(_translate("MainWindow", "add job"))
        self.removejob.setText(_translate("MainWindow", "remove job"))
        self.removecatagory.setText(_translate("MainWindow", "remove catagory"))
        self.profit.setText(_translate("MainWindow", "0"))

    def hide_main(self):
        for item in self.view["main"]:
            item.setHidden(True)
        for item in self.view["detail"]:
            item.setHidden(False)

    
    def hide_detail(self):
        for item in self.view["main"]:
            item.setHidden(False)
        for item in self.view["detail"]:
            item.setHidden(True)


    def add_category(self):
        print("Adding Category")
        if self.lineCategoryName.text() != "":
            for job in self.job_list:
                if job.name == self.comboBoxJob.currentText():
                    # self.comboBox.addItem(self.lineCategoryName.text())
                    categorie_holder = categorie(self.lineCategoryName.text())
                    job.categorie_list.append(categorie_holder)
                    self.lineCategoryName.setText("")
                    print(self.job_list)
                    self.update_list()


    def add_job(self):
        print("Adding Job")
        if self.lineJobName.text() != "":
            self.job_list.append(job(self.lineJobName.text(), self.projectValue.value()))
            self.comboBoxJob.addItem(self.lineJobName.text())
            self.lineJobName.setText("")
            print(self.job_list)
            self.update_data()

    def remove_catagory(self):
        print("removing job")
        for job in self.job_list:
            if job.name == self.comboBoxJob.currentText():
                print(job.name)
                for index, catagory in enumerate(job.categorie_list):
                    if catagory.name == self.comboBox.currentText():
                        print(f"catagory to remove: {catagory.name}, {index}")
                        job.categorie_list.pop(index)

                        self.update_list()
                        



    def remove_job(self):
        for index, job in enumerate(self.job_list):
            if job.name == self.comboBoxJob.currentText():
                print(f"Job to remove: {job.name}, {index}")
                self.job_list.pop(index)

                self.comboBoxJob.clear()
                for job in self.job_list:
                    self.comboBoxJob.addItem(job.name)

                self.update_list()


    def changed_job(self):
        print(self.comboBoxJob.currentText())
        self.update_list()

 
    def add_cost(self):
        print("add cost")
        for job in self.job_list:
            if job.name == self.comboBoxJob.currentText():
                for item in job.categorie_list:
                    if item.name == self.comboBox.currentText():
                        item.add(self.doubleCost.value(), str(self.dateEdit.date()))
                        self.update_list()


    def add_payment(self):
        print("add paid")
        for job in self.job_list:
            if job.name == self.comboBoxJob.currentText():
                for item in job.categorie_list:
                    if item.name == self.comboBox.currentText():
                        item.add_paid(self.doubleCost.value(), str(self.dateEdit.date()))
                        self.update_list()


    #redo everything like this
    def update_list(self):

        self.listWidget.clear()
        self.comboBox.clear()

        for job in self.job_list:
            if job.name == self.comboBoxJob.currentText():
                for item in job.categorie_list:
                    name = item.name
                    self.listWidget.addItem(f"{name}\tCost: {item.total()}\tPaid: {item.total_paid()}\tOwe: {item.total() - item.total_paid()}")
        
        for job in self.job_list:
            if job.name == self.comboBoxJob.currentText():
                for item in job.categorie_list:
                    self.comboBox.addItem(item.name)
        
        self.update_profit()
        self.update_paid_amount_to_you()
        self.update_data()
        

    def valuechange(self):
        print(f"value: {self.projectValue.value()}------")
        self.job_list[0].value = self.projectValue.value()
        self.update_data()

    def update_data(self):
        print(self.job_list, "----")
        with open("catagories.data", "wb") as data_update:
            pickle.dump(self.job_list, data_update)

    def update_paid_amount_to_you(self):
        total_cost = 0
        for job in self.job_list:
            if job.name == self.comboBoxJob.currentText():
                for item in job.categorie_list:
                    total_cost += item.total()

        self.paid_amount_to_you.setText(f"{self.projectValue.value()} ")


    def update_profit(self):
        total_cost = 0
        for job in self.job_list:
            if job.name == self.comboBoxJob.currentText():
                for item in job.categorie_list:
                    total_cost += item.total()

        self.profit.setText(f"{self.projectValue.value() - total_cost} ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """
        QWidget{
            background: #ccdade;
            color: #000;
        }
        QPushButton{
            background: #0577a8;
            padding: 5px 5px;
            border: 1px #f00 solid;
            font-weight: bold;
        }
        QPushButton#addPayment{
            background: #f00;
        }
        QPushButton:hover{
            background: #0f0;
        }
        
    """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

