# pylint: disable=unused-wildcard-import, method-hidden
# pylint: enable=too-many-lines
class Pacman:
    def __init__(self, pos_init, score=0):
        self.score = score
        self.position = pos_init
    def move(self, position):
        self.score -= 1
        self.position = position
    def eat_lv_01_02(self, food):
        raise NotImplementedError
    def eat_lv_03_04(self):
        raise NotImplementedError