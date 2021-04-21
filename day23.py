from collections import deque
import time, datetime

# Part 1
def playMovesPartOne(cupDeck, numMoves):
  i = numMoves
  while i > 0:
    playMove(cupDeck)
    i-=1
    
  # put '1' at end and pop
  cupDeck.rotate(len(cupDeck)-(cupDeck.index(1)+1))
  cupDeck.pop()
  return ''.join(str(i) for i in cupDeck)

def playMove(cupDeck):
  # move current cup to end & save its value
  cupDeck.rotate(-1) 
  currCupVal = cupDeck[-1]
  
  # pop next 3 cups
  pickup = []
  pickup.append(cupDeck.popleft())
  pickup.append(cupDeck.popleft())
  pickup.append(cupDeck.popleft())
  
  # get destination cup label
  destCupVal = currCupVal - 1 
  while destCupVal not in cupDeck:
    destCupVal -= 1
    if destCupVal < min(cupDeck):
      destCupVal = max(cupDeck)
  
  # insert removed to left of destination index
  destCupIndex = cupDeck.index(destCupVal)
  cupDeck.insert(destCupIndex + 1, pickup[0])
  cupDeck.insert(destCupIndex + 2, pickup[1])
  cupDeck.insert(destCupIndex + 3, pickup[2])

partOneInput = [2,8,4,5,7,3,9,6,1]
cq1 = deque(maxlen=len(partOneInput))
for each in partOneInput:
  cq1.append(each)

# print('Part 1:', playMovesPartOne(cq1, 100))


# Part 2, attempt 1
# this disaster would take ~69 days to run
def playMovesPartTwo(cupDeck, numMoves):
  i = numMoves
  while i > 0:
    playMove(cupDeck)
    i-=1
    
  # put '1' at end and pop
  cupDeck.rotate(0-(cupDeck.index(1)+1))
  cupDeck.pop()
  
  a = cupDeck.popleft()
  b = cupDeck.popleft()
  return a*b

partTwoInput = partOneInput + list(range((max(partOneInput) + 1), 1000001))
cq2 = deque(maxlen=len(partTwoInput))
for each in partTwoInput:
  cq2.append(each)

# print('Part 2:', playMovesPartTwo(cq2, 10000000))


# Part 2, attempt 2
# still bad, estimate ~60hrs
def playMovesPartTwoNot69Days(theDictionary, numMoves, initialCurrentCupKey):
  currentCupKey = initialCurrentCupKey
  for move in range(1, numMoves+1):
    # get the next 3 cups after current
    the = theDictionary[currentCupKey]
    nex = theDictionary[the]
    thr = theDictionary[nex]
    pickup = [the, nex, thr]
    
    # get the cup current+3 points to before reassigning it to dest+1
    nextCurrentCupKey = theDictionary[thr]
    
    # get destination cup
    destKey = currentCupKey - 1
    while destKey < min(partTwoInput) or destKey in pickup:
      destKey -= 1
      if destKey < min(partTwoInput):
        destKey = max(partTwoInput)
        
    # print('curr ', currentCupKey, '   dest ', destKey, '   nextCurr ', nextCurrentCupKey, '   3 ', the, nex, thr)
    
    theDictionary[currentCupKey] = theDictionary[thr] # current point to +4
    theDictionary[thr] = theDictionary[destKey] # last of pickup point to dest+1
    theDictionary[destKey] = the # dest point to current+1
    
    currentCupKey = nextCurrentCupKey # reassign to next cup found earlier
  
  cupKeyOnePointsTo = theDictionary[1]
  andThatPointsTo = theDictionary[cupKeyOnePointsTo]
  
  return cupKeyOnePointsTo*andThatPointsTo


partTwoInput = partOneInput + list(range((max(partOneInput) + 1), 1000001))
betterStructure = dict()

# link all to next, and end to start
j = 0
while j < len(partTwoInput)-1:
  betterStructure[partTwoInput[j]] = partTwoInput[j+1]
  j += 1
betterStructure[partTwoInput[-1]] = partTwoInput[0]

# play all moves
start = time.time()
print('Part 2:', playMovesPartTwoNot69Days(betterStructure, 10000000, partTwoInput[0]))
end = time.time()
print(str(datetime.timedelta(seconds=(end-start))))
