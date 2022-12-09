input_path = 'advent_of_code_2020/challenges/Day 14: Docking Data/input'

mem = {}
mask = None

get_binary = lambda x: format(x, 'b').zfill(36)

def apply_mask_to_address(address_bin, mask):
  res = ''
  for i in range(mask.__len__()):
    if (mask[i] == '0'): res += address_bin[i]; continue
    if (mask[i] == '1'): res += mask[i]; continue
    res += 'X'
  return res

def get_posibilities_address(bin):
  posibilities = ['']
  for i in range(bin.__len__()):
    if (bin[i] == 'X'):
      posibilities = list(map(lambda x: x + '0', posibilities)) + list(map(lambda x: x + '1', posibilities))
      continue

    for k in range(posibilities.__len__()):
      posibilities[k] = posibilities[k] + bin[i]
  return posibilities

with open(input_path) as f:
  for line in f:
    if line[:4] == 'mask': mask = line[7:-1]; continue
    assign = line.split(' ')
    address_masked = apply_mask_to_address(get_binary(int(assign[0][4:-1])), mask)
    for add in get_posibilities_address(address_masked):
      mem[int(add, 2)] = int(assign[2])
    
print('Part 2:', sum(mem.values()))