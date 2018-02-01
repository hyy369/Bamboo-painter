import random
from Segment import Segment
from Vec2d import Vec2d

class Stalk:

    def __init__(self, root):
        self.root = root
        self.top = root
        self.segments = list()
        self.joints = list()
        self.count = 0
        self.direction = Vec2d(0, 1)
        self.bend = random.choice([-1, 1])


    def grow(self):
        rand_length = random.randint(100, 300)
        rand_angle = random.randint(1, 10)
        # print("top", self.top.x, self.top.y)
        new_seg = Segment(self.top, self.direction.rotate(rand_angle * self.bend), rand_length)
        self.top = new_seg.get_end()
        self.joints.append(self.top)
        # print("new_top",self.top.x,self.top.y)
        self.segments.append(new_seg)
        self.count = len(self.segments)

