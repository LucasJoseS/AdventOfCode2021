def main(filename):
    with open(filename) as file:
        data = [ line.replace("\n", "").split(",") for line in file.readlines() ]
        coordinates = [(int(x), int(y)) for x, y in data[:data.index([""])]]
        folds = [ data[0].replace("fold along ", "") for data in data[data.index([""])+1:]]
        paper = {}

        for x, y in coordinates:
            paper[(x, y)] = True

        for fold in folds:
            type, pos = fold.split("=")
            pos = int(pos)
            p = {}

            if type == 'x': 
                for (x, y) in paper:
                    if x < pos:
                        p[(x, y)] = True
                    else:
                        p[(pos-(x-pos), y)] = True

            if type == "y":
                for (x, y) in paper:
                    if y < pos:
                        p[(x, y)] = True
                    else:
                        p[(x, pos-(y-pos))] = True

            paper = p

        x = max([ x for x, _ in paper.keys() ])
        y = max([ y for _, y in paper.keys() ])

        buff = ''
        for y in range(y+1):
            for x in range(x+1):
                buff += "#" if (x, y) in paper else ' '
            print(buff)
            buff = ''

from sys import argv
if __name__ == "__main__":
    main(argv[1])
