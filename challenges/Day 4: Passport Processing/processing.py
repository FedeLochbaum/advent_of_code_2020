import re
input_path = 'advent_of_code_2020/challenges/Day 4: Passport Processing/input'

valids = 0

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

needed_keys = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]

check_value = {
  'byr': lambda y: int(y) in range(1920, 2002 + 1),
  'iyr': lambda y: int(y) in range(2010, 2020 + 1),
  'eyr': lambda y: int(y) in range(2020, 2030 + 1),
  'hgt': lambda hgt: int(hgt[:-2]) in range(150, 193 + 1) if hgt[-2:] == 'cm' else int(hgt[:-2]) in range(59, 76 + 1),
  'hcl': lambda hcl: hcl[0] == '#' and hcl[1:].__len__() == 6,
  'ecl': lambda e: e in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
  'pid': lambda id: re.findall('[0-9]+', id).__len__() == 1 and re.findall('[0-9]+', id)[0].__len__() == 9
}

current = {}
with open(input_path) as f:
  for line in f:
    if (line == '\n'):
      valids += 1 if all((n_k in current and check_value[n_k](current[n_k])) for n_k in needed_keys) else 0
      current = {}
      continue;
    for field in line[:-1].split(' '):
      key, value = field.split(':')
      current[key] = value

print('valids: ', valids)
