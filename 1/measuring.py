from sys import argv

def main():
    values = [value.replace("\n", "") for value in open(argv[1]).readlines()]
    window_a = 0
    window_b = 0
    window_b_back = 0
    counter = 0
    window_range = 3

    for i in range(0, len(values)-2, 2):
        for value in values[slice(i, i+window_range)]:
            window_a += int(value)

        for value in values[slice(i+1, i+window_range+1)]:
            window_b += int(value)

        if window_a < window_b:
            counter += 1

        if window_b_back != 0 and window_b_back < window_a:
            counter += 1

        window_b_back = window_b
        window_a = window_b = 0

    return counter


   
if __name__ == "__main__":
    print(main())

