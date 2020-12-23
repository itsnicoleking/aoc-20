file = open("./inputs/day7_input.txt", "r")
lineList = file.read().splitlines()
file.close

allBags = dict()

for line in lineList:
  line = line.replace(' bags', '').replace(' bag', '').replace('.', '')
  line = line.split(' contain ')
  allBags[line[0]] = line[1]


# Part 1
parentBags = set()

def findAllParents(bagName):
  global hohoho
  for parent in allBags:
    if bagName in allBags[parent]:
      parentBags.add(parent)
      findAllParents(parent)

  return parentBags

print ('Part 1:', len(findAllParents('shiny gold')))


# Part 2
childBags = {}

def findNumChildren(bagName):
  parentVals = allBags[bagName].split(', ')
  if parentVals[0] == 'no other':
    return
  else:
    for child in parentVals:
      num = int(child[0])
      name = ' '.join(child.split()[1:])
      if name in childBags:
        childBags[name] += num
      else:
        childBags[name] = num
      for x in range(num):
        findNumChildren(name)
          
    return childBags

print ('Part 2:', sum(findNumChildren('shiny gold').values()))