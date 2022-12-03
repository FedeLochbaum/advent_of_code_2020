input_path = 'advent_of_code_2020/challenges/Day 6: Custom Customs/input'

## Part 1
group = []
counter = 0

with open(input_path) as f:
  for line in f:
    if (line == '\n'):
      counter += set(group).__len__()
      group = []
    else:
      for c in line[:-1]:
        group.append(c)

print('Part 1:', counter)

## Part 2
group = set()
counter = 0
first = True

with open(input_path) as f:
  for line in f:
    if (line == '\n'):
      counter += group.__len__()
      group = set()
      first = True
    else:
      if (first):
        group = group.union(set(line[:-1]))
        first = False
      else:
        group = group.intersection(set(line[:-1]))

print('Part 2:', counter)