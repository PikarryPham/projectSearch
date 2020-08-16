# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "guisettings.ui"
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from guiMenu import *


class Ui_SettingsWindow(object):
    def openMain(self):
        from guiMenu import Ui_MainWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def buttAction(self, butt):
        buttClicked = QtMultimedia.QSound("buttClicked.wav")
        # Get settings, set default when file not found
        l, m, lv, mu, lv_new, mu_new = None, None, 0, 0, 0, 0
        try:
            l = open("set_level", "r")
            lv = l.read()
            l.close()
        except:
            l = open("set_level", "w")
            l.write("1")
            lv = "1"
            l.close()
        try:
            m = open("set_music", "r")
            mu = m.read()
            m.close()
        except:
            m = open("set_music", "w")
            m.write("on")
            mu = "on"
            m.close()
        # Play button click sound
        buttClicked.play()
        if butt == 1:
            lv_new = "1"
        elif butt == 2:
            lv_new = "2"
        elif butt == 3:
            lv_new = "3"
        elif butt == 4:
            lv_new = "4"
        elif butt == "on":
            mu_new = "on"
        elif butt == "off":
            mu_new = "off"
        elif butt == "save":
            print (lv_new, lv)
            print (mu_new, mu)
            if lv_new != 0 and lv_new != lv:
                l = open("set_level", "w")
                l.write(lv_new)
                l.close()
                print(lv_new)
            if mu_new != 0 and mu_new != mu:
                m = open("set_music", "w")
                m.write(mu_new)
                m.close()
                print(mu_new)
        elif butt == "return":
            self.openMain()

    def openLevel(self):
        import os
        os.system("game.py")

    def setupUi(self, SettingsWindow):
        # Color variables, to change the gui easily
        WINDOW_BG_COLOR = "#303030"
        LABEL_FG_COLOR = "#875faf"
        BUTTON_BG_COLOR = "#5b5b5b"
        BUTTON_FG_COLOR = "#dfdfdf"
        BUTTON_PRESSED_BG_COLOR = "#3a3a3a"
        BUTTON_OP_BG_COLOR = "#875faf"
        
        # Main window
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(800, 600)
        SettingsWindow.setWindowIcon(QtGui.QIcon("pac.png"))
        SettingsWindow.setStyleSheet("background-color: %s;"%WINDOW_BG_COLOR)
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
        self.label.setStyleSheet("color: %s;"%LABEL_FG_COLOR)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 500, 41))
        # "Choose your difficulty" label
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: %s;"%LABEL_FG_COLOR)
        self.label_2.setObjectName("label_2")
        # Button 1
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(120, 150, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("background-color: %s;\n"
                                     "color: %s;"%(BUTTON_BG_COLOR, BUTTON_FG_COLOR))
        self.oneButton.setObjectName("oneButton")
        # Button 2
        self.twoButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton_2.setGeometry(QtCore.QRect(540, 150, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.twoButton_2.setFont(font)
        self.twoButton_2.setStyleSheet("background-color: %s;\n"
                                       "color: %s;"%(BUTTON_BG_COLOR, BUTTON_FG_COLOR))
        self.twoButton_2.setObjectName("twoButton_2")
        # Button 3
        self.threeButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton_3.setGeometry(QtCore.QRect(120, 237, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.threeButton_3.setFont(font)
        self.threeButton_3.setStyleSheet("background-color: %s;\n"
                                         "color: %s;"%(BUTTON_BG_COLOR, BUTTON_FG_COLOR))
        self.threeButton_3.setObjectName("threeButton_3")
        # Button 4
        self.fourButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton_4.setGeometry(QtCore.QRect(540, 237, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fourButton_4.setFont(font)
        self.fourButton_4.setStyleSheet("background-color: %s;\n"
                                        "color: %s;"%(BUTTON_BG_COLOR, BUTTON_FG_COLOR))
        self.fourButton_4.setObjectName("fourButton_4")
        # "Music" label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 320, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: %s;"%LABEL_FG_COLOR)
        self.label_3.setObjectName("label_3")
        # Button ON
        self.onButton = QtWidgets.QPushButton(self.centralwidget)
        self.onButton.setGeometry(QtCore.QRect(120, 390, 93, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.onButton.setFont(font)
        self.onButton.setStyleSheet("background-color: %s;\n"
                                    "color: %s;"%(BUTTON_BG_COLOR, BUTTON_FG_COLOR))
        self.onButton.setObjectName("onButton")
        # Button OFF
        self.offButton = QtWidgets.QPushButton(self.centralwidget)
        self.offButton.setGeometry(QtCore.QRect(540, 390, 93, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.offButton.setFont(font)
        self.offButton.setStyleSheet("background-color: %s;\n"
                                     "color: %s;"%(BUTTON_BG_COLOR, BUTTON_FG_COLOR))
        self.offButton.setObjectName("offButton")
        # Button SAVE
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(120, 490, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("background-color: %s;"%BUTTON_OP_BG_COLOR)
        self.saveButton.setObjectName("saveButton")
        # Button RETURN
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(540, 490, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.returnButton.setFont(font)
        self.returnButton.setStyleSheet("background-color: %s;"%BUTTON_OP_BG_COLOR)
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
        self.oneButton.clicked.connect(lambda: self.buttAction(1))
        self.twoButton_2.clicked.connect(lambda: self.buttAction(2))
        self.threeButton_3.clicked.connect(lambda: self.buttAction(3))
        self.fourButton_4.clicked.connect(lambda: self.buttAction(4))
        #music
        self.onButton.clicked.connect(lambda: self.buttAction("on"))
        self.offButton.clicked.connect(lambda: self.buttAction("off"))
        #save settings and retranslate UI
        self.saveButton.clicked.connect(lambda: self.buttAction("save"))
        self.saveButton.clicked.connect(lambda: self.retranslateUi(SettingsWindow))
        #open main window and close
        self.returnButton.clicked.connect(lambda: self.buttAction("return"))
        self.returnButton.clicked.connect(SettingsWindow.close)

        # Translate UI
        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        # Get settings, set default when file not found
        lv = mu = None
        try:
            l = open("set_level", "r")
            lv = l.read()
            l.close()
        except:
            lv = "1"
        try:
            m = open("set_music", "r")
            mu = m.read()
            m.close()
        except:
            mu = "on"
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(
            _translate("SettingsWindow", "Settings"))
        self.label.setText(_translate("SettingsWindow", "SETTINGS"))
        self.label_2.setText(_translate(
            "SettingsWindow", "Choose your difficulty (Current: %s)"%lv))
        self.oneButton.setText(_translate("SettingsWindow", "1"))
        self.twoButton_2.setText(_translate("SettingsWindow", "2"))
        self.threeButton_3.setText(_translate("SettingsWindow", "3"))
        self.fourButton_4.setText(_translate("SettingsWindow", "4"))
        self.label_3.setText(_translate("SettingsWindow", "Music (Current: %s)"%mu))
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
