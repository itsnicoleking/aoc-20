import itertools

file = open("./inputs/day1_input.txt", "r")
lineList = [int(line) for line in file]
file.close

# Part 1
for x,y in itertools.combinations(lineList, 2):
  if x + y == 2020:
    print (x,y)
    print ('Answer:', x*y)
    break

# Part 2
for x,y,z in itertools.combinations(lineList, 3):
  if x + y + z == 2020:
    print (x,y,z)
    print ('Answer:', x*y*z)
    break
    