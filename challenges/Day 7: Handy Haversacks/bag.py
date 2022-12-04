from collections import deque
input_path = 'advent_of_code_2020/challenges/Day 7: Handy Haversacks/input'

contained_by = {}
bags_from_color = {}
graph = {}

def bfs(_graph, initialNode):
  queue = deque()
  visited = set()
  queue.append(initialNode)
  visited.add(initialNode)
  while(queue):
    node = queue.popleft()
    if (node not in _graph): continue
    for i in _graph[node]:
      if(i not in visited):
        queue.append(i)
        visited.add(i)
  return visited

def count_of_bags(color):
  if (color not in bags_from_color):
    bags_from_color[color] = sum(map(lambda c1: c1[1] + (c1[1] * count_of_bags(c1[0])), graph[color]))

  return bags_from_color[color]

with open(input_path) as f:
  for line in f:
    _color, rest = line[:-1].split(' bags contain ')
    color = _color.strip()
    graph[color] = []
    if (rest[:2] == 'no'): continue
    for contained in rest[:-1].split(','):
      _contained = contained[2:-4].strip()
      if (_contained not in contained_by):
        contained_by[_contained] = []
      graph[color].append([_contained, int(contained[:2])])
      contained_by[_contained].append(color)

print('colors: ', bfs(contained_by, 'shiny gold').__len__() - 1)
print('bags', count_of_bags('shiny gold'))