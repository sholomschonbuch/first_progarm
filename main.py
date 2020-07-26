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
            "addjobpage": [],
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
        self.view["detail"].append(self.addCategory)
                
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(310, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.view["detail"].append(self.dateEdit)

        self.doubleCost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleCost.setGeometry(QtCore.QRect(220, 190, 62, 22))
        self.doubleCost.setMaximum(1000000.0)
        self.doubleCost.setObjectName("doubleCost")
        self.view["detail"].append(self.doubleCost)
        #project value: spin and label
        paidx = 10
        paidy = 500 
        self.projectValue = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.projectValue.setGeometry(QtCore.QRect(paidy, paidx, 130, 25))
        self.projectValue.setMaximum(1000000.0)
        self.projectValue.setObjectName("projectValue")
        self.view["detail"].append(self.projectValue)

        self.paid_amount_to_you = QtWidgets.QLabel(self.centralwidget)
        self.paid_amount_to_you.setGeometry(QtCore.QRect(paidy + 200, paidx, 261, 16))
        self.paid_amount_to_you.setObjectName("paid_amount_to_you")
        self.view["detail"].append(self.paid_amount_to_you)
        
    #/

    #job: combo, name, name label add button and remove button
        jobx = 50
        joby = 230

        self.comboBoxJob = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxJob.setGeometry(QtCore.QRect(joby, jobx, 130, 25))
        self.comboBoxJob.setObjectName("comboBoxJob")
        self.view["addjobpage"].append(self.comboBoxJob)

        self.lineJobName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineJobName.setGeometry(QtCore.QRect(joby + 130, jobx, 130, 25))
        self.lineJobName.setObjectName("lineJobName")
        self.view["addjobpage"].append(self.lineJobName)

        self.job_name = QtWidgets.QLabel(self.centralwidget)
        self.job_name.setGeometry(QtCore.QRect(50, 50, 130, 16))
        self.job_name.setObjectName("job_name")
        self.view["detail"].append(self.job_name)

        self.createjob = QtWidgets.QPushButton(self.centralwidget)
        self.createjob.setGeometry(QtCore.QRect(joby + 260, jobx, 130, 25))
        self.createjob.setObjectName("createjob")
        self.view["addjobpage"].append(self.createjob)

        self.removejob = QtWidgets.QPushButton(self.centralwidget)
        self.removejob.setGeometry(QtCore.QRect(joby + 260 + 150, jobx, 130, 25))
        self.removejob.setObjectName("removejob")   
        self.view["main"].append(self.removejob)
        self.view["detail"].append(self.removejob)


        #catagory: combo, name, add button and remove button
        catagoryy = 230
        catagoryx = 100

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(catagoryy, catagoryx, 130, 25))
        self.comboBox.setObjectName("comboBox")
        self.view["detail"].append(self.comboBox)
        

        self.lineCategoryName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCategoryName.setGeometry(QtCore.QRect(catagoryy + 130, catagoryx, 130, 25))
        self.lineCategoryName.setObjectName("lineCategoryName")
        self.view["detail"].append(self.lineCategoryName)

        self.createCategory = QtWidgets.QPushButton(self.centralwidget)
        self.createCategory.setGeometry(QtCore.QRect(catagoryy + 260, catagoryx, 130, 25))
        self.createCategory.setObjectName("createCategory")
        self.view["detail"].append(self.createCategory)
        

        self.removecatagory = QtWidgets.QPushButton(self.centralwidget)
        self.removecatagory.setGeometry(QtCore.QRect(joby + 260 + 150, jobx + 50, 130, 25))
        self.removecatagory.setObjectName("removecatagory")
        self.view["detail"].append(self.removecatagory)
        #/

        
        
        self.profit = QtWidgets.QLabel(self.centralwidget)
        self.profit.setGeometry(QtCore.QRect(240, 490, 261, 16))
        self.profit.setObjectName("profit")
        self.view["detail"].append(self.profit)
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
        self.view["detail"].append(self.addPayment)

        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(500, 500,  100, 23))
        self.backbutton.setObjectName("backbutton")
        
        self.view["addjobpage"].append(self.backbutton)
        self.view["detail"].append(self.backbutton)

        
        

        #first job button
        self.job_index = 0

        buttonsizex = 150
        buttonsizey = buttonsizex 
        buttonx = 100
        buttony = 200

        self.openjobpage = QtWidgets.QPushButton(self.centralwidget)
        self.openjobpage.setGeometry(QtCore.QRect(buttonx + 400, buttony, buttonsizex, buttonsizey))
        self.openjobpage.setObjectName("openjobpage")
        self.view["main"].append(self.openjobpage)

        
        self.jobbutton = QtWidgets.QPushButton(self.centralwidget)
        self.jobbutton.setGeometry(QtCore.QRect(buttonx, buttony, buttonsizex, buttonsizey))
        self.jobbutton.setObjectName("jobbutton")
        self.view["main"].append(self.jobbutton)
        self.jobbutton.clicked.connect(lambda: self.hide_main(0))

        self.jobbutton2 = QtWidgets.QPushButton(self.centralwidget)
        self.jobbutton2.setGeometry(QtCore.QRect(buttonx + 200 , buttony, buttonsizex, buttonsizey))
        self.jobbutton2.setObjectName("jobbutton2")
        self.view["main"].append(self.jobbutton2)
        self.jobbutton2.clicked.connect(lambda: self.hide_main(1))
        
        if os.path.isfile("catagories.data"):
            with open("catagories.data", "rb") as load:
                self.job_list = pickle.load(load)
                print(self.job_list)
                #load combo box
                for combo in self.job_list:
                    self.comboBoxJob.addItem(combo.name)
                
                for item in self.job_list[self.job_index].categorie_list:
                    self.comboBox.addItem(item.name)
                self.update_list()
        else: 
            self.job_list = []

        self.createCategory.clicked.connect(self.add_category)
        self.createjob.clicked.connect(self.add_job)
        self.removejob.clicked.connect(self.remove_job)
        self.removecatagory.clicked.connect(self.remove_catagory)
        self.addCategory.clicked.connect(self.add_cost)
        self.addPayment.clicked.connect(self.add_payment)
        self.projectValue.valueChanged.connect(self.valuechange)
        self.profit.setText("0")
        self.paid_amount_to_you.setText("0")
        self.job_name.setText("job name")
        self.comboBoxJob.currentTextChanged.connect(self.changed_job)
        
        self.openjobpage.setText("+")
        self.openjobpage.clicked.connect(self.show_addjobpage)

        
        self.backbutton.setText("Back")
        self.backbutton.clicked.connect(self.hide_detail)
        self.comboBox.addItem(self.lineCategoryName.text())
        self.comboBoxJob.addItem(self.lineJobName.text())
        self.hide_detail()
        
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

    def hide_main(self, jobindex):
        for item in self.view["main"]:
            item.setHidden(True)
        for item in self.view["detail"]:
            item.setHidden(False)
        for item in self.view["addjobpage"]:
            if item != self.removejob:
                if item != self.backbutton:
                    item.setHidden(True)
        self.job_index = jobindex
        self.job_name.setText(self.job_list[jobindex].name)
        self.update_list()
        print("hide main")

    def hide_addjobpage(self):
        for item in self.view["main"]:
            item.setHidden(False)
        for item in self.view["detail"]:
            item.setHidden(True)
        for item in self.view["addjobpage"]:
            if item != self.backbutton:
                item.setHidden(True)
        print("hide_addjobpage")

    def show_addjobpage(self):
        for item in self.view["main"]:
            item.setHidden(True)
        for item in self.view["detail"]:
            item.setHidden(True)
        for item in self.view["addjobpage"]:
            item.setHidden(False)
        print("show_addjobpage")



    
    def hide_detail(self):
        for item in self.view["main"]:
            item.setHidden(False)
        for item in self.view["detail"]:
            item.setHidden(True)
        for item in self.view["addjobpage"]:
            item.setHidden(True)
        print("hide detail")

        if len(self.job_list) > 0:
            self.jobbutton.setText(f"{self.job_list[0].name}\n{self.job_list[0].value}")
        if len(self.job_list) > 1:
        
            self.jobbutton2.setText(f"{self.job_list[1].name}\n{self.job_list[1].value}")
                 
        
        #if len(self.job_list) < 1:
            #self.jobbutton.setText(f"{self.job_list[0].name}\n{self.job_list[0].value}")
            #self.jobbutton2.setText(f"{self.job_list[1].name}\n{self.job_list[1].value}")
        #else:
            #self.jobbutton.setText(f"{self.job_list[0].name}\n{self.job_list[0].value}")
            #print("not enough jobs!")
            #self.hide_detail
        

    def add_job(self):
            print("Adding Job")
            if self.lineJobName.text() != "":
                self.job_list.append(job(self.lineJobName.text(), self.projectValue.value()))
                self.comboBoxJob.addItem(self.lineJobName.text())
                self.lineJobName.setText("")
                print(self.job_list)
                self.update_data()


    
    def add_category(self):
        print("Adding Category")
        if self.lineCategoryName.text() != "":

            # self.comboBox.addItem(self.lineCategoryName.text())
            categorie_holder = categorie(self.lineCategoryName.text())
            self.job_list[self.job_index].categorie_list.append(categorie_holder)
            self.lineCategoryName.setText("")
            print(self.job_list)
            self.update_list()



    def remove_catagory(self):
        print("removing job")

        print(self.job_list[self.job_index].name)
        for index, catagory in enumerate(self.job_list[self.job_index].categorie_list):
            if catagory.name == self.comboBox.currentText():
                print(f"catagory to remove: {catagory.name}, {index}")
                self.job_list[self.job_index].categorie_list.pop(index)

                self.update_list()
                

    def remove_job(self):
        self.job_list.pop(self.job_index)
        self.comboBoxJob.clear()
        self.comboBoxJob.addItem(self.job_list[self.job_index].name)
        self.update_list()


     


    def changed_job(self):

        print(self.comboBoxJob.currentText())        
        self.update_list()
        self.hide_main(self.job_index)
        print("changedjob")
        

 
    def add_cost(self):
        print("add cost")

        for item in self.job_list[self.job_index].categorie_list:
            if item.name == self.comboBox.currentText():
                item.add(self.doubleCost.value(), str(self.dateEdit.date()))
                self.update_list()


    def add_payment(self):
        print("add paid")
        for item in self.job_list[self.job_index].categorie_list:
            if item.name == self.comboBox.currentText():
                item.add_paid(self.doubleCost.value(), str(self.dateEdit.date()))
                self.update_list()


    #redo everything like this
    def update_list(self):

        self.listWidget.clear()
        self.comboBox.clear()
        if len(self.job_list) == 0:
            print("not enough jobs!")
        else:
            self.projectValue.setValue(self.job_list[self.job_index].value) 
        for item in self.job_list[self.job_index].categorie_list:
            name = item.name
            self.listWidget.addItem(f"{name}\tCost: {item.total()}\tPaid: {item.total_paid()}\tOwe: {item.total() - item.total_paid()}")
            self.comboBox.addItem(item.name)
        
        
        self.update_profit()
        self.update_paid_amount_to_you()
        self.update_data()
        

    def valuechange(self):
        print(f"value: {self.projectValue.value()}------")
        
        self.job_list[self.job_index].value = self.projectValue.value()
        self.update_data()

    def update_data(self):
        print(self.job_list, "----")
        with open("catagories.data", "wb") as data_update:
            pickle.dump(self.job_list, data_update)

    def update_paid_amount_to_you(self):
        total_cost = 0
        for item in self.job_list[self.job_index].categorie_list:
            total_cost += item.total()

        self.paid_amount_to_you.setText(f"{self.projectValue.value()} ")


    def update_profit(self):
        total_cost = 0

        for item in self.job_list[self.job_index].categorie_list:
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

