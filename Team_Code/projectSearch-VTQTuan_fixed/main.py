from game import Game
from monsters import *
import pygame
from food import Food
from pacman import Pacman
pygame.init()

# author: Pham Ngoc Thuy Trang

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 30
HEIGHT = 30
MARGIN = 5
# ------KHOI TAO CAPTION VÀ CẤU HÌNH ẢNH------------------------------------------
pygame.mixer.music.load('pacman_beginning.wav')
pygame.mixer.music.play(-1)
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


def RunLV1(lcol, lrow, row, col, start, Len):
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
def RunLV2(lcol, lrow, row, col, start, Len):
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


if __name__ == "__main__":

    new_game = Game(r"17x9.txt")
    MapGame = new_game.map_game.map_matrix
    Start = new_game.map_game.pos
    row = int(len(MapGame))
    col = int(len(MapGame[0]))
    print(MapGame)
    # cheating level 1 and 2
    Food, path, explored, time_consuming = new_game.cheating_lv01_02(
        algorithms='GBFS')
    # print(explored)

    lcol = []
    lrow = []
    for i in range(0, len(path), 1):
        Row = int(int(path[i])/col)
        lcol.append(Row)
        Col = int(path[i]) % col
        lrow.append(Col)
    print(lcol)
    print(lrow)

    RunLV2(lcol, lrow, row, col, Start, len(path))
    #RunLV1(lcol, lrow, row, col, Start, len(path))
    # cheating level 3
    # cheating level 4
