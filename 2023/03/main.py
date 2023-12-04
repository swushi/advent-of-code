class PartNumber:
  nums = ''
  adjacent = False

  def add_num(self, num: str):
    self.nums += num

  def value(self):
    return int(self.nums)

  def __str__(self):
    return f"<PartNumber {self.nums}: {self.adjacent}>"

  def __repr__(self):
    return f"<PartNumber {self.nums}: {self.adjacent}>"



parts: list[PartNumber] = []

file = open('data.txt')
lines = [line.strip() for line in file.readlines()]

def is_symbol(row, col):
  try:
    char = lines[row][col]
    return not char.isdigit() and char != '.'
  except:
    return False

def is_adjacent_to_symbol(row: int, col: int):
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

  for row, col in comparisons:
    if is_symbol(row, col):
      return True

  return False

for row, line in enumerate(lines):
  part = None 

  for col, char in enumerate(line):
    if char.isdigit():
      if part is None:
        part = PartNumber()
        parts.append(part)
      if part is not None:
        part.add_num(char)
        if not part.adjacent:
          part.adjacent = is_adjacent_to_symbol(row, col)
    else:
      part = None

sum = 0
for part in parts:
  if part.adjacent:
    sum += part.value()


print(sum)