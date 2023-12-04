from functools import reduce
import operator

INPUT = 'd02/input-1-test.txt'
INPUT = 'd02/input-1.txt'

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sumOfValidGameIds = 0
totalGamePower = 0

with open(INPUT) as f:
    for line in f:
        gameTitle, gameInput = line.split(':')
        # print(gameInput)

        rounds = gameInput.split(';')
        # print('\t', rounds)

        isValidGame = True

        minCubeAmount = {
            'red': -1,
            'green': -1,
            'blue': -1 
        }

        for round in rounds:
            picks = round.split(',')
            # print('\t\t', picks)

            for pick in picks:
                pickAmount, pickColor = pick.split()
                pickAmount = int(pickAmount)
                # print('\t\t\t', pickAmount, pickColor)

                if minCubeAmount[pickColor] < pickAmount:
                    minCubeAmount[pickColor] = pickAmount

                if bag[pickColor] < pickAmount:
                    isValidGame = False
                    # print('\t\t\t\tNOT POSSIBLE!!!')
        
        gamePower = reduce(operator.mul, minCubeAmount.values(), 1)
        # print(gameTitle, ': ', gamePower)
        totalGamePower += gamePower

        if isValidGame:
            gameId = int(gameTitle.split()[1])
            sumOfValidGameIds += gameId

print('Sum of valid game IDs: ', sumOfValidGameIds)
print('Total game power: ', totalGamePower)
