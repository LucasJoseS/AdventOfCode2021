def count_dots(paper):
    count = 0
    
    for y in paper:
        for x in y:
            if x == "#":
                count += 1
    return count

def fold_x(paper, pos):
    for y in range(len(paper)):
        for x in range(pos):
            if paper[y][x] == "#":
                paper[y][x*-1-1] = "#"
                paper[y][x] = " "

def fold_y(paper, pos):
    for x in range(len(paper[0])):
        for y in range(pos):
            if paper[y*-1-1][x] == "#":
                paper[y][x] = "#"
                paper[y*-1-1][x] = " "
            

def main(filename):
    with open(filename) as file:
        data = [ line.replace("\n", "").split(",") for line in file.readlines() ]
        coordinates = [(int(x), int(y)) for x, y in data[:data.index([""])]]
        folds = [ data[0].replace("fold along ", "") for data in data[data.index([""])+1:]]

        xsize = 0
        ysize = 0
        for x, y in coordinates:
            if xsize < x:
                xsize = x

            if ysize < y:
                ysize = y
        
        paper = [[" " for _ in range(xsize+1)] for _ in range(ysize+1)]
        
        for x, y in coordinates:
            paper[y][x] = "#"

        type, pos = folds[0].split("=")

        if type == "y":
            fold_y(paper, int(pos))
        else:
            fold_x(paper, int(pos))

        print("dots: ", count_dots(paper))




from sys import argv
if __name__ == "__main__":
    main(argv[1])
