# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guipacman.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# tải thêm module PyQt5 này về nghen
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtMultimedia import QSound, QMediaPlaylist, QMediaPlayer, QMediaContent
from guiSettings import *


class Ui_MainWindow(object):
    def __init__(self):
        # Get settings, set default when file not found
        self.lv = "1"
        self.mu = "on"
        try:
            l = open(".set_level", "r")
            self.lv = l.read()
            l.close()
        except FileNotFoundError:
            l = open(".set_level", "w")
            l.write(self.lv)
            l.close()
        try:
            m = open(".set_music", "r")
            self.mu = m.read()
            m.close()
        except FileNotFoundError:
            m = open(".set_music", "w")
            m.write(self.mu)
            m.close()
        # Music and sfx
        musicUrl = QtCore.QUrl.fromLocalFile(QtCore.QDir.current().absoluteFilePath("pacman.mp3"))
        print(musicUrl)
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(musicUrl))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.mainMusic = QMediaPlayer()
        self.mainMusic.setPlaylist(self.playlist)
        self.buttClicked = QSound("buttClicked.wav")


    def openSettings(self):
        from guiSettings import Ui_SettingsWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def openPacman(self):
        from game import Game
        if self.lv == "1":
            Game.cheating_lv01()
        elif self.lv == "2":
            Game.cheating_lv02()
        # elif self.lv == "3":
        #     Game.cheating_lv03()
        # elif self.lv == "4":
        #     Game.cheating_lv04()


    def buttAction(self, butt):
        if butt == "play":
            self.openPacman()
        elif butt == "settings":
            self.openSettings()
            self.mainMusic.stop()
        if self.mu == "on":
            self.buttClicked.play()

    def setupUi(self, MainWindow):
        # Color variables
        WINDOW_BG_COLOR = "#303030"
        LABEL_FG_COLOR = "#875faf"
        BUTTON_OP_BG_COLOR = "#875faf"
        TEXT_FG_COLOR = "#dfdfdf"
        
        # Main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QtGui.QIcon("pac.png"))
        MainWindow.setStyleSheet("background-color: %s;"%WINDOW_BG_COLOR)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Button PLAY
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(330, 200, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-color: %s;"%BUTTON_OP_BG_COLOR)
        self.playButton.setObjectName("playButton")
        # Button SETTINGS
        self.settingButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingButton.setGeometry(QtCore.QRect(330, 270, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.settingButton.setFont(font)
        self.settingButton.setStyleSheet("background-color: %s;"%BUTTON_OP_BG_COLOR)
        self.settingButton.setObjectName("settingButton")
        # MEMBERS label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 340, 500, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: %s"%LABEL_FG_COLOR)
        self.label.setObjectName("label")
        # Pacman image
        self.label11 = QtWidgets.QLabel(self.centralwidget)
        self.label11.setPixmap(QtGui.QPixmap("pac.png"))
        self.label11.move(50, 70)
        # self.movie = QMovie("gifPacman.gif", QByteArray(), self)
        # self.movie.setCacheMode(QMovie.CacheAll)
        # self.movie.setSpeed(100)
        # self.movie_screen.setMovie(self.movie)
        # self.label11.resize(self.label11.setPixmap(QtGui.QPixmap("pacAva.png")).width(
        # ), self.label11.setPixmap(QtGui.QPixmap("pacAva.png")).height())
        # Trang Name
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 400, 500, 30))
        fontName = QtGui.QFont()
        fontName.setPointSize(13)
        self.label_3.setFont(fontName)
        self.label_3.setStyleSheet("color: %s"%TEXT_FG_COLOR)
        self.label_3.setObjectName("label_3")
        # Tuan Name
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 460, 500, 30))
        self.label_4.setFont(fontName)
        self.label_4.setStyleSheet("color: %s"%TEXT_FG_COLOR)
        self.label_4.setObjectName("label_4")
        # Hung Name
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 520, 500, 30))
        self.label_5.setFont(fontName)
        self.label_5.setStyleSheet("color: %s"%TEXT_FG_COLOR)
        self.label_5.setObjectName("label_5")
        # PACMAN title
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 621, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(60)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:  %s"%LABEL_FG_COLOR)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        # Menubar and statusbar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Call buttAction
        self.playButton.clicked.connect(lambda: self.buttAction("play"))
        self.playButton.clicked.connect(MainWindow.close)
        self.settingButton.clicked.connect(lambda: self.buttAction("settings"))
        self.settingButton.clicked.connect(MainWindow.close)

        # Retranslate UI and play the music
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if self.mu == "on":
            self.mainMusic.play()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Game Pacman"))
        self.playButton.setText(_translate("MainWindow", "PLAY"))
        self.settingButton.setText(_translate("MainWindow", "SETTING"))
        self.label.setText(_translate("MainWindow", "MEMBERS :"))
        self.label_2.setText(_translate("MainWindow", "GAME PACMAN"))
        self.label_3.setText(_translate(
            "MainWindow", "Pham Ngoc Thuy Trang - 18127022"))
        self.label_4.setText(_translate(
            "MainWindow", "Vo Tran Quang Tuan - 18127248"))
        self.label_5.setText(_translate(
            "MainWindow", "Nguyen Gia Hung - 18127044"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())