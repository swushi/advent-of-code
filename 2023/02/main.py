limits = {
  'blue': 14,
  'green': 13,
  'red': 12
}

with open('data.txt') as file:
  lines = [f.strip() for f in file.readlines()]

  sum = 0

  for game in lines:
    possible = True
    idStr, roundsStr = game.split(': ')
    id = int(idStr.split()[1])

    rounds = roundsStr.split('; ')

    for round in rounds:
      colors = round.split(', ')

      for color in colors:
        amount, color = color.split(' ')
        if int(amount) > limits[color]:
          possible = False
          break

    if possible:
      sum += id

print(sum)