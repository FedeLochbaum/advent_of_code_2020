input_path = 'advent_of_code_2020/challenges/Day 2: Password Philosophy/input'

## Part 1
count = 0

with open(input_path) as f:
  for line in f:
    policy, _password = line[:-1].split(':')
    _range, letter = policy.split(' ')
    _min, _max = _range.split('-')
    if (_password[1:].count(letter) in range(int(_min), int(_max) + 1)):
      count += 1
print('Part 1: ', count)

## Part 2
count = 0

with open(input_path) as f:
  for line in f:
    policy, _password = line[:-1].split(':')
    _range, letter = policy.split(' ')
    _min, _max = _range.split('-')
    if ((_password[int(_min)] == letter and _password[int(_max)] != letter) or (_password[int(_min)] != letter and _password[int(_max)] == letter)):
      count += 1

print('Part 2: ', count)
