# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "guisettings.ui"
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
from guiMenu import *


class Ui_SettingsWindow(object):
    def __init__(self):
        # Get settings, set default when file not found
        self.lv = "1"
        self.lv_new = self.lv
        self.mu = "on"
        self.mu_new = self.mu
        try:
            l = open(".set_level", "r")
            self.lv = l.read()
            self.lv_new = self.lv
            l.close()
        except FileNotFoundError:
            l = open(".set_level", "w")
            l.write(self.lv)
            l.close()
        try:
            m = open(".set_music", "r")
            self.mu = m.read()
            self.mu_new = self.mu
            m.close()
        except FileNotFoundError:
            m = open(".set_music", "w")
            m.write(self.mu)
            m.close()
        # Button click sfx
        if self.mu == "on":
            self.buttClicked = QSound("buttClicked.wav")


    def openMain(self):
        from guiMenu import Ui_MainWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def buttAction(self, butt):
        if butt == "1":
            self.lv_new = "1"
        elif butt == "2":
            self.lv_new = "2"
        elif butt == "3":
            self.lv_new = "3"
        elif butt == "4":
            self.lv_new = "4"
        elif butt == "on":
            self.mu_new = "on"
        elif butt == "off":
            self.mu_new = "off"
        elif butt == "save":
            if self.lv_new != 0 and self.lv_new != self.lv:
                self.lv = self.lv_new
                l = open(".set_level", "w")
                l.write(self.lv)
                l.close()
            if self.mu_new != 0 and self.mu_new != self.mu:
                self.mu = self.mu_new
                m = open(".set_music", "w")
                m.write(self.mu)
                m.close()
        elif butt == "return":
            self.openMain()
        self.updateUi()
        # Play button click sound
        if self.mu == "on":
            self.buttClicked.play()


    def openLevel(self):
        import os
        os.system("game.py")


    def setupUi(self, SettingsWindow):
        # Main window
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(800, 600)
        SettingsWindow.setWindowIcon(QtGui.QIcon("pac.png"))
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 131, 41))
        # SETTINGS label
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 500, 41))
        # "Choose your difficulty" label
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # Button 1
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(120, 150, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        # Button 2
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(540, 150, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        # Button 3
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(120, 237, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        # Button 4
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(540, 237, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        # "Music" label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 320, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        # Button ON
        self.onButton = QtWidgets.QPushButton(self.centralwidget)
        self.onButton.setGeometry(QtCore.QRect(120, 390, 93, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.onButton.setFont(font)
        self.onButton.setObjectName("onButton")
        # Button OFF
        self.offButton = QtWidgets.QPushButton(self.centralwidget)
        self.offButton.setGeometry(QtCore.QRect(540, 390, 93, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.offButton.setFont(font)
        self.offButton.setObjectName("offButton")
        # Button SAVE
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(120, 490, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        # Button RETURN
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(540, 490, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.returnButton.setFont(font)
        self.returnButton.setObjectName("returnButton")
        SettingsWindow.setCentralWidget(self.centralwidget)
        # Menubar
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SettingsWindow.setMenuBar(self.menubar)
        # Statusbar
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)

        # Call buttAction
        #levels
        self.oneButton.clicked.connect(lambda: self.buttAction("1"))
        self.twoButton.clicked.connect(lambda: self.buttAction("2"))
        self.threeButton.clicked.connect(lambda: self.buttAction("3"))
        self.fourButton.clicked.connect(lambda: self.buttAction("4"))
        #music
        self.onButton.clicked.connect(lambda: self.buttAction("on"))
        self.offButton.clicked.connect(lambda: self.buttAction("off"))
        #save settings and retranslate UI
        self.saveButton.clicked.connect(lambda: self.buttAction("save"))
        #open main window and close
        self.returnButton.clicked.connect(lambda: self.buttAction("return"))
        self.returnButton.clicked.connect(SettingsWindow.close)
        
        # Update and retranslate GUI
        self.updateUi(SettingsWindow)
        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)


    def updateUi(self, SettingsWindow=None):
        # Color variables, to change the gui easily
        WINDOW_BG_COLOR = "#303030"
        LABEL_FG_COLOR = "#875faf"
        BUTTON_BG_COLOR = "#3a3a3a"
        BUTTON_FG_COLOR = "#5b5b5b"
        BUTTON_ACTIVE_BG_COLOR = "#5b5b5b"
        BUTTON_ACTIVE_FG_COLOR = "#dfdfdf"
        BUTTON_OP_BG_COLOR = "#875faf"
        # Color tuple, to put into formatted strings
        BUTTON_COLOR = (BUTTON_BG_COLOR, BUTTON_FG_COLOR)
        BUTTON_ACTIVE_COLOR = (BUTTON_ACTIVE_BG_COLOR, BUTTON_ACTIVE_FG_COLOR)
        # Set colors
        if SettingsWindow is not None:
            SettingsWindow.setStyleSheet("background-color: %s;"%WINDOW_BG_COLOR)
        self.label.setStyleSheet("color: %s;"%LABEL_FG_COLOR)
        self.label_2.setStyleSheet("color: %s;"%LABEL_FG_COLOR)
        self.oneButton.setStyleSheet("background-color: %s;\n"
                    "color: %s;"%(BUTTON_COLOR if self.lv_new != "1" else BUTTON_ACTIVE_COLOR))
        self.twoButton.setStyleSheet("background-color: %s;\n"
                    "color: %s;"%(BUTTON_COLOR if self.lv_new != "2" else BUTTON_ACTIVE_COLOR))
        self.threeButton.setStyleSheet("background-color: %s;\n"
                    "color: %s;"%(BUTTON_COLOR if self.lv_new != "3" else BUTTON_ACTIVE_COLOR))
        self.fourButton.setStyleSheet("background-color: %s;\n"
                    "color: %s;"%(BUTTON_COLOR if self.lv_new != "4" else BUTTON_ACTIVE_COLOR))
        self.label_3.setStyleSheet("color: %s;"%LABEL_FG_COLOR)
        self.onButton.setStyleSheet("background-color: %s;\n"
                    "color: %s;"%(BUTTON_COLOR if self.mu_new != "on" else BUTTON_ACTIVE_COLOR))
        self.offButton.setStyleSheet("background-color: %s;\n"
                    "color: %s;"%(BUTTON_COLOR if self.mu_new != "off" else BUTTON_ACTIVE_COLOR))
        self.saveButton.setStyleSheet("background-color: %s;"%BUTTON_OP_BG_COLOR)
        self.returnButton.setStyleSheet("background-color: %s;"%BUTTON_OP_BG_COLOR)


    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(
            _translate("SettingsWindow", "Settings"))
        self.label.setText(_translate("SettingsWindow", "SETTINGS"))
        self.label_2.setText(_translate(
            "SettingsWindow", "Choose your difficulty"))
        self.oneButton.setText(_translate("SettingsWindow", "1"))
        self.twoButton.setText(_translate("SettingsWindow", "2"))
        self.threeButton.setText(_translate("SettingsWindow", "3"))
        self.fourButton.setText(_translate("SettingsWindow", "4"))
        self.label_3.setText(_translate("SettingsWindow", "Music"))
        self.onButton.setText(_translate("SettingsWindow", "ON"))
        self.offButton.setText(_translate("SettingsWindow", "OFF"))
        self.saveButton.setText(_translate("SettingsWindow", "SAVE"))
        self.returnButton.setText(_translate("SettingsWindow", "RETURN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())
