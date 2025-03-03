import os
import sys,time
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLineEdit, QListWidget,
    QLineEdit, QTableWidget, QSlider, QLCDNumber, QLabel, QTableWidgetItem, 
    QPushButton, QComboBox, QCheckBox, QTabWidget, QWidget, QDial)
from PyQt5 import uic
from PyQt5.QtCore import QRectF


JSON_DIR = "fixtures"


class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()

        uic.loadUi("fixtureWindow.ui",self)

        self.manufacturerList = self.findChild(QListWidget, 
                                               "manufacturerList")
        self.fixtureList = self.findChild(QListWidget, "fixtureList")
        self.sceneList = self.findChild(QListWidget, "sceneList")

        self.searchBar_Manufacturers = self.findChild(
            QLineEdit,"searchBar_Manufacturers")
        self.searchBar_Fixtures = self.findChild(QLineEdit, 
                                                 "searchBar_Fixtures")
        self.searchBar_Scene = self.findChild(QLineEdit, "searchBar_Scene")

        self.fixtureInfo = self.findChild(QTableWidget, "fixtureInfo")

        self.fixtureAdd_btn = self.findChild(QPushButton, "fixtureAdd_btn")
        self.delFixture_btn = self.findChild(QPushButton, "delFixture_btn")
        self.fixtureSettings_btn = self.findChild(QPushButton, 
                                                  "fixtureSettings_btn")
        self.fixtureSettings_btn.setEnabled(False)

        self.fixtureChannel_lbl = self.findChild(QLabel, 
                                                 "fixtureChannel_lbl")
        self.blackout_btn = self.findChild(QPushButton, "blackout_btn")
        self.reset_btn = self.findChild(QPushButton, "reset_btn")

        global channel_lbl
        channel_lbl = self.fixtureChannel_lbl

        self.original_size = self.size()

        self.widget_data = {}
        for widget in self.findChildren(QWidget):
            self.widget_data[widget] = (widget.geometry(), self.size())

        
        #Event Handlers
        self.manufacturerFixtures = self.load_json_fixtures(
            "manufacturerFixtures.json")
        self.fixtureData = self.manufacturerList.currentRowChanged.connect(
            self.json_load)
        self.searchBar_Manufacturers.textChanged.connect(self.
                                                         update_manufacturers)
        self.searchBar_Fixtures.textChanged.connect(self.update_fixtures)
        self.searchBar_Scene.textChanged.connect(self.update_sceneList)
        self.manufacturerList.currentItemChanged.connect(self.
                                                         display_fixtures)
        self.fixtureList.itemClicked.connect(self.display_fixture_info)
        self.fixtureAdd_btn.clicked.connect(self.add_fixture)
        self.delFixture_btn.clicked.connect(self.delete_fixture)
        self.fixtureSettings_btn.clicked.connect(self.fixture_settings)
        self.reset_btn.clicked.connect(self.reset_faders)
        self.sceneList.itemClicked.connect(self.sceneList_item_clicked)
        self.blackout_btn.clicked.connect(self.blackout_btn_clicked)
        

        #Wheel Dials
        self.redWheel = self.findChild(QDial, "redWheel")
        self.greenWheel = self.findChild(QDial, "greenWheel")
        self.blueWheel = self.findChild(QDial, "blueWheel")

        #Wheel labels
        self.red_lbl = self.findChild(QLabel, "red_lbl")
        self.green_lbl = self.findChild(QLabel, "green_lbl")
        self.blue_lbl = self.findChild(QLabel, "blue_lbl")

        #Wheel LCDs
        self.red_lcd = self.findChild(QLCDNumber, "red_lcd")
        self.green_lcd = self.findChild(QLCDNumber, "green_lcd")
        self.blue_lcd = self.findChild(QLCDNumber, "blue_lcd")

        #Wheel event handlers
        self.redWheel.valueChanged.connect(self.redWheel_change)
        self.greenWheel.valueChanged.connect(self.greenWheel_change)
        self.blueWheel.valueChanged.connect(self.blueWheel_change)

        #Fader sliders
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

        #Fader labels
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

        #Fader LCDs
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


        #Fader event handlers
        self.ch1_fader.valueChanged.connect(self.ch1_lvl_change)
        self.ch2_fader.valueChanged.connect(self.ch2_lvl_change)
        self.ch3_fader.valueChanged.connect(self.ch3_lvl_change)
        self.ch4_fader.valueChanged.connect(self.ch4_lvl_change)
        self.ch5_fader.valueChanged.connect(self.ch5_lvl_change)
        self.ch6_fader.valueChanged.connect(self.ch6_lvl_change)
        self.ch7_fader.valueChanged.connect(self.ch7_lvl_change)
        self.ch8_fader.valueChanged.connect(self.ch8_lvl_change)
        self.ch9_fader.valueChanged.connect(self.ch9_lvl_change)
        self.ch10_fader.valueChanged.connect(self.ch10_lvl_change)
        self.ch11_fader.valueChanged.connect(self.ch11_lvl_change)
        self.ch12_fader.valueChanged.connect(self.ch12_lvl_change)
        self.ch13_fader.valueChanged.connect(self.ch13_lvl_change)
        self.ch14_fader.valueChanged.connect(self.ch14_lvl_change)
        self.ch15_fader.valueChanged.connect(self.ch15_lvl_change)
        self.ch16_fader.valueChanged.connect(self.ch16_lvl_change)
        self.ch17_fader.valueChanged.connect(self.ch17_lvl_change)
        self.ch18_fader.valueChanged.connect(self.ch18_lvl_change)
        self.ch19_fader.valueChanged.connect(self.ch19_lvl_change)
        self.ch20_fader.valueChanged.connect(self.ch20_lvl_change)
        self.ch21_fader.valueChanged.connect(self.ch21_lvl_change)
        self.ch22_fader.valueChanged.connect(self.ch22_lvl_change)
        self.ch23_fader.valueChanged.connect(self.ch23_lvl_change)
        self.ch24_fader.valueChanged.connect(self.ch24_lvl_change)
        self.ch25_fader.valueChanged.connect(self.ch25_lvl_change)
        self.ch26_fader.valueChanged.connect(self.ch26_lvl_change)
        self.ch27_fader.valueChanged.connect(self.ch27_lvl_change)
        self.ch28_fader.valueChanged.connect(self.ch28_lvl_change)
        self.master_fader.valueChanged.connect(self.master_lvl_change)
        
        self.show()

#Changes fader label and fader LCD based on fader position
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

# Changes wheel lcd and label based on wheel position
    def redWheel_change(self, value):
        self.red_lcd.display(str(value))

        if value > 0:
            self.red_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.red_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def greenWheel_change(self, value):
        self.green_lcd.display(str(value))

        if value > 0:
            self.green_lbl.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.green_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def blueWheel_change(self, value):
        self.blue_lcd.display(str(value))

        if value > 0:
            self.blue_lbl.setStyleSheet("color: rgb(0, 0, 255);")
        else:
            self.blue_lbl.setStyleSheet("color: rgb(255, 255, 255);")

    def json_load(self, index): #Locates json for selected fixture
        global file_path
        file_path = ("")

        global index_num
        index_num = index

        current_index = self.fixtureList.currentRow()
        
        if index == 0:
            file_path = os.path.join(JSON_DIR, "spica-250m.json")
            
        elif index == 1:
            file_path = os.path.join(JSON_DIR, "twister-4.json")
                
        elif index == 2:
            file_path = os.path.join(JSON_DIR, "par-180-cob-3in1.json")
                
        elif index == 3:
            
            

            fixture_files = ["alc4.json", "europe-105.json", "warp-m.json"]
            
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 4:
            file_path = os.path.join(JSON_DIR, "lmh460z.json")

        elif index == 5:
            file_path = os.path.join(JSON_DIR, "alien-s.json")
        
        elif index == 6:
            
            current_index = self.fixtureList.currentRow()

            fixture_files = ["7p-hex-ip.json", "12p-hex-ip.josn", 
                             "18p-hex-ip.json", "auto-spot-150.json", 
                             "boom-box-fx2.json", 
                             "cob-cannon-wash.json", 
                             "crazy-pocket-8.json", "dekker-led.json", 
                             "dotz-par.json", "encore-lp12z-ip.json", 
                             "encore-profile-1000-ww.json", 
                             "flat-par-qa12.json", 
                             "flat-par-qa12xs.json", 
                             "fog-fury-jett-pro.json", 
                             "galaxian-3d.json", 
                             "illusion-dotz-4-4.json",
                             "inno-pocket-beam-q4.json", 
                             "inno-pocket-fusion.json", 
                             "mega-bar-50rgb-rc.json", 
                             "mega-bar-50rgb.json", 
                             "mega-bar-rgba.json", "mega-hex-par.json", 
                             "mega-tripar-profile-plus.json", 
                             "mod-hex100.json", "pocket-pro.json", 
                             "quad-phase-hp.json", "revo-4-ir.json", 
                             "revo-burst.json", "revo-sweep.json", 
                             "saber-spot-rgbw.json", "starburst.json", 
                             "stinger-ii.json", "stinger-spot.json", 
                             "uv-eco-bar.json", "vbar-pak.json", 
                             "vizi-q-wash7.json", 
                             "vizi-spot-led-pro.json", "xs-400.json"]
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 7:
            file_path = os.path.join(JSON_DIR, "lightcan.json")

        elif index == 8:
            current_index = self.fixtureList.currentRow()

            fixture_files = ["ls-1200d-pro.json", "nova-p300c.json", 
                             "ls-600x-pro.json", "ls-300x.json", 
                             "ls-600d.json", "ls-600d-pro.json"]

            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 9:
            current_index = self.fixtureList.currentRow()

            fixture_files = ["l5-c.json", "broadcaster-2-plus.json", 
                             "l7-c.json", "skypanel-s30c.json", 
                             "skypanel-s120c.json", 
                             "skypanel-s360c.json", 
                             "skypanel-s60c.json", "l10-c.json"]
            
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 10:
            current_index = self.fixtureList.currentRow()

            fixture_files = ["fp2-helios-tube.json", 
                             "fp5-nyx-bulb.json", 
                             "fp1-titan-tube.json", 
                             "fp3-hyperion-tube.json", 
                             "ax3-lightdrop.json"]

            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 11:
            file_path = os.path.join(JSON_DIR, "boston-60.json")

        elif index == 12:
            current_index = self.fixtureList.currentRow()

            fixture_files = ["tdc-triple-burst.json", "compar-20.json"]

            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 13:
            current_index = self.fixtureList.currentRow()

            fixture_files = ["diablo-tc.json", "diablo-s.json", 
                             "magicblade-fx.json"]

            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 14:
            current_index = self.fixtureList.currentRow()

            fixture_files = ["triple-flex-centre-pro-led.json", 
                             "h2000-faze-machine.json", 
                             "panther-7r.json", "pls25-par.json"]

            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 15:
            current_index = self.fixtureList.currentRow()

            fixture_files = ["ls90.json", "lp001.json"]

            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[
                    current_index])

        elif index == 16:
            file_path = os.path.join(JSON_DIR, "companion-v2.json")

        elif index == 17:
            fixture_files = ['hotbox-exa.json', 'hotbox-rgbw.json', 'puck-rgbaw.json', 'rokbox-rgbw.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 18:
            fixture_files = ['crazy-spot-30.json', 'silentpar-12x10w-5in1.json', 'silentpar-12x10w-6in1.json', 'silentpar-12x3w-3in1.json', 'silentpar-5x10w-5in1.json', 'silentpar-5x10w-6in1.json', 'silentpar-5x3w-3in1.json', 'silentpar-7x10w-5in1.json', 'silentpar-7x10w-6in1.json', 'silentpar-7x3w-3in1.json', 'xtrem-led.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 19:
            fixture_files = ['beam-fury-1.json', 'beamspot1-dmx-fc.json', 'bt-coloray-120r.json', 'bt-coloray-18fcr.json', 'bt-coloray-60r.json', 'bt-ledrotor.json', 'bt-stagepar-6in1.json', 'btx-cirrus-ii.json', 'btx-titan.json', 'cob-slim-100-rgb.json', 'pro-beamer-zoom-indoor.json', 'pro-beamer-zoom-outdoor.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 20:
            fixture_files = ['auro-beam-150.json', 'auro-spot-100.json', 'auro-spot-200.json', 'auro-spot-300.json', 'auro-spot-400.json', 'flash-matrix-250.json', 'flat-par-can-rgb-10-ir.json', 'flat-par-can-tri-5x-3w-ir.json', 'flat-par-can-tri-7x-3w-ir.json', 'flat-pro-18.json', 'flat-pro-flood-600-ip65.json', 'flat-pro-flood-ip65-tri.json', 'gobo-scanner-80.json', 'hydrabeam-100.json', 'hydrabeam-300-rgbw.json', 'hydrabeam-400-rgbw.json', 'instant-air-1000-pro.json', 'instant-air-2000-pro.json', 'instant-hazer-1500-t-pro.json', 'ioda-1000-rgb.json', 'ioda-400-rgy.json', 'ioda-600-rgb.json', 'multi-fx-bar.json', 'multi-par-cob-1.json', 'nanospot-120.json', 'outdoor-par-tri-12.json', 'q-spot-40-cw.json', 'q-spot-40-rgbw.json', 'root-par-6.json', 'steam-wizard-1000.json', 'steam-wizard-2000.json', 'storm.json', 'thunder-wash-100-rgb.json', 'thunder-wash-100-w.json', 'thunder-wash-600-rgb.json', 'thunder-wash-600-rgbw.json', 'thunder-wash-600-w.json', 'ts-100-ww.json', 'ts-200-fc.json', 'ts-60-rgbw.json', 'zenit-w600.json', 'zenit-z120.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 21:
            fixture_files = ['colorband-pix-ip.json', 'colorband-pix.json', 'corepar-uv-usb.json', 'dmx-4.json', 'eve-p-100-ww.json', 'eve-p-130-rgb.json', 'freedom-h1.json', 'geyser-rgb.json', 'gigbar-2.json', 'hurricane-1600.json', 'hurricane-haze-1dx.json', 'hurricane-haze-2d.json', 'intimidator-spot-110.json', 'intimidator-spot-160.json', 'intimidator-spot-260.json', 'kinta-x.json', 'led-par-64-tri-b.json', 'megastrobe-fx12.json', 'motiondrape-led.json', 'slimpar-pro-h-usb.json', 'slimpar-pro-qz12.json', 'slimpar-pro-rgba.json', 'slimpar-pro-w.json', 'slimpar-q12-bt.json', 'slimpar-t12-bt.json', 'slimpar-t12-usb.json', 'washfx.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 22:
            fixture_files = ['colorado-1-solo.json', 'colordash-batten-quad-6.json', 'colordash-s-par-1.json', 'ovation-f-915vw.json', 'rogue-r1-wash.json', 'rogue-r2-wash.json', 'vesuvio-rgba.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 23:
            fixture_files = ['color-force-ii-12.json', 'color-force-ii-48.json', 'color-force-ii-72.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 24:
            file_path = os.path.join(JSON_DIR, 'par-18x15w-rgbwa.json')

        elif index == 25:
            fixture_files = ['a-leda-b-eye-k10.json', 'a-leda-b-eye-k20.json', 'alpha-spot-qwo-800.json', 'sharpy.json', 'show-batten-100.json', 'spheriscan.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 26:
            file_path = os.path.join(JSON_DIR, 'hera.json')

        elif index == 27:
            file_path = os.path.join(JSON_DIR, 'prospot-250-lx.json')

        elif index == 28:
            fixture_files = ['irled64-18x12six.json', 'irledflat-5x12SIXb.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 29:
            fixture_files = ['dled4-bi.json', 'dled7-bi.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 30:
            fixture_files = ['softled-4-vw.json', 'softled-8-vw.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 31:
            fixture_files = ['maxi-mix.json', 'mini-mix.json', 'sl1-mix.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 32:
            fixture_files = ['scena-led-150.json', 'xr1200-wash.json', 'xr4-spot.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 33:
            fixture_files = ['acl-360-roller.json', 'cuepix-blinder-ww2.json', 'cuepix-blinder-ww4.json', 'design-led-par-zoom.json', 'fuze-par-z60ip.json', 'platinum-hfx.json', 'platinum-seven.json', 'platinum-spot-15r-pro.json', 'proteus-hybrid.json', 'sixpar-100-ip.json', 'sixpar-100.json', 'sixpar-200-ip.json', 'sixpar-200-wmg.json', 'sixpar-200.json', 'sixpar-300-ip.json', 'sixpar-300-wmg.json', 'sixpar-300.json', 'uni-bar.json', 'zw19.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 34:
            fixture_files = ['stealth-beam.json', 'stealth-wash-zoom.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 35:
            file_path = os.path.join(JSON_DIR, '8x-3w-led-spider-effect.json')

        elif index == 36:
            file_path = os.path.join(JSON_DIR, 'duo-q-beam-bar.json')

        elif index == 37:
            fixture_files = ['gigabar.json', 'rgb-power-batten.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 38:
            fixture_files = ['colorsource-par-deep-blue.json', 'colorsource-par.json', 'colorsource-spot-deep-blue.json', 'colorsource-spot.json', 'fos4PD16.json', 'fos4PD24.json', 'fos4PD8.json', 'fos4PL16.json', 'fos4PL24.json', 'fos4PL8.json', 'source-4wrd-color-ii.json', 'source-four-led-series-2-daylight-hd.json', 'source-four-led-series-2-lustr.json', 'source-four-led-series-2-tungsten-hd.json', 'source-four-led-series-3-daylight-hdr.json', 'source-four-led-series-3-lustr-x8.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 39:
            fixture_files = ['edx-4.json', 'led-7c-7-silent-slim.json', 'led-b-40.json', 'led-bar-12-qcl-rgba-bar.json', 'led-bar-3-hcl-bar.json', 'led-bar-6-qcl-rgbw.json', 'led-big-party-spot.json', 'led-big-party-tcl-spot.json', 'led-dmx-pixel-tube-16-rgb-ip20.json', 'led-fe-1500.json', 'led-h2o.json', 'led-kls-801.json', 'led-ml-56-rgbw.json', 'led-par-56-tcl.json', 'led-party-spot.json', 'led-party-tcl-spot.json', 'led-pix-12-hcl.json', 'led-pix-144.json', 'led-ps-4-hcl.json', 'led-sls-12-bcl.json', 'led-sls-5-bcl.json', 'led-sls-6-uv-floor.json', 'led-svf-1.json', 'led-tha-100f-mk2.json', 'led-tha-100f.json', 'led-theatre-cob-200-rgb-ww.json', 'led-tl-3-rgb-uv.json', 'led-tl-4-qcl.json', 'led-tmh-14.json', 'led-tmh-17.json', 'led-tmh-18.json', 'led-tmh-7.json', 'led-tmh-8.json', 'led-tmh-9.json', 'led-tmh-x12.json', 'led-tmh-x25.json', 'led-z-200-tcl.json', 'md-2030.json', 'multiflood-pro-ip-smd-rgbw.json', 'n-150.json', 'tmh-xb-130.json', 'ts-2.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 40:
            fixture_files = ['par12x12.json', 'par5x12.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 41:
            file_path = os.path.join(JSON_DIR, 'colours-archspot-54-rgb.json')

        elif index == 42:
            fixture_files = ['gasprojector-gx2.json', 'x2-wave-flamer.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 43:
            file_path = os.path.join(JSON_DIR, 'led-rgbw-54x3-par64.json')

        elif index == 44:
            file_path = os.path.join(JSON_DIR, 'p3-color.json')

        elif index == 45:
            fixture_files = ['led-moving-head-150w.json', 'led-par-64-cob-300w-rgbwauv.json', 'led-par-64-slim-7x10w-rgbw-mk2.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 46:
            file_path = os.path.join(JSON_DIR, '600xb.json')

        elif index == 47:
            fixture_files = ['par-led-7x10w.json', 'par-led-7x12w.json', 'par-led-7x9w.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 48:
            fixture_files = ['led-pot-12-1w-rgbw.json', 'led-pot-12x1w-qcl-rgb-ww-15.json', 'led-pot-12x1w-qcl-rgb-ww-40.json', 'picobeam-30-quad-led.json', 'picobeam-60-cob-rgbw.json', 'picoblade-fx-4x10w-rgbw.json', 'picospot-20-led.json', 'picospot-45-led.json', 'picowash-40-pixel-quad-led.json', 'separ-hex-led-rgbaw-uv.json', 'separ-quad-led-rgb-uv.json', 'separ-quad-led-rgbw.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 49:
            fixture_files = ['dj-scan-250.json', 'dmh-75-i-led-moving-head.json', 'pro-slim-par-7-hcl.json', 'sc-250-scanner.json', 'stb-648-led-strobe-smd-5050.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 50:
            file_path = os.path.join(JSON_DIR, 'g-flame.json')

        elif index == 51:
            file_path = os.path.join(JSON_DIR, 'precision-dmx.json')

        elif index == 52:
            fixture_files = ['4-channel-dimmer-pack.json', 'cmy-fader.json', 'color-temperature-fader.json', 'cw-ww-fader.json', 'desk-channel.json', 'drgb-fader.json', 'drgbw-fader.json', 'grbw-fader.json', 'pan-tilt.json', 'rgb-fader.json', 'rgba-fader.json', 'rgbd-fader.json', 'rgbw-fader.json', 'rgbwauv-fader.json', 'rgbww-fader.json', 'strobe.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 53:
            fixture_files = ['ip-spot-bat.json', 'ip-spot-pro.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 54:
            fixture_files = ['force-120.json', 'impression-fr1.json', 'impression-laser.json', 'impression-spot-one.json', 'impression-x4-bar-10.json', 'jdc1.json', 'knv-arc.json', 'knv-cube.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 55:
            file_path = os.path.join(JSON_DIR, 'gls-4-led-stage-4.json')

        elif index == 56:
            file_path = os.path.join(JSON_DIR, 'kolorado-4000.json')

        elif index == 57:
            fixture_files = ['pixel-tube.json', 'ventilator.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 58:
            file_path = os.path.join(JSON_DIR, 'base-hazer-pro.json')

        elif index == 59:
            fixture_files = ['bee-50-c.json', 'bumble-bee-25-cx.json', 'hornet-200-c.json', 'hornet-200-cx.json', 'super-hornet-575-c.json', 'wasp-100-c.json', 'wasp-100-cx.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 60:
            file_path = os.path.join(JSON_DIR, 'hy-g60.json')

        elif index == 61:
            file_path = os.path.join(JSON_DIR, '40w-beam-spot-light-rgbw.json')

        elif index == 62:
            fixture_files = ['lp64-led-promo.json', 'ls-005led.json', 'par-mini-rgb3.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 63:
            fixture_files = ['2bright-par-18-ip.json', 'led-accu-par.json', 'teatro-led-spot-100-fr.json', 'teatro-led-spot-100-pc.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 64:
            file_path = os.path.join(JSON_DIR, 'stryder-sfb150.json')

        elif index == 65:
            fixture_files = ['iw-340-rdm.json', 'iw-720-rdm.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 66:
            fixture_files = ['jbled-a7.json', 'varyscan-p7.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 67:
            fixture_files = ['imove-5s.json', 'irock-5c.json', 'twin-effect-laser.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 68:
            file_path = os.path.join(JSON_DIR, 'gobotracer.json')

        elif index == 69:
            fixture_files = ['celeb-250-led-dmx.json', 'celeb-450-led-dmx.json', 'celeb-led-201-dmx.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 70:
            fixture_files = ['18leds-par-light.json', 'dj-lights.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 71:
            fixture_files = ['cs-1000rgb.json', 'ds-1000rgb.json', 'el-400rgb-mk2.json', 'shownet.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 72:
            fixture_files = ['slimline-12q5-rgba.json', 'slimline-12q5-rgbw.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 73:
            file_path = os.path.join(JSON_DIR, 'diamond-pro-2-8.json')

        elif index == 74:
            file_path = os.path.join(JSON_DIR, 'aurora.json')

        elif index == 75:
            file_path = os.path.join(JSON_DIR, 'led-par-18x3w-uv.json')

        elif index == 76:
            fixture_files = ['cls-nano-cob.json', 'dj-scan-led.json', 'easy-wash-quad-led.json', 'led-nano-par.json', 'led-par-56.json', 'platinum-mini-tri-par.json', 'vector-haze-1-0.json', 'vector-pixel-bar-18x-15w-rgbwa.json', 'vega-bat-1.json', 'vega-zoom-wash.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 77:
            file_path = os.path.join(JSON_DIR, 'beam-230.json')

        elif index == 78:
            file_path = os.path.join(JSON_DIR, 'washx-21.json')

        elif index == 79:
            fixture_files = ['litemat-plus-1.json', 'litemat-plus-2.json', 'litemat-plus-2l.json', 'litemat-plus-3.json', 'litemat-plus-4.json', 'litemat-plus-8.json', 'litetile-plus-4.json', 'litetile-plus-8.json', 's2-litemat-1.json', 's2-litemat-2.json', 's2-litemat-2l.json', 's2-litemat-3.json', 's2-litemat-4.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 80:
            fixture_files = ['mini-beam-rgbw.json', 'mini-gobo-moving-head-light.json', 'mini-moving-head-rgbw.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 81:
            fixture_files = ['cryofog.json', 'viper-nt.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 82:
            fixture_files = ['actionpanel-dual-color.json', 'actionpanel-full-color.json', 'superpanel-dual-color-60.json', 'superpanel-full-color-60.json', 'superpanelpro-dual-color-30.json', 'superpanelpro-full-color-30.json', 'ultrapanel-dual-color-60.json', 'ultrapanel-full-color-60.json', 'ultrapanelpro-dual-color-30.json', 'ultrapanelpro-full-color-30.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 83:
            fixture_files = ['psyco2jet.json', 'smokejet.json', 'stage-flame.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 84:
            fixture_files = ['mbar-381-ip.json', 'superbat-led-72.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 85:
            fixture_files = ['atomic-3000.json', 'mac-250-beam.json', 'mac-250-krypton.json', 'mac-250-wash.json', 'mac-600.json', 'mac-700-wash.json', 'mac-aura.json', 'mac-axiom-hybrid.json', 'mac-encore-performance.json', 'mac-viper-airfx.json', 'mac-viper-performance.json', 'mac-viper-wash.json', 'magnum-2500-hz.json', 'mania-scx500.json', 'mx-10-extreme.json', 'roboscan-812.json', 'rush-mh-2-wash.json', 'rush-mh-3-beam.json', 'rush-mh-5-profile.json', 'rush-mh-7-hybrid.json', 'rush-par-2-rgbw-zoom.json', 'rush-scanner-1-led.json', 'stagebar-54l.json', 'stagebar-54s.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 86:
            fixture_files = ['hazer-atmosphere-aps.json', 'theone-atmospheric-generator.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 87:
            fixture_files = ['led-par-light-372.json', 'zoom-360.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 88:
            fixture_files = ['framebot-600.json', 'mw1.json', 'spotbot-led-cmy-300.json', 'washbot-led-cymk-300.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 89:
            file_path = os.path.join(JSON_DIR, 'ivl-carre.json')

        elif index == 90:
            fixture_files = ['led-bar-123-fc-ip.json', 'pat-252.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 91:
            file_path = os.path.join(JSON_DIR, 'orcan2.json')

        elif index == 92:
            fixture_files = ['pt-rz120.json', 'pt-rz120l.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 93:
            file_path = os.path.join(JSON_DIR, 'box-leds-batterie-6x15w.json')

        elif index == 94:
            file_path = os.path.join(JSON_DIR, 'wash-84w.json')

        elif index == 95:
            file_path = os.path.join(JSON_DIR, 'xs-250-spot.json')

        elif index == 96:
            fixture_files = ['diamond19.json', 'pixpan16.json', 'polar3000.json', 'smartbat.json', 'v700spot.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 97:
            fixture_files = ['lux-ld01.json', 'lux-ld30w.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 98:
            file_path = os.path.join(JSON_DIR, 'gm107.json')

        elif index == 99:
            fixture_files = ['colorspot-2500e-at.json', 'dj-scan-250-xt.json', 'robin-300e-wash.json', 'robin-600e-spot.json', 'robin-ledbeam-100.json', 'robin-ledbeam-150.json', 'robin-ledwash-600.json', 'robin-parfect-150.json', 'robin-t1-profile.json', 'robin-viva-cmy.json', 'spot-160-xt.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 100:
            file_path = os.path.join(JSON_DIR, '613sx.json')

        elif index == 101:
            file_path = os.path.join(JSON_DIR, 'rockpar50.json')

        elif index == 102:
            file_path = os.path.join(JSON_DIR, 'p-5.json')

        elif index == 103:
            fixture_files = ['led-flat-par-12x3w-rgbw.json', 'led-flat-par-18x18w.json', 'led-flat-par-54x3w.json', 'led-flat-par-7x18w-rgbwa-uv-light.json', 'led-par-18x18w.json', 'led-spot-60w.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 104:
            file_path = os.path.join(JSON_DIR, 'sl-nitro-510c.json')

        elif index == 105:
            file_path = os.path.join(JSON_DIR, 'lb-4390.json')

        elif index == 106:
            file_path = os.path.join(JSON_DIR, 'litebar-h9.json')

        elif index == 107:
            fixture_files = ['accent-spot-q4-rgbw.json', 'archi-painter-24-8-q4.json', 'atmos-2000.json', 'club-par-12-4-rgbw.json', 'club-par-12-6-rgbwauv.json', 'compact-par-18.json', 'compact-par-7-tri.json', 'dim-4lc.json', 'dominator.json', 'explorer-250-wash-pro.json', 'horizon-8.json', 'kanjo-spot-60.json', 'kanjo-wash-rgb.json', 'led-blinder-2-cob.json', 'led-light-bar-rgb-v3.json', 'performer-2500.json', 'phantom-140-led-spot.json', 'phantom-25-led-wash.json', 'phantom-3r-beam.json', 'phantom-50-led-spot.json', 'phantom-matrix-fx.json', 'pixel-bar-12-mkii.json', 'sunraise-led.json', 'sunstrip-active-mkii.json', 'xs-1-rgbw.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 108:
            fixture_files = ['sparkular-fall.json', 'sparkular.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 109:
            file_path = os.path.join(JSON_DIR, 'mx-indigo-6000xe.json')

        elif index == 110:
            file_path = os.path.join(JSON_DIR, 'ribalta-beam.json')

        elif index == 111:
            fixture_files = ['data-ii.json', 'tour-hazer-ii.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 112:
            file_path = os.path.join(JSON_DIR, 'smart-36.json')

        elif index == 113:
            fixture_files = ['max-par-20.json', 'mini-par-12.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 114:
            file_path = os.path.join(JSON_DIR, '3204r-h.json')

        elif index == 115:
            fixture_files = ['mini-beam-rgbw.json', 'stage-wash-7x10w-led-moving-head.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 116:
            fixture_files = ['af-180-led-fogger.json', 'af-250.json', 'afh-600.json', 'bel6-ip-bar-hex.json', 'clb5-2p-rgb-ww-compact-led-par.json', 'hz-200-compact-hazer.json', 'led-bar-240-8.json', 'led-flood-panel-150.json', 'led-par-56.json', 'led-par-64.json', 'matrixx-sc-100.json', 'mh-100.json', 'mh-x20.json', 'mh-x25.json', 'mh-x30-led-spot.json', 'mh-x50.json', 'mh-x60.json', 'octagon-theater-20x6w-cw-ww-a.json', 'par-56.json', 'remus-hexspot-515.json', 'revueled-120-cob-rgbww.json', 'revueled-120-cob-true-white.json', 'stage-tri-led.json', 'vf-1200-dmx-vertifog-co2-fx.json', 'wild-wash-132-led-rgb-dmx.json', 'wild-wash-648-led-white-dmx.json', 'xbrick-full-colour.json', 'xbrick-quad-16x8w-rgbw.json', 'z120m-par-64-led-rgbw-120w.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 117:
            fixture_files = ['servo-color-4k.json', 'stickolor-1210uhd.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 118:
            file_path = os.path.join(JSON_DIR, 'light-deflector.json')

        elif index == 119:
            file_path = os.path.join(JSON_DIR, 'g-2011-nova.json')

        elif index == 120:
            fixture_files = ['nebula-18.json', 'nebula-6.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 121:
            file_path = os.path.join(JSON_DIR, '3-10w-battery-led-wedge-par.json')

        elif index == 122:
            file_path = os.path.join(JSON_DIR, 'solaris-flare.json')

        elif index == 123:
            file_path = os.path.join(JSON_DIR, '3-led-par-light-rgbuv.json')

        elif index == 124:
            fixture_files = ['b117-par-can-4in1-rgbw-18-leds.json', 'mini-led-spot-25w.json', 'par-light-b262.json', 'zq-b20-mini-spider-light.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 125:
            file_path = os.path.join(JSON_DIR, 'radiance-hazer.json')

        elif index == 126:
            fixture_files = ['bat-par-6-rgbuv.json', 'bat-par-6-rgbwa.json', 'easy-move-xs-hp-wash-7x8w-rgbw.json', 'giga-bar-frost-pix-8-rgb.json', 'giga-bar-hex-3.json', 'hero-wash-340fx-rgbw-zoom.json', 'led-hellball-3-rgb.json', 'led-theater-spot-100.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        elif index == 127:
            file_path = os.path.join(JSON_DIR, 'aeron-250-ii.json')

        elif index == 128:
            fixture_files = ['thintri64.json', 'tristrip3z.json']
            if 0 <= current_index < len(fixture_files):
                file_path = os.path.join(JSON_DIR, fixture_files[current_index])

        return file_path, index_num

    def load_json_fixtures(self, filename): #Loads selected json

        file_path = os.path.join(JSON_DIR, filename)

        with open(file_path, "r") as file:
                return json.load(file)

    def display_fixture_info(self, item): #Displays fixture categories and
                                          #modes in table

        self.json_load(index_num)
        
        with open(file_path, 'r') as file:
           global data
           data = json.load(file)

           global modes
        
           categories = ", ".join(data.get("categories", []))
           modes = ", ".join(mode["name"] for mode in data.get("modes", []))

           self.fixtureInfo.setItem(0, 0, QTableWidgetItem(categories))
           self.fixtureInfo.setItem(0, 1, QTableWidgetItem(modes)) 
    
           print(file_path) #TESTING

    def display_fixtures(self, item): #Displays fixtures in fixtureList when
                                      #manufacturer is selected
        
        selected_item = item.text()
        fixtures = self.manufacturerFixtures.get(selected_item, [])
        
        print(selected_item) #TESTING

        self.fixtureList.clear()
        self.fixtureList.addItems(fixtures)

    def add_fixture(self): #Add fixtures to sceneList

        selected_fixture = self.fixtureList.currentItem()
        fixture = selected_fixture.text()
        print(f"{fixture} added to sceneList")

        self.sceneList.addItem(fixture)

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

    def update_sceneList(self): #Scene list search bar
        
        search_entry = self.searchBar_Scene.text().lower()

        for n in range(self.sceneList.count()):

            item = self.sceneList.item(n)

            if search_entry in item.text().lower():
                item.setHidden(False)
            
            else:
                item.setHidden(True)

    def delete_fixture(self): #Delete fixture from sceneList
        item = self.sceneList.currentItem()
        row = self.sceneList.row(item)
        self.sceneList.takeItem(row)

        print(f"{item} deleted from sceneList")

    def fixture_settings(self): #Open fixture settings window - linked to 
                                #selected fixture
        self.settings_window = FixtureSettingsWindow()
        self.settings_window.show()

    def reset_faders(self): #Resets all faders to position 0
        
        self.ch1_fader.setSliderPosition(0)
        self.ch2_fader.setSliderPosition(0)
        self.ch3_fader.setSliderPosition(0)
        self.ch4_fader.setSliderPosition(0)
        self.ch5_fader.setSliderPosition(0)
        self.ch6_fader.setSliderPosition(0)
        self.ch7_fader.setSliderPosition(0)
        self.ch8_fader.setSliderPosition(0)
        self.ch9_fader.setSliderPosition(0)
        self.ch10_fader.setSliderPosition(0)
        self.ch11_fader.setSliderPosition(0)
        self.ch12_fader.setSliderPosition(0)
        self.ch13_fader.setSliderPosition(0)
        self.ch14_fader.setSliderPosition(0)
        self.ch15_fader.setSliderPosition(0)
        self.ch16_fader.setSliderPosition(0)
        self.ch17_fader.setSliderPosition(0)
        self.ch18_fader.setSliderPosition(0)
        self.ch19_fader.setSliderPosition(0)
        self.ch20_fader.setSliderPosition(0)
        self.ch21_fader.setSliderPosition(0)
        self.ch22_fader.setSliderPosition(0)
        self.ch23_fader.setSliderPosition(0)
        self.ch24_fader.setSliderPosition(0)
        self.ch25_fader.setSliderPosition(0)
        self.ch26_fader.setSliderPosition(0)
        self.ch27_fader.setSliderPosition(0)
        self.ch28_fader.setSliderPosition(0)
        self.master_fader.setSliderPosition(0)

        fader_pos = (self.ch1_fader.value(), self.ch2_fader.value(), #TESTING ONLY
                     self.ch3_fader.value(), self.ch4_fader.value(), 
                     self.ch5_fader.value(), self.ch6_fader.value(), 
                     self.ch7_fader.value(), self.ch8_fader.value(), 
                     self.ch9_fader.value(), self.ch10_fader.value(), 
                     self.ch11_fader.value(), self.ch12_fader.value(), 
                     self.ch13_fader.value(), self.ch14_fader.value(), 
                     self.ch15_fader.value(), self.ch16_fader.value(), 
                     self.ch17_fader.value(), self.ch18_fader.value(), 
                     self.ch19_fader.value(), self.ch20_fader.value(), 
                     self.ch21_fader.value(), self.ch22_fader.value(), 
                     self.ch23_fader.value(), self.ch24_fader.value(), 
                     self.ch25_fader.value(), self.ch26_fader.value(), 
                     self.ch27_fader.value(), self.ch28_fader.value(), 
                     self.master_fader.value())

        print(f"TESTING - reset: fader pos:{fader_pos}")

        if fader_pos == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
            print("Reset successful")
        else:
            print("Reset error")

    def sceneList_item_clicked(self, index): #Enables fixture settings button when item is selected
        global selected_item
        
        selected_item = self.sceneList.currentItem().text()

        print(selected_item)
        
        if index != None:
            self.fixtureSettings_btn.setEnabled(True)
        else:
            self.fixtureSettings_btn.setEnabled(False)

    def blackout_btn_clicked(self): #Sets master fader only to positon 0
        self.master_fader.setSliderPosition(0)

        print(f"TESTING - blackout: master pos:{self.master_fader.value()}")
        
        if self.master_fader.value() == 0:
            print("Blackout successful")
        else:
            print("Blackout error")

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)  # Set initial size
        
        self.button1 = QPushButton("Button 1", self)
        self.button1.setGeometry(50, 50, 200, 50)

        self.button2 = QPushButton("Button 2", self)
        self.button2.setGeometry(300, 50, 200, 50)
    
    def resizeEvent(self, event):
        new_size = self.size()
        
        for widget, (original_geometry, original_window_size) in self.widget_data.items():

            x_ratio = new_size.width() / original_window_size.width()
            y_ratio = new_size.height() / original_window_size.height()
            
            new_geometry = QRectF(original_geometry)
            new_geometry.setX(original_geometry.x() * x_ratio)
            new_geometry.setY(original_geometry.y() * y_ratio)
            new_geometry.setWidth(original_geometry.width() * x_ratio)
            new_geometry.setHeight(original_geometry.height() * y_ratio)

            widget.setGeometry(new_geometry.toRect())

        super().resizeEvent(event)

class FixtureSettingsWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("fixtureSettings.ui", self)
        

        self.settingsTab = self.findChild(QTabWidget, "settingsTab")
        self.fixtureType_lbl = self.findChild(QLabel, "fixtureType_lbl")
        self.fixtureType = self.findChild(QLabel, "fixtureType")
        self.fixtureName_lbl = self.findChild(QLabel, "fixtureName_lbl")
        self.fixtureName = self.findChild(QLineEdit, "fixtureName")
        self.selectedFixture_lbl = self.findChild(QLabel, 
                                                  "selectedFixture_lbl")
        self.selectedFixture = self.findChild(QLineEdit, "selectedFixture")
        self.close_btn = self.findChild(QPushButton, "close_btn")
        self.charLimit_lbl = self.findChild(QLabel, "charLimit_lbl")
        self.charLimit_lbl.setHidden(True)
        self.noText_lbl = self.findChild(QLabel, "noText_lbl")
        self.noText_lbl.setHidden(True)

        self.fixtureSettings_tab = self.findChild(QWidget, 
                                                  "fixtureSettings_tab")
        self.saveName_btn = self.findChild(QPushButton, "saveName_btn")
        self.mode_lbl = self.findChild(QLabel, "mode_lbl")
        self.mode_select = self.findChild(QComboBox, "mode_selection")
        self.dmxAddress_lbl = self.findChild(QLabel, "dmxAddress_lbl")
        self.dmxAddress = self.findChild(QLineEdit, "DMXAddress")
        self.dmx_update = self.findChild(QPushButton, "dmx_update")
        self.showFixture_lbl = self.findChild(QLabel, "showFixture_lbl")
        self.showFixture = self.findChild(QCheckBox, "showFixture_checkbox")

        self.patchSettings_tab = self.findChild(QTabWidget, 
                                                "patchSettings_tab")
        self.faderPatch_lbl = self.findChild(QLabel, "faderPatch_lbl")
        self.faderPatch = self.findChild(QComboBox, "channelSelection")
        self.fixtureChannels_lbl = self.findChild(QLabel, 
                                                  "fixtureChannels_lbl")
        self.fixtureChannels_list = self.findChild(QListWidget, 
                                                   "fixtureChannels_list")
        self.update_availableChannels = self.findChild(QPushButton, 
                                                       "update_availableChannels")
        self.updateFader = self.findChild(QPushButton, "updateFader")
        self.main_window = mainWindow
        
        global selected_item
        self.selectedFixture.setText(selected_item)

        #Event handlers
        self.saveName_btn.clicked.connect(self.save_name)
        self.close_btn.clicked.connect(self.close_settings_window)
        self.dmx_update.clicked.connect(self.update_fixture_dmx)
        self.updateFader.clicked.connect(self.fader_patch)
        self.update_availableChannels.clicked.connect(self.update_available_channels)
        mode_items = modes.split(", ")
        self.mode_select.addItems(mode_items)

    def save_name(self): #Save inputed name to fixture
        name = self.fixtureName.text()
        
        if len(name) <= 16:
            self.charLimit_lbl.setHidden(True)

            if not name:
                self.noText_lbl.setHidden(False)
            else:
                self.fixtureType.setText(name)
        else:
            self.charLimit_lbl.setHidden(False)
        if not name:
            self.noText_lbl.setHidden(False)
                
    def close_settings_window(self): #Closes fixture settings
        self.close()

    def update_fixture_dmx(self): #Update fixture DMX Address
        entry = int(self.dmxAddress.text())
        fixture = selected_item

        if entry > 512:
            print("This program only supports one universe")
        
        else:
            print(f"DMX Address for {fixture} updated to: {entry}")

    def fader_patch(self): #Patch fixtures to one of 28 channels
        global selected_item
        global channel_lbl
        fader = self.faderPatch.currentText()
        channel_lbl.setText(fader)


        print(f"{selected_item} patched to {fader}")
        
    def update_available_channels(self): #Updates and prints available channels per fixture
        global data

        availableChannels = ", ".join(data.get("availableChannels", []))
        print(f"Available Channels: {availableChannels}")
        
        channels = availableChannels.split(", ")
        self.fixtureChannels_list.addItems(channels)


#Main code
app = QApplication(sys.argv)
window = mainWindow()
app.exec_()
sys.exit(app.exec_())