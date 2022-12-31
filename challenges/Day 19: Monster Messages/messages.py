input_path = 'advent_of_code_2020/challenges/Day 19: Monster Messages/input0'

sequence_rule = lambda rules: { 'type': 'SEQ', 'rules': rules } # rules is an array of references
or_rule = lambda rules: { 'type': 'OR', 'rules': rules } #
match_rule = lambda char: { 'type': 'MATCH', 'match': char }

memo = {} # str -> { rule -> T | F }
rules = []
matchs = 0

def check_all(rules, string):
  j = -1
  for i in rules:
    j = check_rule(i, string[j + 1:])
    if j == -1: return -1
  return j

def check_seq(node, string): return check_all(node['rules'], string)

def check_or(node, string):
  for sub_rules in node['rules']:
    r = check_all(sub_rules, string)
    if r != -1: return r
  return -1

def check_match(node, string): return string.find(node['match'])

MATCH_BY_TYPE = { 'SEQ': check_seq, 'OR': check_or, 'MATCH': check_match }
def check_rule(rule_index, string):
  if (string not in memo): memo[string] = {}
  if (rule_index not in memo[string]):
    rule = rules[rule_index]
    memo[string][rule_index] = MATCH_BY_TYPE[rule['type']](rule, string)

  return memo[string][rule_index]

with open(input_path) as f:
  end_rules = False
  for line in f:
    if (line == '\n'): end_rules = True; continue
    if (not end_rules):
      rule = line[:-1].split(': ')[1]
      ors = rule.split(' | ')
      if (len(ors) > 1): rules.append(or_rule(list(map(lambda e: list(map(int, e.split(' '))) , ors)))); continue
      elems = rule.split(' ')
      if (len(elems) > 1): rules.append(sequence_rule(list(map(int, elems)))); continue
      rules.append(match_rule(elems[0][1:-1]))
    else:
      if (check_rule(0, line[:-1]) != -1): matchs += 1

print('Part 1: ', matchs)