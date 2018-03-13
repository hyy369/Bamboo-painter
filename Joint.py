from Vec2d import Vec2d


class Joint:

    def __init__(self, x, y, parent):
        self.position = Vec2d(x, y)
        self.parent = parent
        self.stalk = None
        self.l_branch = None
        self.r_branch = None
