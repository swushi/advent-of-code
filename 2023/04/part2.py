import sys
from util import extract_nums

def main():
    file = open(sys.argv[1])
    lines = [line.strip() for line in file.readlines()]

    copies = {}
    def inc_card_at(card_num):
        if card_num in copies:
            copies[card_num] += 1
        else:
            copies[card_num] = 1

    for i, line in enumerate(lines):
        card_num = i + 1
        inc_card_at(card_num)

        num_copies = copies[card_num]

        theirs, yours = extract_nums(line)
        theirs = set(theirs)

        for num in yours:
            if num in theirs:
                card_num += 1
                for i in range(num_copies):
                    inc_card_at(card_num)

    print(copies)
    print(sum(copies.values()))

if __name__ == '__main__':
    main()