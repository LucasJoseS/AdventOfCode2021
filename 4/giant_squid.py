class BoardNum:
    def __init__(self, value):
        self.value = int(value)
        self.checked = False

    def __str__(self):
        return f"{self.value} -> {self.checked}"

class Board:
    def __init__(self, lines):
        self.lines = [[], [], [], [], []]

        for index, line in enumerate(lines):
            for num in line.replace("\n", "").split():
                self.lines[index].append(BoardNum(num))

    def check(self, num):
        for line in self.lines:
            for board_num in line:
                if board_num.value == num:
                    board_num.checked = True

    def winner(self):
        win = False
        for line in self.lines:
            winner_line = True
            for num in line:
                if not num.checked:
                    winner_line = False
                    
            if winner_line:
                win = True
        return win

    def sum_all_unmarked(self):
        s = 0
        for line in self.lines:
            for num in line:
                if not num.checked:
                    s += num.value
        return s
                

def main(filename):
    with open(filename) as file:
        sorted_nums = file.readline().split(",")
        boards_lines = file.readlines()
        boards = list()

        while(boards_lines.count("\n") != 0):
            boards_lines.remove("\n")

        for i in range(0, len(boards_lines), 5):
            boards.append(Board(boards_lines[i:i+5]))

        winner = None
        winner_num = None
        for num in sorted_nums:
            for board in boards:
                if winner == None:
                    board.check(int(num))

                if board.winner() and winner == None:
                    winner = board
                    winner_num = num

        print(winner, " ", winner_num, " ", winner.sum_all_unmarked())


from sys import argv
if __name__ == "__main__":
    main(argv[1])


