def calc_gramma_rate(count_ones: list, total: int) -> str:
    return "".join([ "1" if num > total/2 else "0" for num in count_ones])

def calc_epsilion_rate(gramma_rate: str) -> str:
    return "".join(["0" if grama == "1" else "1" for grama in gramma_rate])

def find_oxygen_generation_rating(content: list, index: int = 0):
    if len(content) == 1:
        return content[0]

    ones = count_ones(content)
    select = ''
    if ones[index] >= len(content)/2:
        select = '1'
    else:
        select = '0'

    return find_oxygen_generation_rating([con for con in content if con[index] == select], index+1)



def find_CO2_crubber_rating(content: list, index: int = 0):
    if len(content) == 1:
        return content[0]

    ones = count_ones(content)
    select = ''
    if ones[index] >= len(content)/2:
        select = '0'
    else:
        select = '1'

    return find_CO2_crubber_rating([con for con in content if con[index] == select], index+1)

def count_ones(content: list):
    ones = [0] * len(content[0])
    for line in content:
        for index, char in enumerate(line):
            if char == "1":
                ones[index] += 1

    return ones


def main(filename: str) -> None:
    content = [line.replace("\n", "") for line in open(filename, "r").readlines()]
    ones = count_ones(content)

    gramma_rate = calc_gramma_rate(ones, len(content))
    epsilion_rate = calc_epsilion_rate(gramma_rate)

    print("The life support rating is: ", int(find_oxygen_generation_rating(content), 2) * int(find_CO2_crubber_rating(content), 2))
    print("The power consumption is: ", int(gramma_rate, 2) * int(epsilion_rate, 2))

from sys import argv
if __name__ == "__main__":
    main(argv[1])
