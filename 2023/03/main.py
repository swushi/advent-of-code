import sys


class PartNumber:
    nums = ''
    adjacent_symbols: set[tuple[str, int, int]] = set()

    def add_num(self, num: str):
        self.nums += num

    def value(self):
        return int(self.nums)

    def __str__(self):
        return f"<PartNumber {self.nums}>"

    def __repr__(self):
        return f"<PartNumber {self.nums}>"


parts: list[PartNumber] = []

file = open(sys.argv[1])
lines = [line.strip() for line in file.readlines()]


def symbol_at_or_none(row, col):
    try:
        if row < 0 or col < 0:
            return None
        char = lines[row][col]
        if char.isdigit() or char == '.':
            return None
        char = lines[row][col]
        return char
    except:
        return None


def find_adjacent_symbols(row: int, col: int):
    comparisons = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1)
    ]

    symbols: set[tuple[str, int, int]] = set()

    for row, col in comparisons:
        adjacent_symbol = symbol_at_or_none(row, col)
        if adjacent_symbol is not None:
            symbols.add((adjacent_symbol, row, col))

    return symbols


for row, line in enumerate(lines):
    part = None

    for col, char in enumerate(line):
        if char.isdigit():
            if part is None:
                part = PartNumber()
                parts.append(part)
            if part is not None:
                part.add_num(char)
                part.adjacent_symbols = part.adjacent_symbols.union(
                    find_adjacent_symbols(row, col))
        else:
            part = None

gears_map = {}

for part in parts:
    gears = [x for x in part.adjacent_symbols if x[0] == '*']
    for gear in gears:
        if gear not in gears_map:
            gears_map[gear] = list([part])
        else:
            gears_map[gear].append(part)

sum = 0
for parts in gears_map.values():
    if len(parts) == 2:
        sum += parts[0].value() * parts[1].value()


print(sum)
