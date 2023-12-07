from typing import Optional

file = open("part2.txt")

lines = [line.strip() for line in file.readlines()]

numMap = {
  'zero': '0',
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

sum = 0

for line in lines:
  first: str = None
  curr: str = None
  left = 0
  right = 0

  def update(value: Optional[str] = None):
    global left
    global right
    left += 1
    right = left
    if value is not None:
      print(line, value)
      global first
      global curr
      global sum
      if first is None:
        first = value
      curr = value

  while left < len(line):
    word = line[left:right]

    if len(word) == 1 and word.isdigit():
      update(word)
      continue

    if word in numMap:
      update(numMap[word])
      continue

    right += 1

    if right > len(line):
      update()

  sum += int(first + curr)

print("Sum:", sum)