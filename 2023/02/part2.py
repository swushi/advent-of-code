

with open('data.txt') as file:
  lines = [f.strip() for f in file.readlines()]

  sum = 0

  for game in lines:
    possible = True
    idStr, roundsStr = game.split(': ')
    id = int(idStr.split()[1])

    maxs = {
      'blue': 0,
      'green': 0,
      'red': 0
    }

    rounds = roundsStr.split('; ')

    for round in rounds:
      colors = round.split(', ')

      for color in colors:
        amount, color = color.split(' ')

        maxs[color] = max(int(amount), maxs[color])
    
    power = maxs['blue'] * maxs['green'] * maxs['red']
    sum += power

  print(sum)
