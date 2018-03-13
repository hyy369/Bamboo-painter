import imageio

class Painter:

    def __init__(self):
        pass

    def paint_p3(self, canvas, filename):
        file = open(filename, 'w')
        file.write("P3\n")
        file.write(str(canvas.width) + " " + str(canvas.height) + "\n")
        file.write(str(255) + "\n")
        for i in range(canvas.height - 1, -1, -1):
            for j in range(canvas.width):
                file.write(str(canvas.pixels[i][j][0]) + " ")
                file.write(str(canvas.pixels[i][j][1]) + " ")
                file.write(str(canvas.pixels[i][j][2]) + " ")

        file.close()

    def paint_p6(self, canvas, filename):
        file = open(filename, 'w')
        file.write("P6\n")
        file.write(str(canvas.width) + " " + str(canvas.height) + "\n")
        file.write(str(255) + "\n")
        for i in range(canvas.height - 1, -1, -1):
            for j in range(canvas.width):
                file.write("%B" % canvas.pixels[i][j][0])
                file.write("%B" % canvas.pixels[i][j][1])
                file.write("%B" % canvas.pixels[i][j][2])
            file.write("\n")

        file.close()

    def paint_png(self, canvas, filename):
        # Reflect the image vertically
        for i in range(canvas.height // 2):
            canvas.pixels[[i, 511 - i]] = canvas.pixels[[511 - i, i]]
        imageio.imwrite(filename, canvas.pixels)
