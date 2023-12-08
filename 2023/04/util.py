def extract_nums(line: str) -> tuple[list[int], list[int]]:
    return tuple(map(lambda x: x.split(), line.split(': ')[1].split(' | ')))
