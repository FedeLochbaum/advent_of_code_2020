input_path = 'advent_of_code_2020/challenges/Day 17: Conway Cubes/input'
from collections import deque
import itertools

points = set([])
cycles = 6

neighboring = list(itertools.product([-1,0,1], repeat=3))
def neighbors(p): return map(lambda v: (p[0] + v[0], p[1] + v[1], p[2] + v[2]), neighboring)

def cycle(_points):
  result = set()
  inactives = deque([])
  for p in _points:
    actives = 0
    for n in neighbors(p):
      if n == p: continue
      if n in _points: actives += 1; continue
      
      inactives.append(n)
    if actives in [2, 3]: result.add(p)

  while inactives:
    p = inactives.popleft()
    actives = 0
    for n in neighbors(p):
      if n == p: continue
      if n in _points: actives += 1; continue
    if actives == 3: result.add(p)

  return result

with open(input_path) as f:
  y = 0
  for line in f:
    for x in range(len(line[:-1])):
      if (line[x] == '#'): points.add((x, y, 0))
    y += 1

for _ in range(cycles): points = cycle(points)

print('Part 1: ', len(points))