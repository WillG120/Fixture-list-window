import sys,time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QListWidget, QLineEdit
from PyQt5 import uic
from datetime import datetime

class fixtureList(QMainWindow):
    
    def __init__(self):
        super(fixtureList, self).__init__()

        uic.loadUi("fixtureWindow.ui",self)

        self.fixtureList = self.findChild(QListWidget, "fixtureList")
        self.searchBar = self.findChild(QLineEdit, "searchBar")

    
        self.searchBar.textChanged.connect(self.update_display)

        
        self.show()

    

    def update_display(self):

        search_entry = self.searchBar.text().lower()

        for n in range(self.fixtureList.count()):
            item = self.fixtureList.item(n)
            if search_entry in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)




app = QApplication(sys.argv)
window = fixtureList()
app.exec_()
sys.exit(app.exec_())
