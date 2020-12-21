# file = open("./inputs/day5_input.txt", "r")
file = open("./inputs/testing.txt", "r")
lineList = file.read().splitlines()
file.close

rows = list(range(0, 128))
columns = list(range(0, 8))

row = 0
column = 0

def findRow(rowArray, rowKeys):
  start = 0
  end = len(rowArray)-1
  mid = 0
  keySearchPoint = 0
  
  while start <= end:
    mid = (start + end) // 2
    
    print ('keypoint', keySearchPoint)
    print ('Start', start)
    print ('End', end)
    print ('Mid', mid)
    
    if rowKeys[keySearchPoint] == 'F':
      end = mid - 1
      print ('F')
    elif rowKeys[keySearchPoint] == 'B':
      start = mid + 1
      print ('B')
    
    print ()
    
    keySearchPoint += 1

def findColumn(columnArray, columnKeys):
  start = 0
  end = len(columnArray)-1
  mid = 0
  keySearchPoint = 0
  
  while start <= end:
    mid = (start + end) // 2
    
    print ('keypoint', keySearchPoint)
    print ('Start', start)
    print ('End', end)
    print ('Mid', mid)

    if columnKeys[keySearchPoint] == 'L':
      end = mid - 1
      print ('L')
    elif columnKeys[keySearchPoint] == 'R':
      start = mid + 1
      print ('R')
      
    print ()
    
    keySearchPoint += 1


# findRow(rows, lineList[0][0:7])
findColumn(columns, lineList[0][7:10])


  
  