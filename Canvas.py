import numpy as np
import math
from Vec2d import Vec2d


class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = np.ndarray(shape=(width, height, 4), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                self.pixels[i][j].fill(255)
        # print(self.pixels[0][0])

    def paint_pixel(self, x, y, r, g, b, a):
        if x < self.width and y < self.height:
            # self.pixels[y][x].set_color(r, g, b)
            self.pixels[y][x] = [r, g, b, a]

    def paint_pixel_black(self, x, y):
        self.paint_pixel(x, y, 0, 0, 0, 255)

    def paint_pixel_red(self, x, y):
        self.paint_pixel(x, y, 255, 0, 0, 255)

    def paint_pixel_blue(self, x, y):
        self.paint_pixel(x, y, 0, 0, 255, 255)

    def paint_seg(self, seg, r, g, b, a):
        x0 = seg.origin.x
        y0 = seg.origin.y
        x1 = seg.get_end().x
        y1 = seg.get_end().y
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.paint_pixel(x, y, r, g, b, a)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.paint_pixel(x, y, r, g, b, a)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.paint_pixel(x, y, r, g, b, a)

    def paint_seg_black(self, seg):
        self.paint_seg(seg, 0, 0, 0, 255)

    def paint_seg_green(self, seg):
        self.paint_seg(seg, 0, 255, 0, 255)

    def paint_seg_blue(self, seg):
        self.paint_seg(seg, 0, 0, 255, 255)

    def paint_joint(self, joint, r, g, b, a):
        x = joint.position.x
        y = joint.position.y
        self.paint_pixel(x, y, r, g, b, a)
        self.paint_pixel(x+1, y+1, r, g, b, a)
        self.paint_pixel(x+1, y-1, r, g, b, a)
        self.paint_pixel(x+2, y+2, r, g, b, a)
        self.paint_pixel(x+2, y-2, r, g, b, a)
        self.paint_pixel(x-1, y+1, r, g, b, a)
        self.paint_pixel(x-1, y-1, r, g, b, a)
        self.paint_pixel(x-2, y+2, r, g, b, a)
        self.paint_pixel(x-2, y-2, r, g, b, a)

    def paint_joint_red(self, joint):
        self.paint_joint(joint, 255, 0, 0, 255)

    def paint_joint_green(self, joint):
        self.paint_joint(joint, 0, 255, 0, 255)

    def paint_joint_blue(self, joint):
        self.paint_joint(joint, 0, 0, 255, 255)

    def paint_seg_sprite(self, seg, sprite):
        x_bound = sprite.shape[1] - 1
        y_bound = sprite.shape[0] - 1
        cos = seg.direction.cosine_angle(Vec2d(0, 1))
        sin = -math.sqrt(1 - cos)
        for y in range(self.height):
            for x in range(self.width):
                new_coord = rotate(Vec2d(x, y), cos, sin)
                new_coord = stretch(new_coord, seg, sprite.shape[0]/seg.length)
                new_coord.x -= seg.origin.x - sprite.shape[1] / 2
                new_coord.y -= seg.origin.y
                if new_coord.x < x_bound and new_coord.x > 0 and new_coord.y < y_bound and new_coord.y > 0:
                    self.pixels[y][x] = composite(bilinear_sample(new_coord, sprite), self.pixels[y][x])


def rotate(point, cos, sin):
    result = np.matmul([[cos, -sin], [sin, cos]], [point.x, point.y])
    return Vec2d(result[0], result[1])


def stretch(point, seg, scale):
    dy = (point.y - seg.origin.y) * scale
    y = seg.origin.y + dy
    return Vec2d(point.x, y)


def composite(c1, c2):
    a1 = c1[3] / 255
    a2 = c2[3] / 255
    r = alpha_composite(c1[0], c2[0], a1, a2)
    g = alpha_composite(c1[1], c2[1], a1, a2)
    b = alpha_composite(c1[2], c2[2], a1, a2)
    a = a1 + a2 * (1 - a1)
    a = int(a * 255)
    return [r, g, b, a]


def alpha_composite(ch1, ch2, a1, a2):
    return (ch1 * a1 + ch2 * a2 * (1 - a1)) / (a1 + a2 * (1 - a1))


def bilinear_sample(point, sprite):
    x1 = math.floor(point.x)
    x2 = x1 + 1
    y1 = math.floor(point.y)
    y2 = y1 + 1
    dx = point.x - x1
    dy = point.y - y1
    a = sprite[y1][x1] * (1 - dx) + sprite[y1][x2] * dx
    b = sprite[y2][x1] * (1 - dx) + sprite[y2][x2] * dx
    result = a * (1 - dy) + b * dy
    return result
