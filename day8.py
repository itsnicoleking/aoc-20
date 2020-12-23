import copy

file = open("./inputs/day8_input.txt", "r")
lineList = file.read().splitlines()
file.close

# Part 1
accumulator = 0
visited = []

i = 0
while i < len(lineList):
  instruction = lineList[i].split()[0]
  operator = lineList[i].split()[1][:1]
  move = int(lineList[i].split()[1][1:])
  
  if i in visited:
    break
  
  visited.append(i)
  
  if instruction == 'nop':
    i += 1
  elif instruction == 'acc':
    if operator == '-':
      accumulator -= move
    elif operator == '+':
      accumulator += move
    i += 1
  elif instruction == 'jmp':
    if operator == '-':
      i -= move
    elif operator == '+':
      i += move
      
print ('Part 1:', accumulator)


# Part 2
def runInstructions(instructions):
  accumulator = 0
  visited = []
  i = 0
  while i < len(instructions):
    instruction = instructions[i].split()[0]
    operator = instructions[i].split()[1][:1]
    move = int(instructions[i].split()[1][1:])
    
    if i in visited:
      return [False, accumulator]
    
    visited.append(i)
    
    if instruction == 'nop':
      i += 1
    elif instruction == 'acc':
      if operator == '-':
        accumulator -= move
      elif operator == '+':
        accumulator += move
      i += 1
    elif instruction == 'jmp':
      if operator == '-':
        i -= move
      elif operator == '+':
        i += move
  return [True, accumulator]

def swapInstruction(instructions, pos):
  instCopy = copy.deepcopy(instructions)
  inst = instCopy[pos].split()[0]
  if inst == 'jmp':
    instCopy[pos] = 'nop' + ' ' + instCopy[pos].split()[1]
  elif inst == 'nop':
    instCopy[pos] = 'jmp' + ' ' + instCopy[pos].split()[1]

  return instCopy

j = 0
while j < len(lineList):
  newInstructions = swapInstruction(lineList, j)
  result = runInstructions(newInstructions)
  if result[0]:
    print ('Part 2:', result[1])
    break
  elif not result[0]:
    j += 1
