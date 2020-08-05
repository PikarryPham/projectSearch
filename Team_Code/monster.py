# pylint: disable=unused-wildcard-import, method-hidden
# pylint: enable=too-many-lines
class Monster:
    def __init__(self, pos_init, score=0):
        self.score = score
        self.position = pos_init
    def move(self, pos):
        self.position = pos
    def meet_pacman(self, pacman):
        raise NotImplementedError

