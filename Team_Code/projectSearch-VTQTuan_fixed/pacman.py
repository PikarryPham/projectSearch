class Pacman:
    """
    attribute:
        position: current position of pacman -> name of node (str)
        score: current score of pacman -> int
        state: true or false
    actions:
        left, right, up, down.
    """
    def __init__(self, pos_init, score=0, state=True):
        self.position = pos_init
        self.score = score
        self.state = state

    def move(self, pos):
        self.score -= 1
        self.position = pos

    def eat(self, pos):
        self.score += 20
        self.position = pos
        

