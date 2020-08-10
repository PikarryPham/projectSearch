# pylint: disable=unused-wildcard-import, method-hidden
# pylint: enable=too-many-lines
from queue import PriorityQueue
import datetime
import timeit
import time
from monster import *
from pacman import *
from food import *

edges = []
exit_node = 0
n = 0
ok = []
trace = []
queue = []
times = 0
is_found = 0
# f = open("../input/input2.txt", "r")


class Game:
    def __init__(self):
        """
        constructor of class game
         maze: a dict save all position of the game's map
         pacman: initializing pacman
         monter: list of monters in game
         food: list of foods in game
        -> Not return
        """
        self.maze = {}
        self.pacman = Pacman(pos_init=(0, 0))
        self.foods = []
        self.monsters = []

    def get_input_file(self, file_name):
        """
        Read the input file of the game.
        -> Not return
        """
        raise NotImplementedError

    def control_pacman(self):
        raise NotImplementedError

    def control_monster(self):
        raise NotImplementedError

    def execute_lv01(self):
        raise NotImplementedError

    def execute_lv02(self):
        raise NotImplementedError

    def execute_lv03(self):
        raise NotImplementedError

    def execute_lv04(self):
        raise NotImplementedError

    def initial():
        global ok, trace
        ok = []
        trace = []

        for i in range(0, n*n+1):
            ok.append(1)
        for i in range(0, n*n+1):
            ok.append(-1)

    def visit(u):
        global trace, ok, exit_node, is_found

        if (is_found == 1):
            return

        ok[u] = 0

        if (u == exit_node):
            is_found = 1
            return

        for index in range(0, len(edges[u])):
            v = edges[u][index]
            if (ok[v] == 1):
                trace[v] = u
                visit(v)

    def BFS_alg():
        initial()
        global trace, times, ok, is_found
        is_found = 0
        queue.append(0)
        trace[0] = 0

        while(len(queue) > 0):
            u = queue.pop(0)

            for index in range(0, len(edges[u])):
                if(is_found == 1):
                    break

                v = edges[u][index]
                if(ok[v] == 1):
                    queue.append(v)
                    ok[v] = 0
                    trace[v] = u
                    if (v == exit_node):
                        is_found = 1
                        break
        print("BFS")
        times = 0
        print_result(exit_node)
        print()

    def print_result(u):
        global times, n, ok

        if(u == -1):
            return

        if (u == 0):
            print("times : ", times)
            #g.write("times : " + str(times) + "\n")

            print('explored node: ')
            for index in range(0, n*n):
                if (ok[index] == 0):
                    print(index, end=' ')
                    #g.write(str(index) + " ")

            print()
            # g.writelines("\n")

            print(0, end='')
            # g.write(str(0))
            return

        times = times + 1
        print_result(trace[u])
        print("-->", u, end='')
        # g.write("->" + str(u))

    def UCS_alg():
        initial()
        global exit_node, ok, edges, times

        print("UCS")
        d = []
        for i in range(0, n*n+1):
            d.append(1000000000)
        d[0] = 0

        queue = PriorityQueue()
        queue.put((d[0], 0))
        while queue.qsize():
            u = queue.get()
            u = u[1]
            if (u == exit_node):
                break

            if (ok[u] == 0):
                continue
            ok[u] = 0

            for index in range(0, len(edges[u])):
                v = edges[u][index]
                if (d[v] > d[u] + 1):
                    d[v] = d[u] + 1
                    queue.put((d[v], v))
                    trace[v] = u
        times = 0
        print_result(exit_node)
        print()

    def DFS_alg_01():
        initial()
        global is_found
        is_found = 0
        visit(0)

        global times
        print("DFS")
        g.write("DFS\n")
        times = 0
        print_result(exit_node)
        print()
