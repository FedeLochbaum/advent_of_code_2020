from functools import reduce
input_path = 'advent_of_code_2020/challenges/Day 3: Toboggan Trajectory/input'

## Part 1
trees_found = 0

def dict_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([num for num in line[:-1]])
  return array

dict = dict_from_file(input_path)

def check(rows, cols):
  count = 0
  pos = [0, 0] # row, column
  while (pos[0] < dict.__len__()):
    count += (1 if dict[pos[0]][pos[1]] == '#' else 0)
    pos[0] += rows
    pos[1] = (pos[1] + cols) % dict[0].__len__()
  return count

print('Part 1:', check(1, 3))

print('Part 2: ', reduce((lambda x, y: x * y), (check(r, c) for r, c in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]])))