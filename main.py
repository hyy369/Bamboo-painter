import random
import time
import imageio
import numpy as np

from Painter import Painter
from Canvas import Canvas
from Vec2d import Vec2d
from Stalk import Stalk


def generate_bamboo_quantity():
    return random.randint(2, 4)


def generate_segment_count():
    return random.randint(3, 5)


def generate_root_position(width):
    return Vec2d(random.randint(int(0.33 * width), int(0.5 * width)), 0)


def generate_new_root(root):
    return Vec2d(root + random.randint(30,60), 0)


def main():
    filename = str(int(time.time())) + ".png"
    size = 512
    canvas = Canvas(size, size)
    ppm_painter = Painter()

    stalk_sprite = imageio.imread('./sprite/stalk-1.png')
    branch_sprite = imageio.imread('./sprite/branch-1.png')
    leaf_sprite = imageio.imread('./sprite/leaf-1.png')
    print(stalk_sprite[0][0])

    quantity = generate_bamboo_quantity()
    newest_root = generate_root_position(size)
    roots = list()
    roots.append(newest_root)
    for i in range(quantity - 1):
        newest_root = generate_new_root(newest_root.x)
        roots.append(newest_root)

    stalks = list()
    for root in roots:
        length = generate_segment_count()
        new_stalk = Stalk(root, length)
        for j in range(length):
            new_stalk.grow()
        stalks.append(new_stalk)

    for stalk in stalks:
        for seg in stalk.segments:
            canvas.paint_seg_black(seg)
            canvas.paint_seg_sprite(seg, stalk_sprite)
        for branch in stalk.branches:
            for seg in branch.segments:
                canvas.paint_seg_blue(seg)
                canvas.paint_seg_sprite(seg, branch_sprite)
            for joint in branch.joints:
                canvas.paint_joint_blue(joint)
            for leaf in branch.leaves:
                canvas.paint_seg_green(leaf)
                canvas.paint_seg_sprite(seg, leaf_sprite)
        for joint in stalk.joints:
            canvas.paint_joint_red(joint)

    ppm_painter.paint_png(canvas, filename)
    # ppm_painter.paint_p6(canvas, filename)


main()
