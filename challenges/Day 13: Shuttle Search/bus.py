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
      if (id == i): print('hola! esto es rarin')
      buses.append([id, i])
      t = to_minimize / id
      times = int(t) + (1 if (t - int(t)) > 0 else 0)
      diff = (times * id) - to_minimize
      if (min_ == None or diff < min_[0]): min_ = [diff, id * diff]

print('Part 1: ', min_[1])

t = buses[0][0] * (100000000000000 / buses[0][0])

def check_buses(t):
  res = True

  for bus in buses[1:]:
    if (t % bus[0] != (bus[0] - bus[1])): return False

  return res

while(True):
  t += buses[0][0]
  # if (t < 100000000000000): continue
  if(check_buses(t)): print('Part 2:', t); break

  agarro (n, i),
 