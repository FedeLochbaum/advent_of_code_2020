input_path = 'advent_of_code_2020/challenges/Day 12: Rain Risk/input'

L = 'left'; R = 'right'
N = 'north'; S = 'south'; E = 'east'; W = 'west'
waypoint = 'waypoint'; pos = 'pos'

# I only keep the position of North and East, South is interpreted as - North and West as - East (as cartisians axis)
state = { waypoint: { N: 1, E: 10 }, pos: { N: 0, E: 0 } }

def incrementing_to_north(state, count): state[waypoint][N] += count
def decrementing_to_north(state, count): state[waypoint][N] -= count
def incrementing_to_east(state, count): state[waypoint][E] += count
def decrementing_to_east(state, count): state[waypoint][E] -= count

def follow_straight(state, count): state[pos][N] += (count * state[waypoint][N]); state[pos][E] += (count * state[waypoint][E])
def apply_rotation_map(_map, state, param):
  north = state[waypoint][N]; east = state[waypoint][E]
  state[waypoint][N] = _map[param][N](north, east); state[waypoint][E] = _map[param][E](north, east)
def rotate_waypoint(_map): return lambda state, param: apply_rotation_map(_map, state, param)

command_function = {
  'N': incrementing_to_north,
  'S': decrementing_to_north,
  'E': incrementing_to_east,
  'W': decrementing_to_east,

  'R': rotate_waypoint({
    90:  { N: lambda _, e: e * -1, E: lambda n, _: n },
    180: { N: lambda n, _: n * -1, E: lambda _, e: e * -1 },
    270: { N: lambda _, e: e, E: lambda n, _: n * -1 }
  }),
  'L': rotate_waypoint({
    90: { N: lambda _, e: e, E: lambda n, _: n * -1 },
    180: { N: lambda n, _: n * -1, E: lambda _, e: e * -1 },
    270: { N: lambda _, e: e * -1, E: lambda n, _: n }
  }),

  'F': follow_straight,
}

with open(input_path) as f:
  for line in f:
    command_function[line[0]](state, int(line[1:-1]))

print(abs(state[pos][N]) + abs(state[pos][E])) # "Manhattan distance"