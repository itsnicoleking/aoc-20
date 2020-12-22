import re

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optionalField = 'cid'

# Part 1... like a novice
file = open("./inputs/day4_input.txt", "r")
lineList = [line.rstrip('\n') for line in file]
file.close

numValid = 0
assessFields = []
megaList = []

for line in lineList:
  if not line:
    megaList.append(assessFields)
    assessFields = []
    continue
  halfFields = re.split(' ', line)
  for field in halfFields:
    assessFields.append(re.split(':', field)[0])
  if (lineList.index(line) == len(lineList)-1):
    megaList.append(assessFields)

for passport in megaList:
  if all(elem in passport for elem in requiredFields):
    numValid += 1
  
print ('Part 1:', numValid)



with open('./inputs/day4_input.txt', 'r') as file:
# with open('./inputs/testing.txt', 'r') as file:
  lineList = file.read().split('\n\n')
  lineList = [x.replace('\n', ' ').split() for x in lineList]
  
  passports = []
  
  # Part 1, less garbage
  numValid = 0
  
  for each in lineList:
    passports.append(dict(field.split(':') for field in each))
    
  for passport in passports:
    if all(field in passport for field in requiredFields):
      numValid += 1
      
  print ('Part 1:', numValid)
  

  # Part 2
  numValid = 0
  
  for passport in passports:
    if all(field in passport for field in requiredFields):
      if (
        (1920 <= int(passport['byr']) <= 2002) and
        (2010 <= int(passport['iyr']) <= 2020) and
        (2020 <= int(passport['eyr']) <= 2030) and
        ((passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) or
         (passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76)) and
        (re.match(r'#[\da-f]', passport['hcl'])) and
        (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and
        (re.match(r'\d{9}', passport['pid']))
      ):
        numValid += 1
  
  print ('Part 2:', numValid-1) # TODO: why -1 ??? :(
    # https://www.reddit.com/r/adventofcode/comments/k6e8sw/2020_day_04_solutions/gfaqxdk/
    # needed to check size aswell; i.e. \d{9} will still match size of 10
