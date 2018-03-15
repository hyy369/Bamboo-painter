import random
import time
import imageio
# import numpy as np

from Painter import Painter
from Canvas import Canvas
from Vec2d import Vec2d
from Stalk import Stalk


def generate_bamboo_quantity():
    # return random.randint(2, 4)
    return 1


def generate_segment_count():
    # return random.randint(3, 5)
    return 3


def generate_root_position(width):
    # return Vec2d(random.randint(int(0.33 * width), int(0.5 * width)), 0)
    return Vec2d(256, 0)


def generate_new_root(root):
    return Vec2d(root + random.randint(30, 60), 0)


def main():
    timestamp = str(int(time.time()))
    filename1 = timestamp + "_sturcture.png"
    filename2 = timestamp + "_render.png"
    size = 512
    canvas_struct = Canvas(size, size)
    canvas_render = Canvas(size, size)
    png_painter = Painter()

    stalk_sprite = imageio.imread('./sprite/stalk-1.png')
    branch_sprite = imageio.imread('./sprite/branch-1.png')
    leaf_sprite = imageio.imread('./sprite/leaf-1.png')

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
            print(seg.origin.x, seg.origin.y)
            print(seg.direction.x, seg.direction.y)
            print(seg.get_end().x, seg.get_end().y)
            canvas_struct.paint_seg_black(seg)
            canvas_render.paint_seg_sprite(seg, stalk_sprite)
        for branch in stalk.branches:
            for seg in branch.segments:
                canvas_struct.paint_seg_blue(seg)
                # canvas_render.paint_seg_sprite(seg, branch_sprite)
            for joint in branch.joints:
                canvas_struct.paint_joint_blue(joint)
            for leaf in branch.leaves:
                canvas_struct.paint_seg_green(leaf)
                # canvas_render.paint_seg_sprite(leaf, leaf_sprite)
        for joint in stalk.joints:
            canvas_struct.paint_joint_red(joint)

    png_painter.paint_png(canvas_struct, filename1)
    png_painter.paint_png(canvas_render, filename2)


main()
