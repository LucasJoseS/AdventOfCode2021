def pattern_in(pattern, other_pattern):
    if other_pattern == "" or pattern == "": return False
    for char in pattern:
        if not char in other_pattern:
            return False
    return True

def decode_patterns(patterns):
    patterns = patterns.copy()
    decoded_patterns = ["", "", "", "", "", "", "", "", "", ""]

    while(decoded_patterns.count("") > 1):
        for _pattern in patterns:
            pattern = "".join(sorted(_pattern))
            
            if len(pattern) == 2: # one
                decoded_patterns[1] = pattern
                patterns.remove(_pattern)

            if len(pattern) == 4: # four
                decoded_patterns[4] = pattern
                patterns.remove(_pattern)
                
            if len(pattern) == 3: # seven
                decoded_patterns[7] = pattern
                patterns.remove(_pattern)
                
            if len(pattern) == 7: # eight
                decoded_patterns[8] = pattern
                patterns.remove(_pattern)

            if len(pattern) == 6 and pattern_in(decoded_patterns[4], pattern) and pattern_in(decoded_patterns[7], pattern): # nine
                decoded_patterns[9] = pattern
                patterns.remove(_pattern)

            if len(pattern) == 5 and pattern_in(pattern, decoded_patterns[9]) and pattern_in(decoded_patterns[7], pattern): #three
                decoded_patterns[3] = pattern
                patterns.remove(_pattern)

            if len(pattern) == 6 and pattern_in(decoded_patterns[1], pattern) and decoded_patterns[9] != "" and not pattern_in(decoded_patterns[9], pattern): # zero
                decoded_patterns[0] = pattern
                patterns.remove(_pattern)

            if len(pattern) == 5 and pattern_in(pattern, decoded_patterns[9]) and decoded_patterns[7] != "" and not pattern_in(decoded_patterns[7], pattern): # five
                decoded_patterns[5] = pattern
                patterns.remove(_pattern)

            if len(pattern) == 6 and pattern_in(decoded_patterns[5], pattern): # six
                decoded_patterns[6] = pattern
                patterns.remove(_pattern)

    decoded_patterns[2] = "".join(sorted(patterns[0]))

    return decoded_patterns
        

def main(_input):
    lines = [ line.replace("\n", "") for line in open(_input).readlines() ]
    _sum = 0

    for line in lines:
        patterns, nums = line.split("|")
        patterns, nums = patterns.split(), nums.split()
        decoded_patterns = decode_patterns(patterns)

        num = "".join([ str(decoded_patterns.index("".join(sorted(num)))) for num in nums ])
        _sum += int(num)

    print("Sum: ", _sum)

from sys import argv
if __name__ == "__main__":
    main(argv[1])
