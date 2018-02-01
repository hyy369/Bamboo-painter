from Vec2d import Vec2d


class Segment:
    """Line segment class"""

    def __init__ (self, origin, direction, length):
        self.origin = Vec2d(origin.x, origin.y)
        self.direction = Vec2d(direction.x, direction.y)
        self.length = length

    def get_end(self):
        return Vec2d(int(self.origin.x + self.direction.x * self.length), int(self.origin.y + self.direction.y * self.length))


