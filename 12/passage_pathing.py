caves = dict()

def paths(local, history):
    if local == "end":
        return 1
        
    if local.islower() and local in history:
        return 0

    history.append(local)
    count = 0
    for cave in caves[local]:
        count += paths(cave, history.copy())
    return count  

def main(filename):
    with open(filename) as file:
        paths_lines = [ line.replace("\n", "").split("-") for line in file.readlines() ]

        for first, last in paths_lines:
            try:
                caves[first].append(last)
            except:
                caves[first] = [last]

            try:
                caves[last].append(first)
            except:
                caves[last] = [first]

        print("Paths: ", paths("start", []))
        

from sys import argv
if __name__ == "__main__":
    main(argv[1])
