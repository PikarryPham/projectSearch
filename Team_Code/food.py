# pylint: disable=unused-wildcard-import, method-hidden
# pylint: enable=too-many-lines
class Food:
    def __init__(self, pos_init):
        self.position = pos_init
    def is_exist(self):
        raise NotImplementedError  