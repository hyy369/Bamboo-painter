import random
from Segment import Segment
from Vec2d import Vec2d
from Joint import Joint
from Branch import Branch

class Stalk:

    def __init__(self, root, length):
        self.root = Joint(root.x, root.y, self)
        # self.top = root
        self.top = Joint(root.x, root.y, self)
        self.segments = list()
        self.joints = list()
        self.branches = list()
        self.count = 0
        self.direction = Vec2d(0, 1)
        self.bend = random.choice([-1, 1])
        self.length = length

    def grow(self):
        # rand_length = random.randint(100, 300)
        rand_length = 200
        # rand_angle = random.randint(1, 10)
        rand_angle = 5
        # print("top", self.top.x, self.top.y)
        new_seg = Segment(self.top.position, self.direction.rotate(rand_angle * self.bend), rand_length)
        self.top = Joint(new_seg.get_end().x, new_seg.get_end().y, new_seg)
        if self.decide_grow_branch():
            new_branch = Branch(self.top, 1)
            for j in range(self.generate_segment_count()):
                new_branch.grow()
                self.top.l_branch = new_branch
            self.branches.append(new_branch)
        if self.decide_grow_branch():
            new_branch = Branch(self.top, -1)
            for j in range(self.generate_segment_count()):
                new_branch.grow()
                self.top.r_branch = new_branch
            self.branches.append(new_branch)
        self.joints.append(self.top)
        # print("new_top",self.top.x,self.top.y)
        self.segments.append(new_seg)
        self.count = len(self.segments)

    def decide_grow_branch(self):
        if len(self.segments) + 1 == self.length: return False
        i = random.randint(1,10)
        if i <= 4: return True
        else: return False


def generate_segment_count():
    return random.randint(1, 2)
