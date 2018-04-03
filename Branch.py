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
        seg_length = random_seg_length()
        leaf_length = random_leaf_length()
        new_seg = Segment(self.top.position, self.direction, seg_length)
        self.top = Joint(new_seg.get_end().x, new_seg.get_end().y, new_seg)
        leaf_angle = random_leaf_angle()
        new_leaf = Segment(self.top.position, Vec2d(0, 1).rotate(leaf_angle), leaf_length)
        self.top.l_branch = new_leaf
        self.leaves.append(new_leaf)
        self.joints.append(self.top)
        self.segments.append(new_seg)
        self.count = len(self.segments)

    def grow_first_seg(self):
        seg_length = random_seg_length()
        leaf_length = random_leaf_length()
        seg_angle = random.randint(30, 90) * random.choice([-1, 1])
        new_seg = Segment(self.top.position, self.direction.rotate(seg_angle), seg_length)
        self.top = Joint(new_seg.get_end().x, new_seg.get_end().y, new_seg)
        leaf_angle = random_leaf_angle()
        new_leaf = Segment(self.top.position, Vec2d(0, 1).rotate(leaf_angle), leaf_length)
        self.top.l_branch = new_leaf
        self.leaves.append(new_leaf)
        self.joints.append(self.top)
        self.segments.append(new_seg)
        self.count = len(self.segments)

    def get_segment(self):
        length = (self.segments[len(self.segments)-1].get_end() - self.root.position).length()
        return Segment(self.root.position, self.direction, length)


def random_leaf_angle():
    return random.randint(135, 225)


def random_leaf_length():
    return random.randint(120, 170)


def random_seg_length():
    return random.randint(80, 120)

