from copy import deepcopy
input_path = 'advent_of_code_2020/challenges/Day 12: Rain Risk/input'

L = 'left'; R = 'right'
N = 'north'; S = 'south'; E = 'east'; W = 'west'
facing = 'facing_to'; pos = 'pos'

# I only keep the position of North and East, South is interpreted as - North and West as - East (as cartisians axis)
state = { facing: E, pos: { N: 0, E: 0 } }

def incrementing_to_north(state, count): state[pos][N] += count
def decrementing_to_north(state, count): state[pos][N] -= count
def incrementing_to_east(state, count): state[pos][E] += count
def decrementing_to_east(state, count): state[pos][E] -= count

def follow_straight(state, count):
  if state[facing] == N: return incrementing_to_north(state, count)
  if state[facing] == S: return decrementing_to_north(state, count)
  if state[facing] == E: return incrementing_to_east(state, count)
  
  return decrementing_to_east(state, count)

def apply_rotation_map(_map, state, param): state[facing] = _map[param][state[facing]]
def rotate_to(_map): return lambda state, param: apply_rotation_map(_map, state, param)

command_function = {
  'N': incrementing_to_north,
  'S': decrementing_to_north,
  'E': incrementing_to_east,
  'W': decrementing_to_east,

  'L': rotate_to({ 90: { S: E, N: W, E: N, W: S }, 180: { S: N, N: S, E: W, W: E }, 270: { S: W, N: E, E: S, W: N } }),
  'R': rotate_to({ 90: { S: W, N: E, E: S, W: N }, 180: { S: N, N: S, E: W, W: E }, 270: { S: E, N: W, E: N, W: S } }),

  'F': follow_straight,
}

with open(input_path) as f:
  for line in f:
    command_function[line[0]](state, int(line[1:-1]))

print(abs(state[pos][N]) + abs(state[pos][E])) # "Manhattan distance"