import random
import time

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
    filename = str(int(time.time())) + ".ppm"
    size = 512
    canvas = Canvas(size, size)
    ppm_painter = Painter()

    quantity = generate_bamboo_quantity()
    newest_root = generate_root_position(size)
    roots = list()
    roots.append(newest_root)
    for i in range(quantity - 1):
        newest_root = generate_new_root(newest_root.x)
        roots.append(newest_root)

    stalks = list()
    for root in roots:
        new_stalk = Stalk(root)
        for j in range(generate_segment_count()):
            new_stalk.grow()
        stalks.append(new_stalk)

    for stalk in stalks:
        for seg in stalk.segments:
            canvas.paint_seg(seg)
        for joint in stalk.joints:
            canvas.paint_joint(joint)

    ppm_painter.paint_p3(canvas, filename)
    # ppm_painter.paint_p6(canvas, filename)


main()
