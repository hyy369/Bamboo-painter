import random
import time
import imageio
# import numpy as np

from Painter import Painter
from Canvas import Canvas
from Vec2d import Vec2d
from Stalk import Stalk


def main():
    # Initializations
    timestamp = str(int(time.time()))
    filename1 = "./sample_output/" + timestamp + "_sturcture.png"
    filename2 = "./sample_output/" + timestamp + "_render.png"
    width = 480
    height = 720
    canvas_struct = Canvas(width, height)
    canvas_render = Canvas(width, height)
    png_painter = Painter()

    # Read sprites
    stalk_sprite = [imageio.imread('./sprite/stalk-1.png'), imageio.imread('./sprite/stalk-2.png'), imageio.imread('./sprite/stalk-3.png')]
    branch_sprite = [imageio.imread('./sprite/branch-1.png'), imageio.imread('./sprite/branch-2.png')]
    leaf_sprite = [imageio.imread('./sprite/leaf-1.png'), imageio.imread('./sprite/leaf-2.png'), imageio.imread('./sprite/leaf-3.png'), imageio.imread('./sprite/leaf-4.png'), imageio.imread('./sprite/leaf-5.png')]
    seal_sprite = imageio.imread('./sprite/seal-90.png')

    print("Constructing...")

    quantity = generate_bamboo_quantity()
    newest_root = generate_root_position(width)
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

    stalk_count = 1
    stalk_total = len(stalks)
    for stalk in stalks:
        print("Rendering stalk", stalk_count, "/", stalk_total)
        shade = get_shade_degree()
        for seg in stalk.segments:
            # print(seg.origin.x, seg.origin.y)
            # print(seg.direction.x, seg.direction.y)
            # print(seg.get_end().x, seg.get_end().y)
            canvas_struct.paint_seg_black(seg)
            canvas_render.paint_seg_sprite(seg, stalk_sprite[get_stalk_sprite_index()], shade)

        for branch in stalk.branches:
            seg = branch.get_segment()
            canvas_struct.paint_seg_blue(seg)
            canvas_render.paint_seg_sprite(seg, branch_sprite[get_branch_sprite_index()], shade)
            for joint in branch.joints:
                canvas_struct.paint_joint_blue(joint)
            for leaf in branch.leaves:
                canvas_struct.paint_seg_green(leaf)
                canvas_render.paint_seg_sprite(leaf, leaf_sprite[get_leaf_sprite_index()], shade)
        for joint in stalk.joints:
            canvas_struct.paint_joint_red(joint)
        stalk_count += 1

    canvas_render.paint_seal(seal_sprite)

    print("Saving images...")
    png_painter.paint_png(canvas_struct, filename1)
    png_painter.paint_png(canvas_render, filename2)


def generate_bamboo_quantity():
    # return random.randint(2, 4)
    return 3


def generate_segment_count():
    return random.randint(3, 4)
    # return 3


def generate_root_position(width):
    return Vec2d(random.randint(int(0.33 * width), int(0.5 * width)), -10)
    # return Vec2d(256, 0)


def generate_new_root(root):
    return Vec2d(root + random.randint(30, 60), -10)


def get_stalk_sprite_index():
    return random.randint(0, 2)


def get_branch_sprite_index():
    return random.randint(0, 1)


def get_leaf_sprite_index():
    return random.randint(0, 4)


def get_shade_degree():
    return random.randint(7, 10) / 10


main()
