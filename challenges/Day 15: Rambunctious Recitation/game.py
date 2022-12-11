input_path = 'advent_of_code_2020/challenges/Day 15: Rambunctious Recitation/input'

numbers = []
spoken = {}
last = None

def play_turn(number, turn):
  if (number not in spoken): spoken[number] = [turn]; return

  if (spoken[number].__len__() == 1): spoken[number].append(turn); return

  spoken[number][0] = spoken[number][1]
  spoken[number][1] = turn

with open(input_path) as f:
  for line in f:
    numbers = list(map(int, line[:-1].split(',')))
    for i in range(numbers.__len__()):
      play_turn(numbers[i], i + 1)
      last = numbers[i]

for turn in range(numbers.__len__(), 30000000):
  number = (
    0 if spoken[last].__len__() == 1
    else abs(spoken[last][-1] - spoken[last][-2])
  )

  play_turn(number, turn + 1)
  last = number

print('Part 2: ', last)