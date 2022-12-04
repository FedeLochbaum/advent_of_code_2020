input_path = 'advent_of_code_2020/challenges/Day 8: Handheld Halting/input'

program = []

def instruction(line):
  op, param = line.split(' ')
  return { 'op': op, 'param': int(param) }

def acc(param, state):
  state['acc'] += param
  state['pointer'] += 1

def nop(_, state):
  state['pointer'] += 1

def jmp(param, state):
  state['pointer'] += param

apply_instruction = { 'acc': acc, 'jmp': jmp, 'nop': nop }

def exec(p, state):
  pointers = {}
  ends = True
  while(state['pointer'] < p.__len__()):
    if (state['pointer'] in pointers): ends = False; break

    pointers[state['pointer']] = True
    inst = program[state['pointer']]
    apply_instruction[inst['op']](inst['param'], state)

  return ends, state

with open(input_path) as f:
  for line in f: program.append(instruction(line[:-1]))

print(exec(program, { 'acc': 0, 'pointer': 0 }))

def check_and_print_result(inst, state):
  prev = inst['op']
  inst['op'] = 'nop' if inst['op'] == 'jmp' else 'jmp'
  ends, state = exec(program, { 'acc': 0, 'pointer': 0 })
  if (ends): print(state)
  inst['op'] = prev

for inst in program:
    if (inst['op'] == 'nop' or inst['op'] == 'jmp'): check_and_print_result(inst, { 'acc': 0, 'pointer': 0 })