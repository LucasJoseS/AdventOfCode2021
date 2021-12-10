cl_chunks = ")]}>"
op_chunks = "([{<"

def is_open_chunck(char):
    return char in op_chunks

def chunk_match(op, cl):
    return op_chunks[cl_chunks.index(cl)] == op

def points(char):
    if char == ")": return 3
    if char == "]": return 57
    if char == "}": return 1197
    if char == ">": return 25137

def main(filename):
    errors = list()
    
    with open(filename) as file:
        stack = list()

        for line in file:
            for char in line.replace("\n", ""):
                if is_open_chunck(char):
                    stack.append(char)
                else:
                    op_char = stack.pop()

                    if not chunk_match(op_char, char):
                        errors.append(char)
                        break;

    print("Syntax error points: ", sum([points(char) for char in errors]))
                    
        

from sys import argv
if __name__ == "__main__":
    main(argv[1])
