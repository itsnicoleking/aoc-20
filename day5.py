file = open("./inputs/day5_input.txt", "r")
# file = open("./inputs/testing.txt", "r")
lineList = file.read().splitlines()
file.close

# Part 1, the hard way
# rows = list(range(0, 128))
# columns = list(range(0, 8))

# def binarySearch(values, keys):
#   start = 0
#   end = len(values)-1
#   mid = 0
#   keySearchPoint = 0
  
#   while start <= end:
#     mid = (start + end) // 2
#     keyChar = keys[keySearchPoint]
    
#     if (keyChar == 'F') or (keyChar == 'L'):
#       end = mid - 1
#     elif (keyChar == 'B') or (keyChar == 'R'):
#       start = mid + 1
    
#     keySearchPoint += 1
    
#   return mid

# for line in lineList:
  # print (line)
  # row = binarySearch(rows, lineList[lineList.index(line)][:7])
  # column = binarySearch(columns, lineList[lineList.index(line)][7:])
  # print (row)
  # print (column)


# Part 1
highestSeatId = 0
seatIds = []

for line in lineList:
  line = line.replace('F', '0')
  line = line.replace('L', '0')
  line = line.replace('B', '1')
  line = line.replace('R', '1')
  seatId = int(line, 2)
  seatIds.append(seatId)
  if seatId > highestSeatId:
    highestSeatId = seatId

print ('Part 1:', highestSeatId)

# Part 2
seatIds = sorted(seatIds)
start = seatIds[0]
end = seatIds[-1]
print ('Part 2:', sorted(set(range(start, end+1)).difference(seatIds)))
