input_path = 'advent_of_code_2020/challenges/Day 9: Encoding Error/input'

# Part 1

preamble = 25
numbers = []
sums = {}

def contains(r1, r2): return r1[0] <= r2[0] and r1[1] >= r2[1]

def add_sum_by_tuple(i, j):
  _sum = numbers[i] + numbers[j]
  if (_sum not in sums): sums[_sum] = set()
  sums[_sum].add((min(i, j), max(i, j)))

def update_sums(_range):
  for i in _range:
    for j in _range:
      if (i == j): continue
      add_sum_by_tuple(i, j)

def add_sum(index):
  for i in range(index - preamble, index + 1):
    for j in range(index - preamble, index + 1):
      if (i == j): continue
      add_sum_by_tuple(i, j)

with open(input_path) as f:
  for line in f: numbers.append(int(line[:-1]))

update_sums(range(0, preamble))

for i in range(preamble, numbers.__len__()):
  curr = numbers[i]
  if (curr not in sums): print(curr); break

  filtered = []
  for _range in sums[curr]:
    if (contains([i - preamble, i], _range)): filtered.append(_range)

  if (filtered.__len__() == 0): print(curr); break

  add_sum(i)

sums = {}

# Part 2

def count_up(index, n):
  val = 0
  for j in range(index, numbers.__len__()):
    val += numbers[j]
    if (val > n): return False, []
    if (val == n): return True, [index, j]

def find_contiguous_sums(n):
  for i in range(numbers.__len__()):
    r, _range = count_up(i, n)
    if (r):
      nums = [numbers[w] for w in range(_range[0], _range[1] + 1)]
      return min(nums) + max(nums)

print(find_contiguous_sums(57195069))