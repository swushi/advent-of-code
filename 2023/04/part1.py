import sys
from util import extract_nums

def main():
    file = open(sys.argv[1])
    lines = [line.strip() for line in file.readlines()]

    total_score = 0

    for line in lines:
        score = 0
        theirs, yours = extract_nums(line)
        theirs = set(theirs)

        for num in yours:
            if num in theirs:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total_score += score

    print('Total score:', total_score)

if __name__ == '__main__':
    main()