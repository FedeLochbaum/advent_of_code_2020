input_path = 'advent_of_code_2020/challenges/Day 16: Ticket Translation/input'

ticket_scanning_error_rate = 0

reading_my_ticket = False
reading_tickets = False

constraints = [] # array of two ranges

def is_valid(n, constraints):
  res = False
  for pair in constraints:
    if (n in pair[0] or n in pair[1]): return True

  return res

with open(input_path) as f:
  for line in f:
    if (line == '\n'): continue
    if (line[:-1] == 'your ticket:'): reading_my_ticket = True; continue
    if (line[:-1] == 'nearby tickets:'): reading_tickets = True; continue

    if (not reading_my_ticket and not reading_tickets):
      ranges = line[:-1].split(' ')[-3:]
      range1 = ranges[0].split('-')
      range2 = ranges[2].split('-')
      constraints.append([range(int(range1[0]), int(range1[1]) + 1), range(int(range2[0]), int(range2[1]) + 1)])
      continue

    if (reading_my_ticket and not reading_tickets): continue # ignored for the moment

    if (reading_tickets):
      for n in map(int, line[:-1].split(',')):
        if (not is_valid(n, constraints)): ticket_scanning_error_rate += n

print('Part 1: ', ticket_scanning_error_rate)