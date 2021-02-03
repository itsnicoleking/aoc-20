import math

file = open("./inputs/day12_input.txt", "r")
lineList = file.read().splitlines()
file.close

# Part 1
ew = 0
ns = 0
orientation = 0 # 0deg is East

i = 0
while i < len(lineList):
  instruction = lineList[i][:1]
  value = int(lineList[i][1:])
  
  if instruction == 'N':
    ns += value
  elif instruction == 'S':
    ns -= value
  elif instruction == 'E':
    ew += value
  elif instruction == 'W':
    ew -= value
  elif instruction == 'L':
    orientation = (orientation - value) % 360
  elif instruction == 'R':
    orientation = (orientation + value) % 360
  elif instruction == 'F':
    if orientation == 0:
      ew += value
    elif orientation == 90:
      ns -= value
    elif orientation == 180:
      ew -= value
    elif orientation == 270:
      ns += value
  
  i += 1
  
print ('Part 1:', (abs(ew) + abs(ns)))


# Part 2
def rotate(origin, point, angle):
  ox, oy = origin
  px, py = point
  cos = math.cos(angle)
  sin = math.sin(angle)
  xdiff = px - ox
  ydiff = py - oy
  
  qx = ox + cos * xdiff - sin * ydiff
  qy = oy + sin * xdiff + cos * ydiff
  return qx, qy

shipNS = 0
shipEW = 0
wayptNS = 1
wayptEW = 10

j = 0
while j < len(lineList):
  instruction = lineList[j][:1]
  value = int(lineList[j][1:])
  og = (shipEW, shipNS)
  pt = (wayptEW, wayptNS)
  
  if instruction == 'N':
    wayptNS += value
  elif instruction == 'S':
    wayptNS -= value
  elif instruction == 'E':
    wayptEW += value
  elif instruction == 'W':
    wayptEW -= value
  elif instruction == 'L':
    rt = rotate(og, pt, math.radians(value))
    wayptEW = int(rt[0])
    wayptNS = int(rt[1])
  elif instruction == 'R':
    rt = rotate(og, pt, math.radians(-value))
    wayptEW = int(rt[0])
    wayptNS = int(rt[1])
  elif instruction == 'F':
    diffNS = wayptNS - shipNS
    diffEW = wayptEW - shipEW
    
    shipNS += value * diffNS
    shipEW += value * diffEW
    wayptNS = shipNS + diffNS
    wayptEW = shipEW + diffEW
  
  j += 1

print ('Part 2:', (abs(shipEW) + abs(shipNS)))
