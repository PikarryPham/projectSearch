# pylint: disable=unused-wildcard-import, method-hidden
# pylint: enable=too-many-lines
from monster import * 
from pacman import * 
from food import * 
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


    
