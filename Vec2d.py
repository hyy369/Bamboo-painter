import math

class Vec2d:
    """2D Vector/Point class"""

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

    def sqaured_length(self):
        return self.x * self.x + self.y * self.y

    def length(self):
        return math.sqrt(self.sqaured_length())

    def dot(self, v2):
        return self.x * v2.x + self.y * v2.y

    def cosine_angle(self, v2):
        return self.dot(v2) / (self.length() * v2.length())

    def sine_angle(self, v2):
        return math.sqrt(1 - self.cosine_angle(v2))

    def angle_btw(self, v2):
        return 180 * math.acos(self.cosine_angle(v2)) / math.pi



