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
                file.write(str(canvas.pixels[i][j].r * 255) + " ")
                file.write(str(canvas.pixels[i][j].g * 255) + " ")
                file.write(str(canvas.pixels[i][j].b * 255) + " ")

        file.close()

    def paint_p6(self, canvas, filename):
        file = open(filename, 'w')
        file.write("P6\n")
        file.write(str(canvas.width) + " " + str(canvas.height) + "\n")
        file.write(str(255) + "\n")
        for i in range(canvas.height - 1, -1, -1):
            for j in range(canvas.width):
                file.write("%B" % canvas.pixels[i][j].r * 255)
                file.write("%B" % canvas.pixels[i][j].g * 255)
                file.write("%B" % canvas.pixels[i][j].b * 255)
            file.write("\n")

        file.close()
