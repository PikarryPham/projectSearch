# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guipacman.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# tải thêm module PyQt5 này về nghen
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def openSettings(self):
        from guisettings import Ui_SettingsWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPacman(self):
        import os
        os.system('pacman.py')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(47, 72, 88);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(330, 200, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-color: rgb(254, 124, 103);")
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(self.openPacman)
        self.playButton.clicked.connect(MainWindow.close)
        self.settingButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingButton.setGeometry(QtCore.QRect(330, 270, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.settingButton.setFont(font)
        self.settingButton.setStyleSheet(
            "background-color: rgb(254, 124, 103);")
        self.settingButton.setObjectName("settingButton")
        self.settingButton.clicked.connect(self.openSettings)
        self.settingButton.clicked.connect(MainWindow.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 621, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0)")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "PLAY"))
        self.settingButton.setText(_translate("MainWindow", "SETTING"))
        self.label.setText(_translate("MainWindow", "Author :"))
        self.label_2.setText(_translate("MainWindow", "GAME PACMAN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
