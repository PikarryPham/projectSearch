# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guisettings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def openMain(self):
        from guipacman import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(800, 600)
        SettingsWindow.setStyleSheet("background-color: rgb(47, 72, 88);")
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 204, 50);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 204, 50);")
        self.label_2.setObjectName("label_2")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(120, 150, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                     "color: rgb(255, 255, 127);")
        self.oneButton.setObjectName("oneButton")
        self.twoButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton_2.setGeometry(QtCore.QRect(540, 150, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.twoButton_2.setFont(font)
        self.twoButton_2.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                       "color: rgb(255, 255, 127);")
        self.twoButton_2.setObjectName("twoButton_2")
        self.threeButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton_3.setGeometry(QtCore.QRect(120, 237, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.threeButton_3.setFont(font)
        self.threeButton_3.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                         "color: rgb(255, 255, 127);")
        self.threeButton_3.setObjectName("threeButton_3")
        self.fourButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton_4.setGeometry(QtCore.QRect(540, 237, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fourButton_4.setFont(font)
        self.fourButton_4.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                        "color: rgb(255, 255, 127);")
        self.fourButton_4.setObjectName("fourButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 204, 50);")
        self.label_3.setObjectName("label_3")
        self.onButton = QtWidgets.QPushButton(self.centralwidget)
        self.onButton.setGeometry(QtCore.QRect(110, 390, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.onButton.setFont(font)
        self.onButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                    "color: rgb(255, 255, 255);")
        self.onButton.setObjectName("onButton")
        self.offButton = QtWidgets.QPushButton(self.centralwidget)
        self.offButton.setGeometry(QtCore.QRect(540, 390, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.offButton.setFont(font)
        self.offButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                     "color: rgb(255, 255, 255);")
        self.offButton.setObjectName("offButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(110, 490, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.saveButton.setObjectName("saveButton")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(540, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.returnButton.setFont(font)
        self.returnButton.setStyleSheet(
            "background-color: rgb(170, 255, 255);")
        self.returnButton.setObjectName("returnButton")
        self.returnButton.clicked.connect(self.openMain)
        self.returnButton.clicked.connect(SettingsWindow.close)
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(
            _translate("SettingsWindow", "SettingWindow"))
        self.label.setText(_translate("SettingsWindow", "SETTINGS"))
        self.label_2.setText(_translate(
            "SettingsWindow", "Choose your difficulty"))
        self.oneButton.setText(_translate("SettingsWindow", "1"))
        self.twoButton_2.setText(_translate("SettingsWindow", "2"))
        self.threeButton_3.setText(_translate("SettingsWindow", "3"))
        self.fourButton_4.setText(_translate("SettingsWindow", "4"))
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
