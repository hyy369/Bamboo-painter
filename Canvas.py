import numpy as np
from Pixel import Pixel


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
        pass
