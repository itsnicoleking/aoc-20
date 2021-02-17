import re

file = open("./inputs/day14_input.txt", "r")
lineList = file.read().splitlines()
file.close

# Part 1
mask = ''
mem = {}

for line in lineList:
  if 'mask' in line:
    mask = line.split('=')[1].strip()
  elif 'mem' in line:
    line = line.split('=')
    addr = int(re.sub("[a-z\[\]]", "", line[0]))
    value = list(format(int(line[1].strip()), "036b"))
    for i, v in enumerate(mask):
      if v != 'X':
        value[i] = v
    mem[addr] = int("".join(value), 2)

print('Part1:', sum([mem[i] for i in mem]))
    
# Bitwise style
# if v == 'X':
#     pass
# elif v == '1':
#     val = val | (2 ** (36 - i - 1))
# elif v == '0':
#     val = val & ~(2 ** (36 - i - 1))


# https://www.reddit.com/r/adventofcode/comments/kcr1ct/2020_day_14_solutions/
# https://github.com/mariothedog/Advent-of-Code-2020/blob/main/Day%2014/day_14.py
