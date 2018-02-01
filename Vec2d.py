import math

class Vec2d:
    """2D Vector class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalize(self):
        pass

    def rotate(self, angle):
        rad = angle * math.pi / 180
        self.x = self.x * math.cos(rad) - self.y * math.sin(rad)
        self.y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return self

