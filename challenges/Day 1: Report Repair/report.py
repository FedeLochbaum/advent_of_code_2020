input_path = 'advent_of_code_2020/challenges/Day 1: Report Repair/input'

## Part 1
seen = {}

with open(input_path) as f:
  for line in f:
    expected = 2020 - int(line)
    if (expected in seen):
      result = expected * int(line)
      break;
    seen[int(line)] = {}
print('Part 1: ', result)

## Part 2
rest_for_2020 = {}

with open(input_path) as f:
  for line in f:
    rest = 2020 - int(line)
    rest_for_2020[rest] = {}
    for k in rest_for_2020:
      if int(line) < k:
        rest_for_2020[k][k - int(line)] = {}
        for k_2 in rest_for_2020[k]:
          if (int(line) == k_2):
            result = int(line) * (k - k_2) * (2020 - k)
            break;
print('Part 2: ', result)