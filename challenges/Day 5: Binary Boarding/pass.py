input_path = 'advent_of_code_2020/challenges/Day 5: Binary Boarding/input'

rows_range = [0, 127]
seats_range = [0, 7]

_max = 0
graph = [[ 0 for _ in range(8)] for _ in range(128)]

def binary_search(to_consume, range, lower, upper, keep_lower):
  for c in to_consume:
    middle = int((range[0] + range[1]) / 2)
    if (c == lower): range[1] = middle
    if (c == upper): range[0] = middle + 1
  return range[0] if keep_lower else range[1]

with open(input_path) as f:
  for line in f:
    row = binary_search(line[:-4], [0, 127], 'F', 'B', True)
    seat = binary_search(line[-4:-1], [0, 7], 'L', 'R', False)
    _max = max(row * 8 + seat, _max)
    graph[row][seat] = 1
    print(row, seat)

print('Part 1:', _max)
print('Part 2: ')
c = 0
for i in graph:
  print('row ', c, ' :', i)
  c+=1
