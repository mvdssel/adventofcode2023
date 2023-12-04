from functools import reduce
import operator

INPUT = 'd03/input-test.txt'
INPUT = 'd03/input.txt'

GEAR = '*'

def isValidPos(x: int, y: int, maxX: int, maxY: int):
    return x >= 0 and y >= 0 and x < maxX and y < maxY

def isSymbol(letter: str):
    return not letter.isalnum() and letter != '.'

def isAdjacentToSymbol(schematic: list, numberPositions: set): 
    maxX = len(schematic)
    maxY = len(schematic[0])
    posDelta = [ -1, 0, 1 ]

    # print('checking ', number)

    for pos in numberPositions:
        for deltaX in posDelta:
            for deltaY in posDelta:
                xToCheck = pos[0] + deltaX
                yToCheck = pos[1] + deltaY
                # print('\t ', (xToCheck, yToCheck))
                if isValidPos(xToCheck, yToCheck, maxX, maxY) and not (xToCheck, yToCheck) in numberPositions:
                    # print('\t\t valid pos')
                    if isSymbol(schematic[xToCheck][yToCheck]):
                        # print('found symbol at ', xToCheck, ':', yToCheck)
                        return True
    
    return False

def getAdjacentNumbers(schematic: list, listOfNumbers: list(), symbolPosition: tuple): 
    maxX = len(schematic)
    maxY = len(schematic[0])
    posDelta = (-1, 0, 1)

    # print('checking ', symbolPositions)

    checkedPositions = set()
    adjacentNumbers = list()

    for deltaX in posDelta:
        for deltaY in posDelta:
            xToCheck = symbolPosition[0] + deltaX
            yToCheck = symbolPosition[1] + deltaY
            posToCheck = (xToCheck, yToCheck)
            # print('\t ', (xToCheck, yToCheck))
            if isValidPos(xToCheck, yToCheck, maxX, maxY) and posToCheck != symbolPosition:
                # print('\t\t valid pos')
                if schematic[xToCheck][yToCheck].isnumeric():
                    # print('number symbol at ', xToCheck, ':', yToCheck)

                    for numberValue, numberPositions in listOfNumbers:
                        if posToCheck not in checkedPositions and posToCheck in numberPositions:
                            adjacentNumbers.append(numberValue)
                            checkedPositions.update(numberPositions)
    
    return adjacentNumbers

def getPartNumber(schematic: list, number: set):
    for pos in number: 
        print(pos)
    return 

schematic = []  # 2D array
listOfSymbols = list()    # set of tupples
listOfNumbers = list()    # list of tupple with the number and set of tupples as positions

with open(INPUT) as f: 
    for x, line in enumerate(f):
        schematic.append(list(line.strip()))

        trackingNumber = False
        numberPositions = set()
        numberValue = 0

        for y, letter in enumerate(schematic[x]):

            if letter.isnumeric() and not trackingNumber:
                # Found start of new number
                trackingNumber = True
                numberPositions.add((x, y))
                numberValue = int(letter)

            elif letter.isnumeric() and trackingNumber:
                # Continue tracking existing number
                numberPositions.add((x, y))
                numberValue = numberValue*10 + int(letter)
            
            else:
                # not letter.isnumeric():
                if trackingNumber:
                    # Stopped tracking number
                    trackingNumber = False

                    # Register number
                    listOfNumbers.append((numberValue, numberPositions))

                    # Reset loop
                    numberValue = 0
                    numberPositions = set()

                if isSymbol(letter):
                    listOfSymbols.append((letter, (x, y)))

        if trackingNumber:
            # Line is done, but number not yet registered
            listOfNumbers.append((numberValue, numberPositions))

############# PART 1 ###############
sumOfPartNumbers = 0

for numberValue, numberPositions in listOfNumbers:
    if isAdjacentToSymbol(schematic, numberPositions):
        sumOfPartNumbers += numberValue

print('Sum of part numbers: ', sumOfPartNumbers)



############# PART 2 ###############
sumOfGearRatios = 0

for symbol, symbolPosition in listOfSymbols:
    if symbol == GEAR:
        adjacentNumbers = getAdjacentNumbers(schematic, listOfNumbers, symbolPosition)
        if len(adjacentNumbers) == 2:
            sumOfGearRatios += reduce(operator.mul, adjacentNumbers, 1)

print('Sum of part gear ratios: ', sumOfGearRatios)