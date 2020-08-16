# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guipacman.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# tải thêm module PyQt5 này về nghen
map_lv01 = ['lv1_01.txt', 
            'lv1_02.txt', 
            'lv1_03.txt', 
            'lv1_04.txt',
            'lv1_05.txt',
            'lv1_06.txt']
map_lv02 = ['lv2_01.txt',
            'lv2_02.txt',
            'lv2_03.txt',
            'lv2_04.txt',
            'lv2_05.txt']
map_lv03 = []
map_lv04 = []

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtMultimedia import QSound, QMediaPlaylist, QMediaPlayer, QMediaContent
from guiSettings import *
from game import Game
from monsters import *
import pygame
from food import Food
from pacman import Pacman
import pygame
import random
pygame.init()

# author: Pham Ngoc Thuy Trang

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WIDTH = 30
HEIGHT = 30
MARGIN = 5

lst_color = [RED, BLUE, GREEN]
# ------KHOI TAO CAPTION VÀ CẤU HÌNH ẢNH------------------------------------------
#pygame.mixer.music.load('pacman_beginning.wav')
#pygame.mixer.music.play(-1)
pygame.display.set_caption("Pacman")
img_pacMax = pygame.image.load("pacman.png")
img_food = pygame.image.load("food.png")
img_pacMaxRed = pygame.image.load("red_1.png")
img_pacMaxBlue = pygame.image.load("blue.png")
img_pacMaxYellow = pygame.image.load("yellow.png")
img_pacMax = pygame.transform.scale(img_pacMax, (25, 25))
img_food = pygame.transform.scale(img_food, (25, 25))
img_pacMaxRed = pygame.transform.scale(img_pacMaxRed, (25, 25))
img_pacMaxBlue = pygame.transform.scale(img_pacMaxBlue, (25, 25))
img_pacMaxYellow = pygame.transform.scale(img_pacMaxYellow, (25, 25))
clock = pygame.time.Clock()
# -------------------------------------LV1-------------------------------------------


def RunLV1(lcol, lrow, row, col, start, Len, MapGame):
    WINDOW_SIZE = [800, 800]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    tempX, tempY = init(int(start[0]), int(start[1]))
    print(tempX)
    print(tempY)
    done = False
    flag = False
    score = 0
    index = 0
    path = 0
    FoodX = []
    FoodY = []
    check = [[0] * 1000] * 1000
    path = 0
    PointX = [0] * 2000
    PointY = [0] * 2000
    ind = 0
    while not done:

        for event in pygame.event.get():  #
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row2 = pos[1] // (HEIGHT + MARGIN)
                print(str(column) + " " + str(row2))

        if index <= len(lrow) - 1:
            tempX = lrow[index] * (WIDTH + MARGIN) + MARGIN
            tempY = lcol[index] * (WIDTH + MARGIN) + MARGIN
            score -= 1
            ShowScore(col * (WIDTH + MARGIN) + MARGIN, row *
                      (WIDTH + MARGIN) + MARGIN, score, screen, "PacMan")
            if len(PointX) > 0:
                for i in range(0, len(PointX), 1):
                    if tempX == PointX[i] and tempY == PointY[i] and check[FoodX[i]][FoodY[i]] == 0:
                        ind += 1
                        check[FoodX[i]][FoodY[i]] = int(1)
                        print("col= ", FoodX[i], " row= ", FoodY[i],
                              " = ", check[FoodX[i]][FoodY[i]])
                        score = score + 20
                        pygame.mixer.Sound("pacman_eatfruit.wav").play()
                        ShowScore(col * (WIDTH + MARGIN) + MARGIN, row * (WIDTH + MARGIN) + MARGIN, score, screen,
                                  "PacMan")

        screen.fill(BLACK)
        screen.blit(img_pacMax, (tempX, tempY))

        if index >= len(lrow):
            index += 1
            continue
        if path > Len:
            continue
        path += 1
        print(score)
        ShowScore(col*(WIDTH+MARGIN) + MARGIN, row *
                  (WIDTH+MARGIN) + MARGIN, score, screen, "PacMan")

        for i in range(0, len(FoodX), 1):
            if check[FoodX[i]][FoodY[i]] == 1:
                print("col= ", FoodX[i], " row= ", FoodY[i],
                      " = ", check[FoodX[i]][FoodY[i]])
            if check[FoodX[i]][FoodY[i]] == 0:
                PointX[i] = (FoodY[i] * (MARGIN + WIDTH) + MARGIN)
                PointY[i] = (FoodX[i] * (MARGIN + WIDTH) + MARGIN)
                screen.blit(
                    img_food, (FoodY[i] * (MARGIN + WIDTH) + 1, FoodX[i] * (MARGIN + WIDTH) + 1))
        for row1 in range(row):
            for column in range(col):
                if int(MapGame[row1][column]) == 1:
                    color = RED
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row1 + MARGIN,
                                      WIDTH,
                                      HEIGHT])
                if int(MapGame[row1][column]) == 2:
                    FoodX.append(row1)
                    FoodY.append(column)

        if index >= len(lrow):
            index += 1
            continue
        clock.tick(60)
        pygame.time.wait(500)
        index += 1
        pygame.display.update()
        pygame.display.flip()
        Pacman.score = score

    pygame.quit()

# --------------------------ĐIỂM--------------------------------------------------


font = pygame.font.Font('freesansbold.ttf', 25)


def ShowScore(x, y, score_value, screen, singal):
    score = font.render(singal+" :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
# ---------------------------------------------------------------------------------


def init(startX, startY):
    tempX = startX*(WIDTH+MARGIN) + MARGIN
    tempY = startY*(WIDTH+MARGIN) + MARGIN
    return tempX, tempY


index = 0


# ----------------------------LV2-------------------------------------------------------
def RunLV2(lcol, lrow, row, col, start, Len, MapGame):
    
    WINDOW_SIZE = [800, 800]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    tempX, tempY = init(int(start[0]), int(start[1]))

    done = False
    score_pacman = 0
    score_monters = 0
    index = 0
    flag = False
    FoodX = []
    FoodY = []
    check = [[0]*1000]*1000
    path = 0
    PointX = [0]*2000
    PointY = [0]*2000
    ind = 0
    while not done:

        for event in pygame.event.get():  #
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row2 = pos[1] // (HEIGHT + MARGIN)
                print(str(column) + " " + str(row2))

        ShowScore(col * (WIDTH + MARGIN) + MARGIN, row * (WIDTH +
                                                          MARGIN) + MARGIN + 20, score_monters, screen, "Monsters")
        if index <= len(lrow) - 1:
            tempX = lrow[index] * (WIDTH + MARGIN) + MARGIN
            tempY = lcol[index] * (WIDTH + MARGIN) + MARGIN
            score_pacman -= 1
            ShowScore(col * (WIDTH + MARGIN) + MARGIN, row *
                      (WIDTH + MARGIN) + MARGIN, score_pacman, screen, "PacMan")
            ShowScore(col * (WIDTH + MARGIN) + MARGIN, row * (WIDTH + MARGIN) + MARGIN + 20, score_monters, screen,
                      "Monsters")
            print("Score Pac ", score_pacman)
            if len(PointX) > 0:
                for i in range(0, len(PointX), 1):
                    if tempX == PointX[i] and tempY == PointY[i] and check[FoodX[i]][FoodY[i]] == 0:
                        ind += 1
                        check[FoodX[i]][FoodY[i]] = int(1)
                        print("col= ", FoodX[i], " row= ", FoodY[i],
                              " = ", check[FoodX[i]][FoodY[i]])
                        score_pacman = score_pacman + 20
                        print("Score: ", score_pacman, " ", score_monters)
                        pygame.mixer.Sound("pacman_eatfruit.wav").play()
                        ShowScore(col * (WIDTH + MARGIN) + MARGIN, row *
                                  (WIDTH + MARGIN) + MARGIN, score_pacman, screen, "PacMan")
                        ShowScore(col * (WIDTH + MARGIN) + MARGIN, row * (WIDTH + MARGIN) + MARGIN + 30, score_monters, screen,
                                  "Monsters")
        screen.fill(BLACK)
        screen.blit(img_pacMax, (tempX, tempY))

        ShowScore(col * (WIDTH + MARGIN) + MARGIN, row *
                  (WIDTH + MARGIN) + MARGIN, score_pacman, screen, "PacMan")
        ShowScore(col * (WIDTH + MARGIN) + MARGIN, row * (WIDTH + MARGIN) + MARGIN + 30, score_monters, screen,
                  "Monsters")
        # print(str(X) + " " + str(Y))
        if path > Len:
            continue
        path += 1

        L_COL = []
        L_ROW = []
        for i in range(0, len(FoodX), 1):
            if check[FoodX[i]][FoodY[i]] == 1:
                print("col= ", FoodX[i], " row= ", FoodY[i],
                      " = ", check[FoodX[i]][FoodY[i]])
            if check[FoodX[i]][FoodY[i]] == 0:
                PointX[i] = (FoodY[i] * (MARGIN + WIDTH) + MARGIN)
                PointY[i] = (FoodX[i] * (MARGIN + WIDTH) + MARGIN)
                screen.blit(
                    img_food, (FoodY[i] * (MARGIN + WIDTH) + 1, FoodX[i] * (MARGIN + WIDTH) + 1))
        for row1 in range(row):
            for column in range(col):
                if int(MapGame[row1][column]) == 1:
                    color = RED
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row1 + MARGIN,
                                      WIDTH,
                                      HEIGHT])
                if int(MapGame[row1][column]) == 2:
                    FoodX.append(row1)
                    FoodY.append(column)
                if int(MapGame[row1][column]) == 3:
                    L_COL.append(column)
                    L_ROW.append(row1)

        if len(L_COL) == 1:
            screen.blit(
                img_pacMaxRed, (L_COL[0] * (MARGIN + WIDTH) + 1, L_ROW[0] * (MARGIN + WIDTH) + 1))
        elif len(L_COL) == 2:
            screen.blit(
                img_pacMaxRed, (L_COL[0] * (MARGIN + WIDTH) + 1, L_ROW[0] * (MARGIN + WIDTH) + 1))
            screen.blit(
                img_pacMaxBlue, (L_COL[1] * (MARGIN + WIDTH) + 1, L_ROW[1] * (MARGIN + WIDTH) + 1))
        elif len(L_COL) >= 3:
            screen.blit(
                img_pacMaxRed, (L_COL[0] * (MARGIN + WIDTH) + 1, L_ROW[0] * (MARGIN + WIDTH) + 1))
            screen.blit(
                img_pacMaxBlue, (L_COL[1] * (MARGIN + WIDTH) + 1, L_ROW[1] * (MARGIN + WIDTH) + 1))
            screen.blit(
                img_pacMaxYellow, (L_COL[2] * (MARGIN + WIDTH) + 1, L_ROW[2] * (MARGIN + WIDTH) + 1))
        if len(L_COL) > 3:
            for i in range(3, len(L_COL), 1):
                screen.blit(
                    img_pacMaxRed, (L_COL[i] * (MARGIN + WIDTH) + 1, L_ROW[i] * (MARGIN + WIDTH) + 1))
                screen.blit(
                    img_pacMaxBlue, (L_COL[i] * (MARGIN + WIDTH) + 1, L_ROW[i] * (MARGIN + WIDTH) + 1))
                screen.blit(
                    img_pacMaxYellow, (L_COL[i] * (MARGIN + WIDTH) + 1, L_ROW[i] * (MARGIN + WIDTH) + 1))
        if index >= len(lrow):
            index += 1
            continue
        clock.tick(60)
        pygame.time.wait(500)
        index += 1
        pygame.display.update()
        pygame.display.flip()
        Monster.score = score_monters
        Pacman.score = score_pacman
    pygame.quit()

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
        if self.lv == "1":
            file_name = random.choice(map_lv01)
            self.game = Game(file_name)
            self.game.cheating_lv01_02(algorithms='A_star')
            MapGame = self.game.map_game.map_matrix
            Start = self.game.map_game.pos
            row = int(len(MapGame))
            col = int(len(MapGame[0]))
            # cheating level 1 and 2
            Food, path, explored, time_consuming = self.game.cheating_lv01_02(algorithms='A_star')
    
            lcol = []
            lrow = []
            for i in range(0, len(path), 1):
                Row = int(int(path[i])/col)
                lcol.append(Row)
                Col = int(path[i]) % col
                lrow.append(Col)
            print(lcol)
            print(lrow)
    
            RunLV1(lcol, lrow, row, col, Start, len(path), MapGame)
        elif self.lv == "2":
            file_name = random.choice(map_lv02)
            self.game = Game(file_name)
            self.game.cheating_lv01_02(algorithms='A_star')
            MapGame = self.game.map_game.map_matrix
            Start = self.game.map_game.pos
            row = int(len(MapGame))
            col = int(len(MapGame[0]))
            # cheating level 1 and 2
            Food, path, explored, time_consuming = self.game.cheating_lv01_02(algorithms='A_star')
    
            lcol = []
            lrow = []
            for i in range(0, len(path), 1):
                Row = int(int(path[i])/col)
                lcol.append(Row)
                Col = int(path[i]) % col
                lrow.append(Col)
            print(lcol)
            print(lrow)
    
            RunLV2(lcol, lrow, row, col, Start, len(path), MapGame)


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
    