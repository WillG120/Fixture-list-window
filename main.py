import sys,time
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QListWidget, QLineEdit, QTableWidget, QSlider, QLCDNumber, QLabel
from PyQt5 import uic
from datetime import datetime

class mainWindow(QMainWindow):

    
    def __init__(self):
        super(mainWindow, self).__init__()

        uic.loadUi("fixtureWindow.ui",self)

        self.manufacturerList = self.findChild(QListWidget, "manufacturerList")
        self.searchBar_Manufacturers = self.findChild(QLineEdit, "searchBar_Manufacturers")
        self.searchBar_Fixtures = self.findChild(QLineEdit, "searchBar_Fixtures")
        self.fixtureList = self.findChild(QListWidget, "fixtureList")
        self.fixtureInfo = self.findChild(QTableWidget, "fixtureInfo")

        self.manufacturerFixtures = self.load_json_fixtures("manufacturerFixtures.json")
        self.fixtureData = self.manufacturerList.currentRowChanged.connect(self.json_load)
        self.searchBar_Manufacturers.textChanged.connect(self.update_manufacturers)
        self.searchBar_Fixtures.textChanged.connect(self.update_fixtures)
        self.manufacturerList.itemClicked.connect(self.display_fixtures)
        self.fixtureList.itemClicked.connect(self.display_fixture_info)

        self.ch1_fader = self.findChild(QSlider, "ch1")
        self.ch2_fader = self.findChild(QSlider, "ch2")
        self.ch3_fader = self.findChild(QSlider, "ch3")
        self.ch4_fader = self.findChild(QSlider, "ch4")
        self.ch5_fader = self.findChild(QSlider, "ch5")
        self.ch6_fader = self.findChild(QSlider, "ch6")
        self.ch7_fader = self.findChild(QSlider, "ch7")
        self.ch8_fader = self.findChild(QSlider, "ch8")
        self.ch9_fader = self.findChild(QSlider, "ch9")
        self.ch10_fader = self.findChild(QSlider, "ch10")
        self.ch11_fader = self.findChild(QSlider, "ch11")
        self.ch12_fader = self.findChild(QSlider, "ch12")
        self.ch13_fader = self.findChild(QSlider, "ch13")
        self.ch14_fader = self.findChild(QSlider, "ch14")
        self.ch15_fader = self.findChild(QSlider, "ch15")
        self.ch16_fader = self.findChild(QSlider, "ch16")
        self.ch17_fader = self.findChild(QSlider, "ch17")
        self.ch18_fader = self.findChild(QSlider, "ch18")
        self.ch19_fader = self.findChild(QSlider, "ch19")
        self.ch20_fader = self.findChild(QSlider, "ch20")
        self.ch21_fader = self.findChild(QSlider, "ch21")
        self.ch22_fader = self.findChild(QSlider, "ch22")
        self.ch23_fader = self.findChild(QSlider, "ch23")
        self.ch24_fader = self.findChild(QSlider, "ch24")
        self.ch25_fader = self.findChild(QSlider, "ch25")
        self.ch26_fader = self.findChild(QSlider, "ch26")
        self.ch27_fader = self.findChild(QSlider, "ch27")
        self.ch28_fader = self.findChild(QSlider, "ch28")
        self.master_fader = self.findChild(QSlider, "master")

        self.ch1_lbl = self.findChild(QLabel, "lbl_1")
        self.ch2_lbl = self.findChild(QLabel, "lbl_2")
        self.ch3_lbl = self.findChild(QLabel, "lbl_3")
        self.ch4_lbl = self.findChild(QLabel, "lbl_4")
        self.ch5_lbl = self.findChild(QLabel, "lbl_5")
        self.ch6_lbl = self.findChild(QLabel, "lbl_6")
        self.ch7_lbl = self.findChild(QLabel, "lbl_7")
        self.ch8_lbl = self.findChild(QLabel, "lbl_8")
        self.ch9_lbl = self.findChild(QLabel, "lbl_9")
        self.ch10_lbl = self.findChild(QLabel, "lbl_10")
        self.ch11_lbl = self.findChild(QLabel, "lbl_11")
        self.ch12_lbl = self.findChild(QLabel, "lbl_12")
        self.ch13_lbl = self.findChild(QLabel, "lbl_13")
        self.ch14_lbl = self.findChild(QLabel, "lbl_14")
        self.ch15_lbl = self.findChild(QLabel, "lbl_15")
        self.ch16_lbl = self.findChild(QLabel, "lbl_16")
        self.ch17_lbl = self.findChild(QLabel, "lbl_17")
        self.ch18_lbl = self.findChild(QLabel, "lbl_18")
        self.ch19_lbl = self.findChild(QLabel, "lbl_19")
        self.ch20_lbl = self.findChild(QLabel, "lbl_20")
        self.ch21_lbl = self.findChild(QLabel, "lbl_21")
        self.ch22_lbl = self.findChild(QLabel, "lbl_22")
        self.ch23_lbl = self.findChild(QLabel, "lbl_23")
        self.ch24_lbl = self.findChild(QLabel, "lbl_24")
        self.ch25_lbl = self.findChild(QLabel, "lbl_25")
        self.ch26_lbl = self.findChild(QLabel, "lbl_26")
        self.ch27_lbl = self.findChild(QLabel, "lbl_27")
        self.ch28_lbl = self.findChild(QLabel, "lbl_28")
        self.master_lbl = self.findChild(QLabel, "lbl_Master")

        self.ch1_lvl = self.findChild(QLCDNumber, "ch1_lcd")
        self.ch2_lvl = self.findChild(QLCDNumber, "ch2_lcd")
        self.ch3_lvl = self.findChild(QLCDNumber, "ch3_lcd")
        self.ch4_lvl = self.findChild(QLCDNumber, "ch4_lcd")
        self.ch5_lvl = self.findChild(QLCDNumber, "ch5_lcd")
        self.ch6_lvl = self.findChild(QLCDNumber, "ch6_lcd")
        self.ch7_lvl = self.findChild(QLCDNumber, "ch7_lcd")
        self.ch8_lvl = self.findChild(QLCDNumber, "ch8_lcd")
        self.ch9_lvl = self.findChild(QLCDNumber, "ch9_lcd")
        self.ch10_lvl = self.findChild(QLCDNumber, "ch10_lcd")
        self.ch11_lvl = self.findChild(QLCDNumber, "ch11_lcd")
        self.ch12_lvl = self.findChild(QLCDNumber, "ch12_lcd")
        self.ch13_lvl = self.findChild(QLCDNumber, "ch13_lcd")
        self.ch14_lvl = self.findChild(QLCDNumber, "ch14_lcd")
        self.ch15_lvl = self.findChild(QLCDNumber, "ch15_lcd")
        self.ch16_lvl = self.findChild(QLCDNumber, "ch16_lcd")
        self.ch17_lvl = self.findChild(QLCDNumber, "ch17_lcd")
        self.ch18_lvl = self.findChild(QLCDNumber, "ch18_lcd")
        self.ch19_lvl = self.findChild(QLCDNumber, "ch19_lcd")
        self.ch20_lvl = self.findChild(QLCDNumber, "ch20_lcd")
        self.ch21_lvl = self.findChild(QLCDNumber, "ch21_lcd")
        self.ch22_lvl = self.findChild(QLCDNumber, "ch22_lcd")
        self.ch23_lvl = self.findChild(QLCDNumber, "ch23_lcd")
        self.ch24_lvl = self.findChild(QLCDNumber, "ch24_lcd")
        self.ch25_lvl = self.findChild(QLCDNumber, "ch25_lcd")
        self.ch26_lvl = self.findChild(QLCDNumber, "ch26_lcd")
        self.ch27_lvl = self.findChild(QLCDNumber, "ch27_lcd")
        self.ch28_lvl = self.findChild(QLCDNumber, "ch28_lcd")
        self.master_lvl = self.findChild(QLCDNumber, "master_lcd")


        self.ch1_fader.sliderMoved.connect(self.ch1_lvl_change)
        self.ch2_fader.sliderMoved.connect(self.ch2_lvl_change)
        self.ch3_fader.sliderMoved.connect(self.ch3_lvl_change)
        self.ch4_fader.sliderMoved.connect(self.ch4_lvl_change)
        self.ch5_fader.sliderMoved.connect(self.ch5_lvl_change)
        self.ch6_fader.sliderMoved.connect(self.ch6_lvl_change)
        self.ch7_fader.sliderMoved.connect(self.ch7_lvl_change)
        self.ch8_fader.sliderMoved.connect(self.ch8_lvl_change)
        self.ch9_fader.sliderMoved.connect(self.ch9_lvl_change)
        self.ch10_fader.sliderMoved.connect(self.ch10_lvl_change)
        self.ch11_fader.sliderMoved.connect(self.ch11_lvl_change)
        self.ch12_fader.sliderMoved.connect(self.ch12_lvl_change)
        self.ch13_fader.sliderMoved.connect(self.ch13_lvl_change)
        self.ch14_fader.sliderMoved.connect(self.ch14_lvl_change)
        self.ch15_fader.sliderMoved.connect(self.ch15_lvl_change)
        self.ch16_fader.sliderMoved.connect(self.ch16_lvl_change)
        self.ch17_fader.sliderMoved.connect(self.ch17_lvl_change)
        self.ch18_fader.sliderMoved.connect(self.ch18_lvl_change)
        self.ch19_fader.sliderMoved.connect(self.ch19_lvl_change)
        self.ch20_fader.sliderMoved.connect(self.ch20_lvl_change)
        self.ch21_fader.sliderMoved.connect(self.ch21_lvl_change)
        self.ch22_fader.sliderMoved.connect(self.ch22_lvl_change)
        self.ch23_fader.sliderMoved.connect(self.ch23_lvl_change)
        self.ch24_fader.sliderMoved.connect(self.ch24_lvl_change)
        self.ch25_fader.sliderMoved.connect(self.ch25_lvl_change)
        self.ch26_fader.sliderMoved.connect(self.ch26_lvl_change)
        self.ch27_fader.sliderMoved.connect(self.ch27_lvl_change)
        self.ch28_fader.sliderMoved.connect(self.ch28_lvl_change)
        self.master_fader.sliderMoved.connect(self.master_lvl_change)

        
        

        self.show()

    def ch1_lvl_change(self, sliderPosition):
        self.ch1_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch1_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch1_lbl.setStyleSheet("color: rgb(255, 255, 255);")
    
    def ch2_lvl_change(self, sliderPosition):
        self.ch2_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch2_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch2_lbl.setStyleSheet("color: rgb(255, 255, 255);")
   
    def ch3_lvl_change(self, sliderPosition):
        self.ch3_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch3_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch3_lbl.setStyleSheet("color: rgb(255, 255, 255);")
   
    def ch4_lvl_change(self, sliderPosition):
        self.ch4_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch4_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch4_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch5_lvl_change(self, sliderPosition):
        self.ch5_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch5_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch5_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch6_lvl_change(self, sliderPosition):
        self.ch6_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch6_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch6_lbl.setStyleSheet("color: rgb(255, 255, 255);")
            
    def ch7_lvl_change(self, sliderPosition):
        self.ch7_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch7_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch7_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch8_lvl_change(self, sliderPosition):
        self.ch8_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch8_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch8_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch9_lvl_change(self, sliderPosition):
        self.ch9_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch9_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch9_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch10_lvl_change(self, sliderPosition):
        self.ch10_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch10_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch10_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch11_lvl_change(self, sliderPosition):
        self.ch11_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch11_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch11_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch12_lvl_change(self, sliderPosition):
        self.ch12_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch12_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch12_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch13_lvl_change(self, sliderPosition):
        self.ch13_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch13_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch13_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch14_lvl_change(self, sliderPosition):
        self.ch14_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch14_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch14_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch15_lvl_change(self, sliderPosition):
        self.ch15_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch15_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch15_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch16_lvl_change(self, sliderPosition):
        self.ch16_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch16_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch16_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch17_lvl_change(self, sliderPosition):
        self.ch17_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch17_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch17_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch18_lvl_change(self, sliderPosition):
        self.ch18_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch18_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch18_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch19_lvl_change(self, sliderPosition):
        self.ch19_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch19_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch19_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch20_lvl_change(self, sliderPosition):
        self.ch20_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch20_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch20_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch21_lvl_change(self, sliderPosition):
        self.ch21_lvl.display(str(sliderPosition))
        
        if sliderPosition > 0:
            self.ch21_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch21_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch22_lvl_change(self, sliderPosition):
        self.ch22_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch22_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch22_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch23_lvl_change(self, sliderPosition):
        self.ch23_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch23_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch23_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch24_lvl_change(self, sliderPosition):
        self.ch24_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch24_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch24_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch25_lvl_change(self, sliderPosition):
        self.ch25_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch25_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch25_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch26_lvl_change(self, sliderPosition):
        self.ch26_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch26_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch26_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch27_lvl_change(self, sliderPosition):
        self.ch27_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch27_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch27_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def ch28_lvl_change(self, sliderPosition):
        self.ch28_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.ch28_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ch28_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def master_lvl_change(self, sliderPosition):
        self.master_lvl.display(str(sliderPosition))

        if sliderPosition > 0:
            self.master_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.master_lbl.setStyleSheet("color: rgb(255, 255, 255);")

        

    def load_json_fixtures(self, filename):

        with open(filename, "r") as file:
                return json.load(file)
        

    def json_load(self, index):
        global file_path
        file_path = ("spica-250m.json")
        
        if index == 0:
            file_path = ("spica-250m.json")
        
        elif index == 1:
            file_path = ("twister-4.json")

        elif index == 2:
            file_path = ("par-180-cob-3in1.json")
        
        elif index == 3:
            
            current_index = self.fixtureList.currentRow()
            
            if current_index == 0:
                file_path = ("alc4.json")
            elif current_index == 1:
                file_path = ("europe-105.json")
            elif current_index == 2:
                file_path = ("warp-m.json")
        
        else:
            file_path = ("error")

        return file_path



    def display_fixture_info(self, index):
       file = self.json_load(index)
       

       with open(file, 'r') as files:
           data = json.load(files)

           print(file)


        
        
    def display_fixtures(self, item):
        
        selected_item = item.text()
        fixtures = self.manufacturerFixtures.get(selected_item, [])

        self.fixtureList.clear()
        self.fixtureList.addItems(fixtures)

            


        

    def update_manufacturers(self): #Manufacturer Search bar

        search_entry = self.searchBar_Manufacturers.text().lower()

        for n in range(self.manufacturerList.count()):
            
            item = self.manufacturerList.item(n)
            
            if search_entry in item.text().lower():
                item.setHidden(False)
           
            else:
                item.setHidden(True)

    def update_fixtures(self): #Fixture Search bar

        search_entry = self.searchBar_Fixtures.text().lower()

        for n in range(self.fixtureList.count()):
            
            item = self.fixtureList.item(n)
            
            if search_entry in item.text().lower():
                item.setHidden(False)
           
            else:
                item.setHidden(True)



app = QApplication(sys.argv)
window = mainWindow()
app.exec_()
sys.exit(app.exec_())
