input_path = 'advent_of_code_2020/challenges/Day 18: Operation Order/input'
import tatsu

grammar = '''
    @@grammar::CALC
    start = expression $ ;
    expression = | expression '*' factor | expression '+' factor | factor ;
    factor = | '(' expression ')' | number;
    number = /\d+/ ;
'''

sum = 0
OP = { '+' : lambda a,b: a + b, '*' : lambda a,b: a * b }

def eval(node):
  if (node[0] == '('): return eval(node[1:-1])
  if len(node) == 3: return OP[node[1]](eval(node[0]), eval(node[2]))

  return eval(node[0]) if type(node[0]) == tuple else int(node[0])

with open(input_path) as f:
  for line in f:
    sum += eval(tatsu.parse(grammar, line[:-1]))

print('Part 1: ', sum)
