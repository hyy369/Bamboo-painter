class Painter:

    def paint(self, canvas):
        file = open('test.ppm', 'w')
        file.write("P3\n")
        file.write(str(canvas.width) + " " + str(canvas.height) + "\n")
        file.write(str(255) + "\n")
        for i in range(canvas.height - 1, -1, -1):
            for j in range(canvas.width):
                file.write(str(canvas.pixels[i][j].r * 255) + " ")
                file.write(str(canvas.pixels[i][j].g * 255) + " ")
                file.write(str(canvas.pixels[i][j].b * 255) + "  ")
            #print(chr(int(canvas.pixels[i].r * 511)), end="")
            #print(chr(int(canvas.pixels[i].g * 511)), end="")
            #print(chr(int(canvas.pixels[i].b * 511)), end="")
            #print()

        file.close()
