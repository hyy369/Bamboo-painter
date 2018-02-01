from Pixel import Pixel

class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []
        for i in range(height):
            new_row = []
            for j in range(width):
                new_row.append(Pixel(1, 1, 1))
            self.pixels.append(new_row)

    def paint_pixel(self, x, y, r, g, b):
        if x < self.width and y < self.height:
            self.pixels[y][x].set_color(r, g, b)

    def paint_pixel_black(self, x, y):
        self.paint_pixel(x, y, 0, 0, 0)

    def paint_pixel_red(self, x, y):
        self.paint_pixel(x, y, 1, 0, 0)

    def paint_seg(self, seg):
        x0 = seg.origin.x
        y0 = seg.origin.y
        # print("x1",x0,"y1",y0)
        x1 = seg.get_end().x
        y1 = seg.get_end().y
        # print("x2",x1,"y2",y1)
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.paint_pixel_black(x, y)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.paint_pixel_black(x, y)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.paint_pixel_black(x, y)

    def paint_joint(self, joint):
        x = joint.x
        y = joint.y
        self.paint_pixel_red(x, y)
        self.paint_pixel_red(x+1, y+1)
        self.paint_pixel_red(x+1, y-1)
        self.paint_pixel_red(x+2, y+2)
        self.paint_pixel_red(x+2, y-2)
        self.paint_pixel_red(x-1, y+1)
        self.paint_pixel_red(x-1, y-1)
        self.paint_pixel_red(x-2, y+2)
        self.paint_pixel_red(x-2, y-2)
