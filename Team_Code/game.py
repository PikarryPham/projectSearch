from food import Food
from pacman import Pacman
from mapGame import *
from algorithms import *
from monsters import Monster

class Game:
    """
    attribute:
        map_game:
            N: number of rows
            M: number of cols
            list_of_nodes: list of node in graph.
                node:  
                    position
                    content
                    num_order
            list_of_monsters: list of node in graph where monsters stand.
            list_of_foods: list of node in graph where foods stand.
            start: start node, where pacman stands.
        foods: list of food objects in game.
        monsters: list of monsters objects in game.
        pacman: pacman object in game
    """
    def __init__(self, file_name):
        self.map_game = Map(file_name)
        self.pacman = Pacman(self.map_game.start.num_order)
        self.foods = []
        for fd in self.map_game.list_foods:
            f = Food(fd.num_order)
            self.foods.append(f)

        self.monsters = []
        for monster in self.map_game.list_monsters:
            m = Monster(monster.num_order)
            self.monsters.append(m)

    def cheating_lv01(self, algorithms='A_star'):
        food = self.foods[0]
        path, explored, time_consuming = a_star_graph_search(self.pacman.position,
                                                            food.position, 
                                                            self.map_game.map_graph, 
                                                            self.map_game.N,
                                                            self.map_game.M)

        return path, explored, time_consuming
    def cheating_lv02(self, algorithms='A_star'):
        pass


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
    
    
    def AStar(maze, start, goal):
        frontier = []
        explored = []
        h = []
        cost = 1
        for maze_i in maze:  # Manhattan distance
            h_i = []
            for i in maze_i:
                dist_x = abs(i % problem[2] - goal % problem[2])
                dist_y = abs(i // problem[2] - goal // problem[2])
                h_i.append(dist_x + dist_y)
            h.append(h_i)
        maze = [[(0, m_i) for m_i in maze_i] for maze_i in maze]
        trace = [-1] * len(maze)
        trace[0] = 0
        #
        if goal != 0:  # The goal is not at the start
            frontier.append((0, 0))
            last_h = [0] * len(maze[0])
            while frontier:
                node = frontier.pop(0)
                explored.append(node[1])
                # Sort the list -> Pop smallest cost first, then smallest val
                adjqueue = maze[node[1]]
                adjqueue.sort(key=operator.itemgetter(0, 1))
                for adj in adjqueue:
                    if (adj[1] not in explored) and (adj not in frontier):
                        # f = f(node) - h(node) + cost + h(adj)
                        adj_i = adjqueue.index(adj)
                        adj_h = h[node[1]][adj_i]
                        node_h = last_h.pop(0)
                        adj = (node[0] - node_h + cost + adj_h, adj[1])
                        trace[adj[1]] = node[1]
                        if goal == adj[1]:
                            trace[goal] = node[1]
                            break
                        # Update cost
                        updated = False
                        for f_i in frontier:
                            if f_i[1] == adj[1]:
                                if f_i[0] > adj[0]:
                                    frontier[frontier.index(f_i)] = adj
                                    updated = True
                        if not updated:
                            frontier.append(adj)
                        last_h.append(adj_h if not updated else node_h)
                else:
                    continue
                break
        #
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
        #
        print_result(path, explored, frontier, 'A* Search')
        return (path, explored, frontier)
