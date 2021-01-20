from itertools import permutations

# file = open("./inputs/day10_input.txt", "r")
file = open("/Users/nicoleking/Desktop/aoc-20/inputs/testing.txt", "r")
lineList = file.read().splitlines()
lineList = [int(line) for line in lineList]
file.close

adapters = sorted(lineList)
adapters.append(adapters[-1]+3)
adapters.insert(0, 0)

# Part 1
numOneDiff = 0
numThreeDiff = 0

i = 0
while i < len(adapters)-1:
  if adapters[i+1] - adapters[i] == 1:
    numOneDiff += 1
  elif adapters[i+1] - adapters[i] == 3:
    numThreeDiff += 1
  i += 1

print ('Part 1:', numOneDiff*numThreeDiff)


# Part 2, attempt 1
# matrix = [[0 for x in range(len(adapters))] for y in range(len(adapters))]

# j = 0
# while j < len(adapters)-1:
#   if (adapters[j]+1) in adapters:
#     pos = adapters.index(adapters[j]+1)
#     matrix[j][pos] = 1
#   if (adapters[j]+2) in adapters:
#     pos = adapters.index(adapters[j]+2)
#     matrix[j][pos] = 1
#   if (adapters[j]+3) in adapters:
#     pos = adapters.index(adapters[j]+3)
#     matrix[j][pos] = 1
#   j+=1

# for p in permutations(matrix):
#   print(p)
# allPossible = permutations(matrix)
# print(len(list(allPossible)))



# Part 2, take 2
matrix = [[]]

j = 0
while j < len(adapters)-1:
  vals = []
  if (adapters[j]+1) in adapters:
    vals.append(adapters.index(adapters[j]+1))
  if (adapters[j]+2) in adapters:
    vals.append(adapters.index(adapters[j]+2))
  if (adapters[j]+3) in adapters:
    vals.append(adapters.index(adapters[j]+3))
  matrix.insert(j, vals)
  j+=1

# print(matrix)

# https://stackoverflow.com/questions/43127332/python-list-of-lists-specific-path-combinations-or-permutations
setOnlyDifferentMatrixValues = set()
for row in range(len(matrix)):
  for column in range(len(matrix[row])):
    setOnlyDifferentMatrixValues.add(matrix[row][column])
allPossiblePaths = permutations(setOnlyDifferentMatrixValues)
print(list(allPossiblePaths))


# NOTES
# pt 2 is dynamic programming problem
# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gf9mvrh/
# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfa9gjn/
