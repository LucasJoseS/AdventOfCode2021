caves = dict()
unique_paths = list()

def paths_with_chosen_one(local, history, chosen_one):
    if local == "end":
        if history not in unique_paths:
            unique_paths.append(history)
            return 1
        else:
            return 0
        
    if local.islower() and local in history:
        if local != chosen_one or history.count(chosen_one) == 2:
            return 0

    history.append(local)
    count = 0

    for cave in caves[local]:
        count += paths_with_chosen_one(cave, history.copy(), chosen_one)
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

        small_caves = [cave for cave in caves.keys() if cave.islower() and cave != "start" and cave != "end"]
        print("Paths: ", sum([paths_with_chosen_one("start", list(), chosen) for chosen in small_caves]))
        

from sys import argv
if __name__ == "__main__":
    main(argv[1])
