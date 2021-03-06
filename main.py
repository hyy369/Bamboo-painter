import random
import time
import imageio
# import numpy as np

from Painter import Painter
from Canvas import Canvas
from Vec2d import Vec2d
from Stalk import Stalk

IMAGE_WIDTH = 1160
IMAGE_HEIGHT = 720


def main():
    # Initializations
    timestamp = str(int(time.time()))
    filename1 = "./sample_output/" + timestamp + "_sturcture.png"
    filename2 = "./sample_output/" + timestamp + "_render.png"
    canvas_struct = Canvas(IMAGE_WIDTH, IMAGE_HEIGHT)
    canvas_render = Canvas(IMAGE_WIDTH, IMAGE_HEIGHT)
    png_painter = Painter()

    # Read sprites
    stalk_sprite = [imageio.imread('./sprite/stalk-1.png'), imageio.imread('./sprite/stalk-2.png'), imageio.imread('./sprite/stalk-3.png')]
    branch_sprite = [imageio.imread('./sprite/branch-1.png'), imageio.imread('./sprite/branch-2.png')]
    leaf_sprite = [imageio.imread('./sprite/leaf-1.png'), imageio.imread('./sprite/leaf-2.png'), imageio.imread('./sprite/leaf-3.png'), imageio.imread('./sprite/leaf-4.png'), imageio.imread('./sprite/leaf-5.png')]
    seal_sprite = imageio.imread('./sprite/seal-90.png')

    print("Constructing...")
    t0 = time.clock()

    # start construction
    quantity = get_bamboo_quantity()
    newest_root = get_root_position(IMAGE_WIDTH)
    roots = list()
    roots.append(newest_root)
    for i in range(quantity - 1):
        newest_root = get_new_root(newest_root.x)
        roots.append(newest_root)

    stalks = list()
    for root in roots:
        length = get_segment_count()
        new_stalk = Stalk(root, length)
        for j in range(length):
            new_stalk.grow()
        stalks.append(new_stalk)

    t1 = time.clock() - t0
    print("Construction time", t1, "seconds.")

    # start rendering
    stalk_count = 1
    stalk_total = len(stalks)
    for stalk in stalks:
        print("Rendering stalk", stalk_count, "/", stalk_total)
        shade = get_shade_degree()
        for seg in stalk.segments:
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

    print("Rendering time", time.clock() - t1, "seconds.")
    print("Saving images...")
    png_painter.paint_png(canvas_struct, filename1)
    png_painter.paint_png(canvas_render, filename2)


def get_bamboo_quantity():
    i = random.randint(1, 100)
    if i <= 6:
        return 1
    elif 6 < i <= 44:
        return 2
    elif 44 < i <= 74:
        return 3
    elif 74 < i <= 88:
        return 4
    elif 88 < i <= 100:
        return 5


def get_segment_count():
    return random.randint(3, 4)


def get_root_position(width):
    return Vec2d(random.randint(int(0.33 * width), int(0.5 * width)), -10)


def get_new_root(root):
    return Vec2d(root + random.randint(100, 200), -10)


def get_stalk_sprite_index():
    return random.randint(0, 2)


def get_branch_sprite_index():
    return random.randint(0, 1)


def get_leaf_sprite_index():
    return random.randint(0, 4)


def get_shade_degree():
    return random.choice([1.0, 0.9, 0.8, 0.6])


main()
