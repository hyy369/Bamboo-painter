import random
from Segment import Segment
from Vec2d import Vec2d
from Joint import Joint


class Branch:

    def __init__(self, root):
        self.root = root
        self.top = Joint(root.position.x, root.position.y, self)
        self.segments = list()
        self.joints = list()
        self.leaves = list()
        self.count = 0
        self.direction = Vec2d(0, 1)
        self.grow_first_seg()

    def grow(self):
        rand_length = random.randint(50, 100)
        rand_leaf_length = random.randint(30, 50)
        new_seg = Segment(self.top.position, self.direction, rand_length)
        self.top = Joint(new_seg.get_end().x, new_seg.get_end().y, new_seg)
        leaf_angle = random_leaf_angle()
        new_leaf = Segment(self.top.position, Vec2d(0, 1).rotate(leaf_angle), rand_leaf_length)
        self.top.l_branch = new_leaf
        self.leaves.append(new_leaf)
        self.joints.append(self.top)
        self.segments.append(new_seg)
        self.count = len(self.segments)

    def grow_first_seg(self):
        rand_length = random.randint(50, 100)
        rand_leaf_length = random.randint(30, 50)
        rand_angle = random.randint(30, 90) * random.choice([-1, 1])
        new_seg = Segment(self.top.position, self.direction.rotate(rand_angle), rand_length)
        self.top = Joint(new_seg.get_end().x, new_seg.get_end().y, new_seg)
        leaf_angle = random_leaf_angle()
        new_leaf = Segment(self.top.position, Vec2d(0, 1).rotate(leaf_angle), rand_leaf_length)
        self.top.l_branch = new_leaf
        self.leaves.append(new_leaf)
        self.joints.append(self.top)
        self.segments.append(new_seg)
        self.count = len(self.segments)


def random_leaf_angle():
    return random.randint(135, 225)

