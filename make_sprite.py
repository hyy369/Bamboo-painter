import imageio
import sys


def main():
    filename = sys.argv[1]
    print(filename)
    px = imageio.imread(filename)
    for y in range(px.shape[0]):
        for x in range(px.shape[1]):
            shade = px[y][x][0]
            px[y][x] = [0, 0, 0, 255 - shade]
    imageio.imwrite("out" + filename, px)


main()
