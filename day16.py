import math

file = open("./inputs/day16_input.txt", "r")
lineList = file.read().splitlines()
file.close

# Part 1
section = 0
fields = dict()
errorScanRate = 0

def setupFields(line):
  splitLine = line.split(': ') # into field name & ranges
  ranges = splitLine[1].split(' or ')
  
  # Assuming always 2 ranges per field
  vals1 = ranges[0].split('-')
  range1 = getRange(int(vals1[0]), int(vals1[1]))
  vals2 = ranges[1].split('-')
  range2 = getRange(int(vals2[0]), int(vals2[1]))
  
  # dict {field: [valid numbers]}
  fields[splitLine[0]] = range1 + list(set(range2) - set(range1))

def getRange(a, b):
  return list(range(a, b+1))


for line in lineList:
  if line == '':
    section += 1
    continue
  else:
    if section == 0:
      setupFields(line)
    elif section == 2 and 'nearby tickets' not in line: # skip header line
      nearbyTicket = [int(x) for x in line.split(',')]
      for num in nearbyTicket: # for each number in nearby ticket
        valid = False
        for key in fields:
          if num in fields[key]: # is it valid for any field
            valid = True
            break
        if not valid:
          errorScanRate += num
      
print('Part 1:', errorScanRate)


# Part 2
section = 0
fields = dict()
yourTicket = []
validTickets = []

def addIfValidTicket(line):
  ticket = [int(x) for x in line.split(',')]
  ticketValid = True
  for num in ticket: # for each number in ticket
    valid = False
    for key in fields:
      if num in fields[key]: # is it valid for any field
        valid = True
        break
    if not valid:
      ticketValid = False
  if ticketValid:
    validTickets.append(ticket)

def doesColumnFollowRule(column, rule):
  for value in column:
    if not doesValueFollowRule(value, rule):
      return False
  return True

def doesValueFollowRule(value, rule):
  return value in rule


# MAIN:

# Setup fields and valid tickets
for line in lineList:
  if line == '':
    section += 1
    continue
  else:
    if section == 0:
      setupFields(line)
    elif section == 1 and 'your ticket' not in line:
      yourTicket = [int(x) for x in line.split(',')]
      addIfValidTicket(line)
    elif section == 2 and 'nearby tickets' not in line:
      addIfValidTicket(line)

# Get values in each column of ticket
# i.e. [[a,b,c], [d,e,f]] => [(a,d), (b,e), (c,f)]
ticketCols = list(zip(*validTickets)) # TODO: why does this need unpacking operator * ?

possiblePositions = {field: [] for field in fields.keys()}

# Find which column/s each field could be
for j, col in enumerate(ticketCols):
  for field, validNums in fields.items():
    if doesColumnFollowRule(col, validNums):
      possiblePositions[field].append(j)

# Find field that has only 1 position option
# Save that field at that position, & remove pos
# as possibility from all other fields
fieldsPositions = dict()
while len(fieldsPositions) < len(fields):
  for field, possibilities in possiblePositions.items():
    if len(possibilities) == 1:
      foundPosition = possibilities[0]
      fieldsPositions[field] = foundPosition
      for k in possiblePositions.values():
        if foundPosition in k:
          k.remove(foundPosition)

yourTicketDepartureFields = []
for field, finalPosition in fieldsPositions.items():
  if field.startswith('departure'):
    yourTicketDepartureFields.append(yourTicket[finalPosition])
    
print('Part 2:', math.prod(yourTicketDepartureFields))