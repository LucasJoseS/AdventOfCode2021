def insert(polymer, obj):
    return polymer[0] + obj + polymer[1]

def main(filename):
    with open(filename) as file:
        template = file.readline().replace("\n", "")
        rules = {}

        for line in file.readlines():
            if line != "\n":
                line = line.replace("\n", "").split(" -> ")
                rules[line[0]] = line[1]

        pool = [ char for char in template ]

        final = 10
        step = 0
        while(step < final):
            npool = " "
            for polymer in [ pool[i] + pool[i+1] for i in range(len(pool)-1)]:
                npool = npool[0:-1] + insert(polymer, rules[polymer])
            pool = npool
            step += 1

        counts = [ pool.count(char) for char in set(pool) ]
        print("Result: ", max(counts) - min(counts))
            
from sys import argv
if __name__ == "__main__":
    main(argv[1])
