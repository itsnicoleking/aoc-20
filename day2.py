import re

file = open("./inputs/day2_input.txt", "r")
lineList = [line.rstrip('\n') for line in file]
file.close

# Part 1
numValid1 = 0
for line in lineList:
  split = re.split(': |-| ', line)
  counter = split[3].count(split[2])
  
  if counter >= int(split[0]) and counter <= int(split[1]):
    numValid1+=1
  
print ('Answer:', numValid1)

# Part 2
numValid2 = 0
for line in lineList:
  split = re.split(': |-| ', line)
  pos1 = int(split[0])-1
  pos2 = int(split[1])-1
  char = split[2]
  
  if (split[3][pos1] == char) ^ (split[3][pos2] == char):
    numValid2+=1
    
print ('Answer:', numValid2)
