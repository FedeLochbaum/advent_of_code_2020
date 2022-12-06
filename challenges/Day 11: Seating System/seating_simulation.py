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

def adjacent_occupied_count(row, col, graph):
  count = 0
  for _row in range(row - 1, row + 2):
    for _col in range(col - 1, col + 2):
      if (_row == row and _col == col): continue
      if (_row < 0 or _row >= graph.__len__()): continue
      if (_col < 0 or _col >= graph[0].__len__()): continue
      if (graph[_row][_col] == '#'): count += 1
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
      if (seat == '#' and adjacents > 3):
        copy[row][col] = 'L'; changed = True; continue # Release it
  return changed, copy

with open(input_path) as f:
  for line in f:
    _graph.append([num for num in line[:-1]])

while(True):
  changed, _graph = simulate_seating(_graph)
  # print_graph(_graph)
  if (not changed): print(count_occupied_seats(_graph)); break
