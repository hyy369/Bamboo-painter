import random
from Segment import Segment
from Vec2d import Vec2d
from Joint import Joint

class Branch:

    def __init__(self, root, dir):
        self.root = root
        self.top = Joint(root.position.x, root.position.y, self)
        self.segments = list()
        self.joints = list()
        self.leaves = list()
        self.count = 0
        self.direction = Vec2d(0, 1)
        self.bend = dir
        self.grow_first_seg()

    def grow(self):
        rand_length = random.randint(50, 100)
        rand_leaf_length = random.randint(20, 50)
        new_seg = Segment(self.top.position, self.direction, rand_length)
        self.top = Joint(new_seg.get_end().x, new_seg.get_end().y, new_seg)
        new_leaf = Segment(self.top.position, self.random_leaf_angle(), rand_leaf_length)
        self.top.l_branch = new_leaf
        self.leaves.append(new_leaf)
        self.joints.append(self.top)
        self.segments.append(new_seg)
        self.count = len(self.segments)

    def grow_first_seg(self):
        rand_length = random.randint(50, 100)
        rand_angle = random.randint(30, 90)
        new_seg = Segment(self.top.position, self.direction.rotate(rand_angle * self.bend), rand_length)
        self.top = Joint(new_seg.get_end().x, new_seg.get_end().y, new_seg)
        self.joints.append(self.top)
        self.segments.append(new_seg)
        self.count = len(self.segments)

    @staticmethod
    def random_leaf_angle():
        return Vec2d(0.0, random.random() - 0.5)

