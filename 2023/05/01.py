import sys
import re
from typing import List


class CategoryMapRange:
    def __init__(self, line: str):
        nums = line.split(' ')
        self.dest_start = int(nums[0])
        self.source_start = int(nums[1])
        self.length = int(nums[2])


class CategoryMap:
    def __init__(self, lines: List[str]):
        self.source, self.destination = re.search(
            r"(\w+)-to-(\w+) map:", lines[0]).groups()
        self.ranges = [CategoryMapRange(line) for line in lines[1:]]


def main():
    file = open(sys.argv[1])
    groups = list(map(lambda x: x.split('\n'), file.read().split('\n\n')))
    seeds = re.findall(r"\d+", groups[0][0])
    category_maps = [CategoryMap(x) for x in groups[1:]]


if __name__ == '__main__':
    main()
