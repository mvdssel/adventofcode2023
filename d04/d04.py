INPUT = 'd04/input-test.txt'
INPUT = 'd04/input.txt'

sumCardPoints = 0

with open(INPUT) as f:
    for card in f:
        cardTitle, cardNumbers = card.split(':')

        winningNumbers, myNumbers = cardNumbers.split('|')
        winningNumbers = set((int(n) for n in winningNumbers.split()))
        myNumbers = set((int(n) for n in myNumbers.split()))
        
        cardPoints = 0

        for myNumber in myNumbers:
            if myNumber in winningNumbers:
                if cardPoints == 0:
                    cardPoints = 1
                else:
                    cardPoints *= 2
        
        sumCardPoints += cardPoints

print('There are {} card points.'.format(sumCardPoints))