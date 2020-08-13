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



