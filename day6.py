file = open("./inputs/day6_input.txt", "r")
lineList = file.read().split('\n\n')
lineList = [x.replace('\n', ' ').split() for x in lineList]
file.close

# Part 1
countSum = 0

for line in lineList:
  combined = ''.join(lineList[lineList.index(line)])
  countSum += len(set(combined))
  
print ('Part 1:', countSum)

# Part 2
countSum2 = 0

for line in lineList:
  sets = [set(x) for x in line]
  intersect = sets[0].intersection(*sets)
  countSum2 += len(intersect)

print ('Part 2:', countSum2)