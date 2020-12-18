file = open("./inputs/day3_input.txt", "r")
lineList = [line.rstrip('\n') for line in file]
file.close

# Part 1
numTrees = 0
tree = '#'
maxHeight = len(lineList)-1
ypos = 0
xpos = 0

while ypos <= maxHeight:
  if lineList[ypos][xpos % len(lineList[ypos])] == tree:
    numTrees+=1
  ypos+=1
  xpos+=3

print ('Answer:', numTrees)

# Part 2
def numTreesHit(numRight, numDown):
  numTrees2 = 0
  tree = '#'
  maxHeight = len(lineList)-1
  ypos = 0
  xpos = 0

  while ypos <= maxHeight:
    if lineList[ypos][xpos % len(lineList[ypos])] == tree:
      numTrees2+=1
    ypos+=numDown
    xpos+=numRight
  
  return numTrees2

numTreesProduct = numTreesHit(1,1)
numTreesProduct *= numTreesHit(3,1)
numTreesProduct *= numTreesHit(5,1)
numTreesProduct *= numTreesHit(7,1)
numTreesProduct *= numTreesHit(1,2)

print ('Answer:', numTreesProduct)
