input_path = 'advent_of_code_2020/challenges/Day 14: Docking Data/input'

mem = {}
mask = None

get_binary = lambda x: format(x, 'b').zfill(36)

def apply_mask(bin, mask):
  res = ''
  for i in range(mask.__len__()):
    if (mask[i] != 'X'): res += mask[i]; continue
    res += bin[i]
  return res

with open(input_path) as f:
  for line in f:
    if line[:4] == 'mask': mask = line[7:-1]; continue

    assign = line.split(' ')
    binary = get_binary(int(assign[2]))
    mem[int(assign[0][4:-1])] = int(apply_mask(binary, mask), 2)
    
print('Part 1:', sum(mem.values()))

