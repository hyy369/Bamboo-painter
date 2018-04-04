import math

class Vec2d:
    """2D Vector/Point class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalize(self):
        self.x = self.x / self.length()
        self.y = self.y / self.length()
        return self

    def rotate(self, angle):
        rad = angle * math.pi / 180
        x = self.x * math.cos(rad) - self.y * math.sin(rad)
        y = self.x * math.sin(rad) + self.y * math.cos(rad)
        self.x = x
        self.y = y
        return self

    def static_rotate(self, angle):
        rad = angle * math.pi / 180
        x = self.x * math.cos(rad) - self.y * math.sin(rad)
        y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vec2d(x, y)

    def sqaured_length(self):
        return self.x * self.x + self.y * self.y

    def length(self):
        return math.sqrt(self.sqaured_length())

    def dot(self, v2):
        return self.x * v2.x + self.y * v2.y

    def cosine_angle(self, v2):
        return self.dot(v2) / (self.length() * v2.length())

    def sine_angle(self, v2):
        return self.x * v2.y - v2.x * self.y

    # override methods
    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)



