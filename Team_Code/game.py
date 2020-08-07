# pylint: disable=unused-wildcard-import, method-hidden
# pylint: enable=too-many-lines
from ./monster import *
from ./pacman import *
from ./food import *
from math import sqrt
from operator import itemgetter


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

    def DFS(maze, start, goal, is_ids=False, d=0):
        """
        Depth First Search:
            maze: the full maze or a restricted view of the maze,
            start: position of the object using this function (pacman/monster),
            goal: result of a search func for food or pacman,
            is_ids: if this function is called from IDS,
            d: IDS current depth, a.k.a maximum depth allowed in DFS
        """
        frontier = []
        explored = []
        trace = [-1] * len(maze)  # Traceback to find path
        trace[0] = start  # Starting pos of object
        if goal != start:
            # node = (depth, position)
            frontier.append((0, start))
            while frontier:
                node = frontier.pop()
                explored.append(node[1])
                for adj in list(reversed(maze[node[1]])):
                    if (adj not in explored):
                        if ((node[0] + 1, adj) not in frontier):
                            trace[adj] = node[1]
                            break
                        # Increase depth of next node if this is IDS
                        if is_ids:
                            frontier.append((node[0] + 1, adj))
                else:
                    # Remove deeper nodes from frontier if this is IDS
                    if is_ids:
                        frontier = [f for f in frontier if f[0] <= d]
                    continue
                break
        path = []
        trace_i = goal
        while True:
            path.append(trace_i)
            if trace_i == start:
                break  # Finished trace back path
            elif trace_i == -1:
                path = [-1]  # Couldn't find path
                break
            trace_i = trace[trace_i]
        path = list(reversed(path))
        return (path, explored, frontier)

    def IDS(maze, start, goal):
        """
        Iterative Depth Search:
            maze: the full maze or a restricted view of the maze,
            start: position of the object using this function (pacman/monster),
            goal: result of a search func for food or pacman,
        """
        frontier = []
        ex_set = []
        path = []
        d = 0
        while True:
            dfs = DFS(maze, obj, is_ids=True, d=d)
            if len(ex_set) > 0 and ex_set[-1] == dfs[1]:  # Reached last level
                break
            ex_set.append(dfs[1])
            if dfs[0] != [-1]:
                path, frontier = dfs[0], dfs[2]
                break
            d += 1
        if path == []:
            path = [-1]
        return (path, ex_set, frontier)

    def GBFS(maze, start, goal):
        """
        Greedy-Best First Search:
            maze: the full maze or a restricted view of the maze,
            start: position of the object using this function (pacman/monster),
            goal: result of a search func for food or pacman,
        """
        frontier = []
        explored = []
        cost = []
        maze_size = sqrt(len(maze))  # Get value of N in NxN (the size of maze)
        for maze_i in maze:  # Init cost
            cost_i = []
            for i in maze_i:
                dist_x = abs(i % maze_size - goal % maze_size)
                dist_y = abs(i // maze_size - goal // maze_size)
                cost_i.append(dist_x + dist_y)
            cost.append(cost_i)
        # node = (heuristic cost, position)
        maze = [[(c_i, m_i) for (c_i, m_i) in zip(cost_i, maze_i)]
                for (cost_i, maze_i) in zip(cost, maze)]
        trace = [-1] * len(maze)
        trace[0] = start
        if goal != start:
            frontier.append((0, start))
            while frontier:
                node = frontier.pop(0)
                explored.append(node[1])
                # Create an adjacent node queue sorted by cost and position
                adjqueue = maze[node[1]]
                adjqueue.sort(key=itemgetter(0, 1))
                for adj in adjqueue:
                    if (adj[1] not in explored) and (adj not in frontier):
                        trace[adj[1]] = node[1]
                        if goal == adj[1]:
                            trace[goal] = node[1]
                            break
                        frontier.append(adj)
                else:
                    continue
                break
        path = []
        trace_i = goal
        while True:
            path.append(trace_i)
            if trace_i == 0:
                break
            elif trace_i == -1:
                path = [-1]
                break
            trace_i = trace[trace_i]
        path = list(reversed(path))
        return (path, explored, frontier)
