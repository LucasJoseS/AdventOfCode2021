def main():
    last_in = input()
    last_num = int()
    is_first = True
    count = 0

    while last_in != "EOF":
        if is_first:
            last_num = int(last_in)
            is_first = False
            continue

        if last_num < int(last_in):
            count += 1

        last_num = int(last_in)
        last_in = input()

    return count
    
if __name__ == "__main__":
    print(main())

