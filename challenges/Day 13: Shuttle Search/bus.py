input_path = 'advent_of_code_2020/challenges/Day 13: Shuttle Search/input'

min_ = None
to_minimize = None
buses = []
with open(input_path) as f:
  for line in f:
    if (not to_minimize): to_minimize = int(line[:-1]); continue

    i = -1
    for num in line[:-1].split(','):
      i += 1
      if num == 'x': continue
      id = int(num)
      buses.append([id, i])
      t = to_minimize / id
      times = int(t) + (1 if (t - int(t)) > 0 else 0)
      diff = (times * id) - to_minimize
      if (min_ == None or diff < min_[0]): min_ = [diff, id * diff]

print('Part 1: ', min_[1])

index = 1
t = 0

for bus in buses:
  while True:
    t += index
    if (t + bus[1]) % bus[0] == 0: index = index * bus[0]; break

print('Part 2: ', t)
