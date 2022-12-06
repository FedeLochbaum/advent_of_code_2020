input_path = 'advent_of_code_2020/challenges/Day 10: Adapter Array/input'

_graph = {}
adapters = []
_max = 0

outlet_joltage = 0
adapter_resistence = 3
adapter_resistence = 3

def must_include(adapter, element): return element > adapter and (element - adapter) <= 3

def add_adapter_relationships(element):
  if (element not in _graph): _graph[element] = []
  adapters.append(element)

  for adapter in adapters:
    if (must_include(adapter, element)): _graph[adapter].append(element)
    if (must_include(element, adapter)): _graph[element].append(adapter)

# def hamiltonian_path(graph, node, visited, path, n):
#   if path.__len__() == n: return [True, path]

#   for w in graph[node]:
#     if not visited[w]:
#       visited[w] = True
#       path.append(w)

#       found, path = hamiltonian_path(graph, w, visited, path, n)
#       if (found): return [found, path]

#       visited[w] = False
#       path.pop()

#   return [False, path]

with open(input_path) as f:
  add_adapter_relationships(0)

  for line in f:
    adapter = int(line[:-1])
    add_adapter_relationships(adapter)
    _max = max(_max, adapter)

  add_adapter_relationships(_max + 3)
  
  visited = {}
  for i in adapters:
    if i == 0: visited[i] = True; continue
    visited[i] = False

  adapters.sort()
  path = adapters
  ones = 0
  threes = 0
  for i in range(path.__len__()):
    if (i == 0): continue
    if ((path[i] - path[i - 1]) == 1): ones += 1
    if ((path[i] - path[i - 1]) == 3): threes += 1
  print(ones, threes)

# DP
def conbinations_from_array(before, i, array, seen):
  if (not must_include(array[before], array[i])): return 0

  counter = 1
  if (array[i] == array[-1]): return counter

  key = str(array[before]) + str(array[i]) + str(array[i + 1])

  if (key not in seen):
    seen[key] = conbinations_from_array(before, i + 1, array, seen) + conbinations_from_array(i, i + 1, array, seen)
  return seen[key]

print(conbinations_from_array(0, 1, path, {}))
