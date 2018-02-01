class Pixel:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def set_black(self):
        self.set_color(0, 0, 0)

    def sef_red(self):
        self.set_color(1, 0, 0)

    def sef_green(self):
        self.set_color(0, 1, 0)

    def sef_blue(self):
        self.set_color(0, 0, 1)
