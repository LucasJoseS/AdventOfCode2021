def calc_gramma_rate(count_ones: list, total: int) -> str:
    return "".join([ "1" if num > total/2 else "0" for num in count_ones])

def calc_epsilion_rate(gramma_rate: str) -> str:
    return "".join(["0" if grama == "1" else "1" for grama in gramma_rate])


def main(filename: str) -> None:
    content = [line.replace("\n", "") for line in open(filename, "r").readlines()]

    ones = [0] * len(content[0])
    for line in content:
        for index, char in enumerate(line):
            if char == "1":
                ones[index] += 1

    gramma_rate = calc_gramma_rate(ones, len(content))
    epsilion_rate = calc_epsilion_rate(gramma_rate)

    print("The power consumption is: ", int(gramma_rate, 2) * int(epsilion_rate, 2))

from sys import argv
if __name__ == "__main__":
    main(argv[1])
