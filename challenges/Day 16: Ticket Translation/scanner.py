input_path = 'advent_of_code_2020/challenges/Day 16: Ticket Translation/input'

ticket_scanning_error_rate = 0

reading_my_ticket = False
my_ticket = []
reading_tickets = False
constraints = []
valids = []

class Constraint:
  def __init__(self, name, range1, range2):
    self.name = name
    self.ranges = [range(int(range1[0]), int(range1[1]) + 1), range(int(range2[0]), int(range2[1]) + 1)]
  
  def is_in(self, n): return n in self.ranges[0] or (n in self.ranges[1])
  def all_match(self, array):
    for x in array:
      if (not self.is_in(x)): return False

    return True

def is_valid(n, constraints):
  for constraint in constraints:
    if (constraint.is_in(n)): return True

  return False

with open(input_path) as f:
  for line in f:
    if (line == '\n'): continue
    if (line[:-1] == 'your ticket:'): reading_my_ticket = True; continue
    if (line[:-1] == 'nearby tickets:'): reading_tickets = True; continue

    if (not reading_my_ticket and not reading_tickets):
      ranges = line[:-1].split(' ')[-3:]
      range1 = ranges[0].split('-')
      range2 = ranges[2].split('-')
      constraints.append(Constraint(line.split(':')[0], range1, range2))
      continue

    if (reading_my_ticket and not reading_tickets): my_ticket = list(map(int, line[:-1].split(','))); continue

    if (reading_tickets):
      ticket_nums = list(map(int, line[:-1].split(',')))
      curret_is_valid = True
      for i in range(ticket_nums.__len__()):
        if (not is_valid(ticket_nums[i], constraints)):
          curret_is_valid = False; ticket_scanning_error_rate += ticket_nums[i]
      
      if (curret_is_valid): valids.append(ticket_nums)

print('Part 1: ', ticket_scanning_error_rate)
print('valids: ', valids.__len__())