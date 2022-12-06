from copy import deepcopy
input_path = 'advent_of_code_2020/challenges/Day 11: Seating System/input'

_graph = []

def print_graph(graph):
  for i in graph:
    print(''.join(i))

def count_occupied_seats(graph): # One can omit this just calculating the total number and going increasing/decreasing the counter
  occupied_seats = 0
  for row in graph:
    for e in row:
      if (e == '#'): occupied_seats += 1
  return occupied_seats

def look_until_see_seat(point, next_point, graph):
  seat = None
  while(True):
    next_r, next_c = next_point(point[0], point[1])
    if (next_r < 0 or next_r >= graph.__len__()): break
    if (next_c < 0 or next_c >= graph[0].__len__()): break

    elem = graph[next_r][next_c]
    if (elem != '.'): return elem
    point = [next_r, next_c]
  return seat

def adjacent_occupied_count(row, col, graph):
  count = 0
  if (look_until_see_seat([row, col], lambda r, c: [r - 1, c - 1], graph) == '#'): count += 1
  if (look_until_see_seat([row, col], lambda r, c: [r - 1, c], graph) == '#'): count += 1
  if (look_until_see_seat([row, col], lambda r, c: [r - 1, c + 1], graph) == '#'): count += 1
  if (look_until_see_seat([row, col], lambda r, c: [r, c - 1], graph) == '#'): count += 1
  if (look_until_see_seat([row, col], lambda r, c: [r, c + 1], graph) == '#'): count += 1
  if (look_until_see_seat([row, col], lambda r, c: [r + 1, c - 1], graph) == '#'): count += 1
  if (look_until_see_seat([row, col], lambda r, c: [r + 1, c], graph) == '#'): count += 1
  if (look_until_see_seat([row, col], lambda r, c: [r + 1, c + 1], graph) == '#'): count += 1

  return count

def simulate_seating(graph):
  changed = False
  copy = deepcopy(graph)
  for row in range(graph.__len__()):
    for col in range(graph[row].__len__()):
      seat = graph[row][col]

      if (seat == '.'): continue
      adjacents = adjacent_occupied_count(row, col, graph)
      if (seat == 'L' and adjacents == 0):
        copy[row][col] = '#'; changed = True; continue # Ocuppy it
      if (seat == '#' and adjacents > 4): # 3 -> 4
        copy[row][col] = 'L'; changed = True; continue # Release it
  return changed, copy

with open(input_path) as f:
  for line in f:
    _graph.append([num for num in line[:-1]])

while(True):
  changed, _graph = simulate_seating(_graph)
  if (not changed): print(count_occupied_seats(_graph)); break
