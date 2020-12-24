from itertools import islice, combinations

file = open("./inputs/day9_input.txt", "r")
lineList = file.read().splitlines()
lineList = [int(line) for line in lineList]
file.close

# Part 1
def findFirstInvalid(preambleLen):
  i = preambleLen
  
  while i < len(lineList):
    precedingNums = islice(lineList, (i-preambleLen), (i))
    
    foundSumMatch = False
    for x,y in combinations(precedingNums, 2):
      if x + y == lineList[i]:
        foundSumMatch = True
        break
    
    if not foundSumMatch:
      return lineList[i]
        
    i += 1
    
  return 'All values have a sum match - none are invalid'

print ('Part 1:', findFirstInvalid(25))


# Part 2
def findAddends(invalidNum):
  testLen = 2
  
  while testLen < len(lineList):
    for j in range(0, len(lineList)+1):
      contiguousSlice = islice(lineList, j, (j+testLen))
      addendsArr = [] # ugly, but can't access values in islice after sum() otherwise
      for p in contiguousSlice:
          addendsArr.append(p)
      testSum = sum(addendsArr)
      if testSum == invalidNum:
        return addendsArr

    testLen += 1
    
  return ('No values sum to make: ' + str(invalidNum))

addends = findAddends(findFirstInvalid(25))
print ('Part 2:', min(addends) + max(addends))
