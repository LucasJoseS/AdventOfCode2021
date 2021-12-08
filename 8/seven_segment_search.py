def main(_input):
    lines = [ line.replace("\n", "") for line in open(_input).readlines() ]

    ones_fours_sevens_and_eights_sum = 0

    for line in lines:
        pattern, nums = line.split("|")
        pattern, nums = pattern.split(), nums.split()

        for num in nums:
            if len(num) in [2, 3, 4, 7]: #num -> 1, 7, 4, 8
                ones_fours_sevens_and_eights_sum+=1

        print(pattern, nums)
    print("sum = ", ones_fours_sevens_and_eights_sum)

from sys import argv
if __name__ == "__main__":
    main(argv[1])
