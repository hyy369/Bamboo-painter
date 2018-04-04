import random
from Segment import Segment
from Vec2d import Vec2d
from Joint import Joint
from Branch import Branch

class Stalk:

    def __init__(self, root, length):
        self.root = Joint(root.x, root.y, self)
        self.top = Joint(root.x, root.y, self)
        self.segments = list()
        self.joints = list()
        self.branches = list()
        self.count = 0
        self.bend_side = random.choice([-1, 1])
        self.direction = Vec2d(0, 1).rotate(get_initial_angle() * self.bend_side)
        self.length = length
        self.branch_side = random.choice([-1, 1])

    def grow(self):
        rand_length = get_segment_length()
        rand_angle = get_random_angle()
        new_seg = Segment(self.top.position, self.direction.rotate(rand_angle * self.bend_side), rand_length)
        self.top = Joint(new_seg.get_end().x, new_seg.get_end().y, new_seg)
        if self.decide_grow_branch():
            new_branch = Branch(self.top, self.branch_side)
            self.branch_side *= -1
            for j in range(get_segment_count()):
                new_branch.grow()
            new_branch.grow_tip_leaf()
            self.top.l_branch = new_branch
            self.branches.append(new_branch)
        # if self.decide_grow_branch():
        #     new_branch = Branch(self.top)
        #     for j in range(generate_segment_count()):
        #         new_branch.grow()
        #         self.top.r_branch = new_branch
        #     self.branches.append(new_branch)
        self.joints.append(self.top)
        self.segments.append(new_seg)
        self.count = len(self.segments)

    def decide_grow_branch(self):
        if len(self.segments) + 1 == self.length:
            return False
        i = random.randint(1, 100)
        if i <= 35:
            return True
        else:
            return False


def get_segment_count():
    return random.randint(6, 10)


def get_segment_length():
    return random.randint(242, 335)


def get_random_angle():
    return random.randint(0, 5)


def get_initial_angle():
    return random.randint(0, 10)
