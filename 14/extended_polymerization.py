from collections import Counter

def main(filename):
    with open(filename) as file:
        template = file.readline().replace("\n", "")

        rules = {}
        for line in file.readlines():
            if line != "\n":
                line = line.replace("\n", "").split(" -> ")
                rules[line[0]] = line[1]

        counter = Counter()
        for i in range(len(template)-1):
            counter[template[i]+template[i+1]] += 1

        for i in range(40):
            counter2 = Counter()
            for k in counter:
                counter2[k[0]+rules[k]] += counter[k]
                counter2[rules[k]+k[1]] += counter[k]
            counter = counter2

        counter_chars = Counter()
        for k in counter:
            counter_chars[k[0]] += counter[k]
        counter_chars[template[-1]] += 1
            
        print(counter_chars)

        print("Result: ", max(counter_chars.values()) - min(counter_chars.values()))
            
from sys import argv
if __name__ == "__main__":
    main(argv[1])
